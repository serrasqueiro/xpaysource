#-*- coding: utf-8 -*-
# stockr.py  (c)2021  Henrique Moreira

"""
stockr - reader for 'stock' transactions within a table.
Basic Libre/Excel reader (using filing.xcelent 'openpyxl' wrapper).
"""

# pylint: disable=no-self-use, missing-function-docstring

import datetime
import openpyxl
import stocking.simpledate as simpledate
import filing.xcelent as xcelent


def main_test():
    """ Basic tests! """
    fname = "/tmp/a.xlsx"
    wbk = openpyxl.load_workbook(fname)
    libre = xcelent.Xcel(wbk, "stocks")
    sheet = libre.get_sheet(1)
    table = xcelent.Xsheet(sheet)
    idx = 0
    for row in table.rows:
        idx += 1
        shown = [item.value for item in row]
        print(idx, shown)
    folio = StockFolio(table, "stocks")
    print(">>> folio.name:", folio.name, "; number of columns:", folio.n_columns())
    print("table.column_refs:", folio.columns())
    folio.parse()
    for idx in folio.y_indexes():
        shown = folio.row(idx)
        pre = "" if len(shown) == folio.n_columns() else "!"
        print(f"{pre}{idx}\t{shown}")
    print("# warnings:", folio.get_warnings())


class StockFolio(xcelent.Libre):
    """ Class to hold Stock transactions/ portfolio;
	aka as 'Transactions_accoes.xlsx'
    """
    _table = None
    _rows = None
    _rdict = None
    _issues = None

    """ Stocks read from source (Libre/Excel) """
    def __init__(self, rows=None, aname=""):
        super().__init__()
        self.name = aname
        self._table = None
        if isinstance(rows, xcelent.Xsheet):
            self._table = rows
            self._rows = self._table.rows
        else:
            self._rows = rows
        self._rdict = {0: None}
        self._issues = {
            "warn": {"extra-lines": list()},
        }

    def row(self, num=0) -> list:
        """ Returns the row with index 'num' (num = 0 for the header).
        """
        result = self._rdict[num]
        return result

    def all_rows(self) -> list:
        """ Returns all rows, including the header. """
        return sorted(self._rdict)

    def columns(self) -> dict:
        """ Returns the dictionary of 'A'/1 headings. """
        if not self._table:
            return dict()
        return self._table.column_refs

    def n_columns(self) -> int:
        """ Returns the number of columns. """
        plus = len(self._table.column_refs["@letters"])
        assert plus > 0
        return plus - 1

    def get_warnings(self) -> dict:
        """ Returns warnings found during parsing. """
        return self._issues["warn"]

    def y_indexes(self) -> list:
        return sorted(self._rdict)[1:]

    def parse(self, header_lines=1):
        """ Parse existing rows 'values'. """
        header = self._rows[0] if header_lines > 0 else list()
        self._rdict[0] = header
        self._parse(header_lines, self._rows[1:])

    def better(self, value):
        astr = value
        if isinstance(value, datetime.datetime):
            astr = simpledate.date_str(value)
        elif isinstance(value, datetime.time):
            astr = simpledate.time_str(value)
        elif isinstance(value, str):
            new = simpledate.looks_date_str(value)
            if new:
                return new
        return astr

    def _parse(self, header_lines, rows, empty="-"):
        idx = header_lines
        for row in rows:
            idx += 1
            listed = [item.value for item in row if item.value is not None]
            ncols = len(row)
            msg = f"y={idx},cols={ncols}"
            if not listed:
                self._issues["warn"]["extra-lines"].append(msg)
                continue
            listed = [self.better(item.value) if item.value is not None else empty for item in row]
            self._rdict[idx] = listed


# Main script
if __name__ == "__main__":
    print("Import stocking.stockr !")
    main_test()
