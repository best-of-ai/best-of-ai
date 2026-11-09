#!/usr/bin/env python3
"""Check translated files in content_<lang>/ against their English sources.

usage: validate-translation.py [--lang es] [--stamp] [--allow-stale] [paths...]
  paths   files or directories under content_<lang>/ (default: everything)
  --stamp write/update the i18n_source hash first (translators run this after saving a file)
  --allow-stale do not fail on a stale i18n_source (CI uses this so an English edit never blocks a deploy)

Per file it checks: valid frontmatter; every key outside the section's TEXT_KEYS identical to English;
text keys present exactly when English has them, non-empty, and not left in English; same list shapes;
body keeps the same number of paragraphs, headings, code fences and the same links in the same order,
and a body of 40 characters or more must not be left identical to English;
i18n_source matches the current English file. Exit status 1 when anything fails.
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "i18n"))
import rules  # noqa: E402


def links(body):
    return re.findall(r"\]\(([^)\s]+)", body)


def paragraphs(body):
    return [p for p in re.split(r"\n\s*\n", body.strip()) if p.strip()]


def stamp(path: Path, en_path: Path):
    raw, body = rules.split_frontmatter(path.read_text(encoding="utf-8"))
    raw = re.sub(r"^i18n_source:.*\n?", "", raw, flags=re.M).rstrip("\n")
    raw += f"\ni18n_source: '{rules.source_hash(en_path)}'"
    path.write_text(f"---\n{raw}\n---\n{body}", encoding="utf-8")


def check(path: Path, root: Path, lang: str, allow_stale: bool = False):
    errs = []
    rel = path.relative_to(root)
    en_path = rules.SOURCE / rel
    if not en_path.exists():
        return [f"no English source {en_path.relative_to(rules.ROOT)}"]
    try:
        tr, tr_body = rules.load(path)
    except Exception as e:  # yaml or frontmatter problems
        return [f"cannot parse: {e}"]
    en, en_body = rules.load(en_path)
    keys = rules.text_keys(rel)

    for k in sorted(set(en) | set(tr)):
        if k == "i18n_source":
            continue
        if k not in tr:
            errs.append(f"missing key '{k}'")
        elif k not in en:
            errs.append(f"extra key '{k}'")
        elif k in keys:
            ev, tv = en[k], tr[k]
            if isinstance(ev, str):
                if ev.strip() and not str(tv).strip():
                    errs.append(f"'{k}' is empty")
                elif len(ev) >= rules.MAY_EQUAL_MIN_LEN and ev.strip() == str(tv).strip():
                    errs.append(f"'{k}' left in English")
            elif isinstance(ev, dict) and k == "params":
                tv = tv or {}
                if set(ev) != set(tv):
                    errs.append("'params' keys differ")
                for pk in ev:
                    if pk != "period" and ev[pk] != tv.get(pk):
                        errs.append(f"'params.{pk}' must stay identical to English")
            elif isinstance(ev, list):
                if not isinstance(tv, list) or len(ev) != len(tv):
                    errs.append(f"'{k}' list length differs")
            elif type(ev) is not type(tv):
                errs.append(f"'{k}' changed type")
        elif k == "url":
            # Hugo does not prefix a front-matter url with the language, so the copy carries it
            want = f"/{lang}{en[k]}"
            if tr[k] != want:
                errs.append(f"'url' must be {want!r} (Hugo adds no language prefix to an explicit url)")
        elif en[k] != tr[k]:
            errs.append(f"'{k}' must stay identical to English ({en[k]!r} -> {tr[k]!r})")

    if en_body.strip() or tr_body.strip():
        if bool(en_body.strip()) != bool(tr_body.strip()):
            errs.append("body present in only one of the files")
        else:
            if len(paragraphs(en_body)) != len(paragraphs(tr_body)):
                errs.append(f"paragraph count {len(paragraphs(tr_body))} != {len(paragraphs(en_body))}")
            if len(re.findall(r"^#{1,6} ", en_body, flags=re.M)) != len(re.findall(r"^#{1,6} ", tr_body, flags=re.M)):
                errs.append("heading count differs")
            if en_body.count("```") != tr_body.count("```"):
                errs.append("code fence count differs")
            if links(en_body) != links(tr_body):
                errs.append("links differ from English (same URLs, same order required)")
            if en_body.strip() == tr_body.strip() and len(en_body.strip()) >= rules.MAY_EQUAL_MIN_LEN:
                errs.append("body left in English")

    if not allow_stale and rules.section_of(rel) not in rules.SKIP_SECTIONS and tr.get("i18n_source") != rules.source_hash(en_path):
        errs.append("i18n_source missing or stale (run with --stamp)")
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="es")
    ap.add_argument("--stamp", action="store_true")
    ap.add_argument("--allow-stale", action="store_true")
    ap.add_argument("paths", nargs="*")
    a = ap.parse_args()
    root = rules.LANGS[a.lang]

    files = []
    for p in (a.paths or [str(root)]):
        p = Path(p).resolve()
        files += sorted(p.rglob("*.md")) if p.is_dir() else [p]

    bad = 0
    for f in files:
        rel = f.relative_to(root)
        if a.stamp and (rules.SOURCE / rel).exists():
            try:
                stamp(f, rules.SOURCE / rel)
            except ValueError:
                pass
        errs = check(f, root, a.lang, a.allow_stale)
        if errs:
            bad += 1
            print(f"FAIL content_{a.lang}/{rel}")
            for e in errs:
                print(f"     - {e}")
    print(f"{len(files) - bad}/{len(files)} files ok")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
