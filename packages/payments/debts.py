# debts.py  (c)2021  Henrique Moreira

"""
Miscelaneous functions for payment methods
"""
# pylint: disable=unused-argument


import payments.freedate as freedate
import payments.ptpays as ptpays
from payments.debug import bprint, set_debug


AMBIGUOUS_COMPANY = "@(ambiguous)"


def sample() -> bool:
    """ Just a basic sample for usage.
    """
    set_debug(1)
    assert scrub_infos()
    num_contract = 31272397605
    optional_contract = f" {num_contract}" if num_contract else ""
    debt_desc = "DDPT16103627 EASYPAY" + optional_contract
    key = get_company_str(debt_desc, "18-06-2019")
    print("get_company_str():", debt_desc, "; is:", key)
    assert key
    key = get_company_str("PAG.SERV 10611/nnn EASYPAY")
    print("get_company_str('...10611..'):", key)
    assert key
    return key != ""

def scrub_infos() -> bool:
    """ Scrub information, and assert if something not ok in variables.
    """
    ctxs, urls = ptpays.INFO_CONTEXTS, ptpays.URL_CONTEXTS
    for name in urls:
        acontext = ctxs.get(name)
        if acontext is None:
            return False
        assert isinstance(acontext, tuple)
        cont = urls[name]
        assert isinstance(cont, tuple)
        assert len(cont) == 1
        url = cont[0]
        assert isinstance(url, str), "url should be a string, even empty"
        if not url:
            continue
        assert url.startswith(("http://", "https://",)), f"Invalid URL: {url}"
    return True

def get_company_str(debt_desc: str, date: str="") -> str:
    """ Returns the company-key, if found, or empty if not found.
    :param debt_desc: bank account debt description
    :param date: free, optional date (either dd-mm-YYYY or YYYY-mm-dd format)
    :return: string, the company key.
    """
    words = [word for word in debt_desc.split(' ') if word]
    if not words:
        return ""
    if date:
        assert len(date) == 10, "date string size should be 10"
        datestr = freedate.dotted_date(date)
    else:
        datestr = "-"
    assert datestr
    all_methods = [
        ptpays.METHODS_2021,
        ]
    astr = company_from_methods(words, ptpays.INFO_CONTEXTS, all_methods, date)
    return astr

def company_from_methods(words: list, context_infos: dict, methods: list, date="") -> str:
    """ Returns the company-key, if found, or empty if not found.
    :param words: debt description, as a list
    :param context_infos: dictionary with all contexts
    :param methods: list of methods, each one is a dictionary
    :param date: optional date (either dd-mm-YYYY or YYYY-mm-dd format)
    :return: string, the company key.
    """
    company = ""
    context, idxs = context_in_words(words, context_infos)
    bprint(f"Debug: {words}: '{context}', idxs={idxs}")
    if not context or not idxs:
        if not idxs:
            assert not context, f"Unexpected context string: {context}"
        return ""
    at_idx, hint = idxs[0]
    assert at_idx >= 1, "INFO_CONTEXTS format should be e.g. '$1 EASYPAY'"
    assert words
    if at_idx > len(words):
        return ""
    aref = words[at_idx-1]
    if hint == "/":
        aref = aref.split("/")[0]
    if not aref:
        return ""
    for method in methods:
        assert isinstance(method, dict)
        what = method.get(aref)
        if what:
            if company:
                # Check if it matches
                if company != what:
                    return AMBIGUOUS_COMPANY
            else:
                company = what
    return company


def context_in_words(words, context_infos: dict) -> tuple:
    """ Returns a non-empty string if context is found in a bank debt string.
    Context is e.g. 'EASYPAY'.
    """
    candidates = list()
    infos = list()
    if not words:
        return "", None
    for ctx, tup in context_infos.items():
        infos += [(ctx, aformat) for aformat in tup]
    for ctx, aformat in infos:
        idx, where, idx_list = 0, list(), list()
        for aref in aformat.split(' '):
            if not aref:
                continue
            idx += 1
            hint = ""
            if aref.startswith("$") or aref in ("*",):
                idx_ref = aref[1:]
                if idx_ref.endswith("/"):
                    idx_val = int(idx_ref[:-1])
                    hint = "/"
                elif aref == "*":
                    idx_val = None
                else:
                    idx_val = int(idx_ref)
                if idx_val is not None:
                    assert idx_val == idx
                    idx_list.append((idx, hint))
            else:
                where.append((aref, idx))
        if not where:
            continue
        assert len(where) == 1, "Expected e.g. '$1 XYZ $3'"	# Not 'ABC DEF'...
        context, idx = where[0]
        assert context
        idx -= 1
        # if idx_list and idx_list[0][1] == "/": ...
        try:
            word_there = words[idx]
        except IndexError:
            word_there = None
        if word_there == context:
            candidates.append((ctx, idx_list))
    if not candidates:
        return "", None
    if len(candidates) > 1:
        astr = ';'.join([ctx_name for ctx_name, _ in candidates])
        msg = f"ambiguous contexts: {astr}"
        bprint("Debug:", msg, "")
        return msg, None
    ctx, idx_list = candidates[0]
    if ctx and not idx_list:
        idx_list = [(1, "")]
    return ctx, tuple(idx_list)


# Main script
if __name__ == "__main__":
    print("import payments.debts as debts !")
    print("\n...Follows just a sample.\n")
    sample()
