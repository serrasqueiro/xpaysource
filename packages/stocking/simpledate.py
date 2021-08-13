# simpledate.py  (c)2021  Henrique Moreira

"""
Yet another Simplified string dates
"""

# pylint: disable=unused-argument

import datetime

def date_str(obj) -> str:
    """ Input 'YYYY-mm-dd' or 'dd-mm-YYYY',
    Output: YYYY.mm.dd; on error, it returns empty.
    """
    if isinstance(obj, (tuple, list)):
        year, month, day = obj
    elif isinstance(obj, datetime.datetime):
        year, month, day = obj.year, obj.month, obj.day
    elif isinstance(obj, str):
        adate = obj
        fields = adate.split("-")
        assert len(fields) == 3, f"Does not look a date: '{adate}'"
        aaa, _, _ = fields
        if len(aaa) >= 4:
            year, month, day = fields
        else:
            day, month, year = fields
    else:
        return ""
    dttm = datetime.datetime(int(year), int(month), int(day))
    astr = dttm.strftime("%Y.%m.%d")
    return astr

def looks_date_str(obj) -> str:
    """ Returns a non-empty string in case 'obj' string looks a date.
    """
    if not isinstance(obj, str):
        return ""
    spl = obj.split("-")
    if len(spl) != 3:
        return ""
    day, month, year = spl
    if not year.isdigit():
        return ""
    when = int(year)
    if 1970 <= when <= 2999:
        astr = date_str((year, month, day))
    else:
        astr = ""
    return astr

def time_str(atime) -> str:
    """ Returns the string for 'atime', if atime is of type datetime.time!
    """
    if isinstance(atime, datetime.time):
        hour, minu = atime.hour, atime.minute
        return f"{hour:02}:{minu:02}"
    return ""

# This is a module
if __name__ == "__main__":
    print("import stocking.simpledate as simpledate !")
    print("Sample:", date_str(datetime.datetime(2021, 8, 13)))
