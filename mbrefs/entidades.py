#-*- coding: utf-8 -*-
# entidades.py  (c)2021  Henrique Moreira

"""
Reader of tuplets
"""

# pylint: disable=missing-function-docstring

import sys
import json
from waxpage.redit import char_map


def main():
    """ Main script.
    """
    code = run_main(sys.stdout, sys.stderr, sys.argv[1:])
    if code is None:
        print("""entidades.py command [options]

Commands are:
   to-json     Convert (4) tuplets to json
""")
    sys.exit(code if code else 0)


def run_main(out, err, args):
    """ Main run: returns 0 on success.
    """
    msg = ""
    if not args:
        return None
    cmd = args[0]
    param = args[1:]
    if param:
        return None
    if cmd == "to-json":
        msg = to_json(out, open("input.txt", "r", encoding="ISO-8859-1").read())
        if msg:
            err.write(f"ERROR: {msg}\n")
    else:
        return None
    return 1 if msg else 0


def to_json(out, data:str, debug:int=0) -> str:
    """ Converts triplets to json file
    """
    out_encode = "ISO-8859-1"
    idx = 0
    lines = data.splitlines()
    res = []
    used_refs = {}
    for line in lines:
        shown = line.replace("\t", "|")
        idx += 1
        try:
            ref, name, entity, associated = line.split("\t")
        except ValueError:
            msg = f"Unexpected line ({idx}): {shown}"
            return msg
        shown = trim_chars(line, ("_", " ")).replace("_", " ")
        ref, name, entity, associated = shown.split("\t")
        iso_name = char_map.simpler_ascii(name, 1)
        entity = char_map.simpler_ascii(entity)
        associated = char_map.simpler_ascii(entity, 1)
        if not entity:
            entity = None
        if "digo" in ref:
            continue
        ref = int(ref)
        elem = {
            "ref": ref,
            "name": name,
            "iso-name": iso_name,
            "entity": entity,
            "associated": associated,
        }
        res.append(elem)
        assert ref not in used_refs, f"Duplicate ref: {ref}, elem={elem}"
        used_refs[ref] = elem
        assert name.strip() == name, f"Unstripped: '{name}'"
        if debug <= 0:
            continue
        what = f'; associated: {associated}' if associated else ""
        item = f'{ref} name="{iso_name}" entity={entity}{what}'
        print(f"Line {idx}/{len(lines)}: {item}", end="\n\n")
    if not out:
        return ""
    ordered = []
    for key in sorted(used_refs):
        elem = used_refs[key]
        ordered.append(elem)
    astr = json.dumps(ordered, indent=2, sort_keys=True)
    out.write(astr + "\n")
    return ""


def trim_chars(astr:str, tups):
    new = astr
    for achr in tups:
        assert achr
        while True:
            shown = new.replace(achr + achr, achr)
            if shown == new:
                break
            new = shown
    return new


# Main script
if __name__ == "__main__":
    main()
