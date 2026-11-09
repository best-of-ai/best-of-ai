#!/usr/bin/env python3
"""Check the i18n/*.yaml files against the templates.

usage: check-i18n.py [--prune]
  reports  - keys used in layouts/ but missing from a language file
           - keys present in one language file but not another
           - keys no template uses (they pile up when copy is reworded)
  --prune  removes the unused keys from every i18n/*.yaml file

Keys built at render time (printf "enum_%s" ...) are matched by prefix, so enum_*, kind_*, seo_cp_title_*
and similar are never reported as unused.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"
LAYOUTS = ROOT / "layouts"

text = "\n".join(p.read_text(encoding="utf-8") for p in LAYOUTS.rglob("*") if p.is_file() and p.suffix in {".html", ".xml", ".json", ".txt"})
used = set(re.findall(r'i18n\s+"([a-z0-9_]+)"', text))
# keys can also be chosen through a variable ({{ $what := "what_ai_tools" }} ... i18n $what), so any quoted
# string that equals a key counts as a use of that key
literals = set(re.findall(r'"([a-z0-9_]+)"', text))
prefixes = set(re.findall(r'printf\s+"([a-z0-9_]+)%s"', text))

langs = {p.stem: {str(k): v for k, v in (yaml.safe_load(p.read_text(encoding="utf-8")) or {}).items()} for p in sorted(I18N.glob("*.yaml"))}
default = "en"
bad = False

for lang, keys in langs.items():
    missing = sorted(k for k in used if k not in keys and not any(k.startswith(p) for p in prefixes))
    if missing:
        bad = True
        print(f"[{lang}] used in templates but missing: {', '.join(missing)}")
    other = sorted(set(langs[default]) ^ set(keys)) if lang != default else []
    if other:
        bad = True
        print(f"[{lang}] differs from {default}: {', '.join(other)}")


def is_used(k):
    return k in used or k in literals or any(k.startswith(p) for p in prefixes)


unused = sorted(k for k in langs[default] if not is_used(k))
print(f"{len(unused)} unused keys" + (": " + ", ".join(unused[:12]) + (" ..." if len(unused) > 12 else "") if unused else ""))

if "--prune" in sys.argv and unused:
    drop = set(unused)
    for p in sorted(I18N.glob("*.yaml")):
        out, skipping = [], False
        for line in p.read_text(encoding="utf-8").split("\n"):
            m = re.match(r"^([a-z0-9_]+):", line)
            if m:
                skipping = m.group(1) in drop
            elif line.strip() and not line.startswith((" ", "#")):
                skipping = False
            if not skipping:
                out.append(line)
        p.write_text("\n".join(out), encoding="utf-8")
    print(f"pruned {len(unused)} keys from {len(list(I18N.glob('*.yaml')))} files")

sys.exit(1 if bad else 0)
