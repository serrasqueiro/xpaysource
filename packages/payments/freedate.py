# freedate.py  (c)2021  Henrique Moreira

"""
Simplified string dates
"""

# pylint: disable=unused-argument

import datetime

def dotted_date(adate: str) -> str:
    """ Input 'YYYY-mm-dd' or 'dd-mm-YYYY',
    Output: YYYY.mm.dd; on error, it returns empty.
    """
    if isinstance(adate, (tuple, list)):
        year, month, day = adate
        return dotted_date(f"{year}-{month}-{day}")
    if not isinstance(adate, str):
        return ""
    fields = adate.split("-")
    assert len(fields) == 3, f"Does not look a date: '{adate}'"
    aaa, _, _ = fields
    if len(aaa) >= 4:
        year, month, day = fields
    else:
        day, month, year = fields
    # my_datetime = time.strptime("2020-02-29", "%Y-%m-%d")
    dttm = datetime.datetime(int(year), int(month), int(day))
    astr = dttm.strftime("%Y.%m.%d")
    return astr


# This is a module
if __name__ == "__main__":
    print("import payments.freedate as freedate !")
