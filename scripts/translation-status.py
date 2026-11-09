#!/usr/bin/env python3
"""Report translation progress per section, or list the files that still need work.

usage: translation-status.py [--lang es]
       translation-status.py --list missing|stale SECTION [--limit N] [--offset N] [--by-rank]

SECTION is a folder under content/ ('tools', 'professionals', ...) or '.' for top-level pages.
A file is 'ok' when content_<lang>/ has it and its i18n_source matches the current English file,
'stale' when the English file changed since, and 'missing' when it has not been translated.
--by-rank orders the list by the English file's rank (highest first), the order bulk runs follow.
"""
import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "i18n"))
import rules  # noqa: E402


def state(rel: Path, root: Path):
    tr = root / rel
    if not tr.exists():
        return "missing"
    m = re.search(r"^i18n_source:\s*'?([0-9a-f]+)'?\s*$", tr.read_text(encoding="utf-8").split("\n---", 1)[0], flags=re.M)
    return "ok" if m and m.group(1) == rules.source_hash(rules.SOURCE / rel) else "stale"


def rank_of(rel: Path):
    try:
        data, _ = rules.load(rules.SOURCE / rel)
        return int(data.get("rank") or 0)
    except Exception:
        return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="es")
    ap.add_argument("--list", choices=["missing", "stale"])
    ap.add_argument("section", nargs="?")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--offset", type=int, default=0)
    ap.add_argument("--by-rank", action="store_true")
    a = ap.parse_args()
    root = rules.LANGS[a.lang]
    files = rules.english_files()

    if a.list:
        sec = "" if a.section in (None, ".") else a.section
        pick = [r for r in files if rules.section_of(r) == sec and state(r, root) == a.list]
        if a.by_rank:
            pick.sort(key=lambda r: (-rank_of(r), str(r)))
        pick = pick[a.offset:]
        if a.limit:
            pick = pick[: a.limit]
        for r in pick:
            print(r)
        return

    table = collections.defaultdict(collections.Counter)
    for r in files:
        table[rules.section_of(r) or "(top-level)"][state(r, root)] += 1
    print(f"{'section':<20}{'ok':>7}{'stale':>7}{'missing':>9}{'total':>7}")
    tot = collections.Counter()
    for sec in sorted(table):
        c = table[sec]
        tot.update(c)
        print(f"{sec:<20}{c['ok']:>7}{c['stale']:>7}{c['missing']:>9}{sum(c.values()):>7}")
    print(f"{'TOTAL':<20}{tot['ok']:>7}{tot['stale']:>7}{tot['missing']:>9}{sum(tot.values()):>7}")


if __name__ == "__main__":
    main()
