"""Utility functions for wrangling data."""

__author__ = "730163234"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    
    for row in csv_reader:
        rows.append(row)

    file_handle.close()
    return rows


def column_values(rows: list[dict[str, str]], key: str) -> list[str]:
    """Creates empty list to append column values to, returns list of column values."""
    values: list[str] = []

    for row in rows:
        values.append(row[key])

    return values


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transposes columns into rows to create a dictionary of columns instead of a list of rows."""
    columns: dict[str, list[str]] = {}
    values: list[str] = []

    names = rows[0]
    for name in names:
        values = column_values(rows, name)
        columns[name] = values

    return columns


def head(table: dict[str, list[str]], rowsnum: int) -> dict[str, list[str]]:
    """Appends first five rows of our dataset into an empty dictionary."""
    result: dict[str, list[str]] = {}

    for col in table:
        headList: list[str] = []
        if rowsnum >= len(table[col]):
            rowsnum = len(table[col])
           
        for n in range(rowsnum):
            headList.append(table[col][n])
        result[col] = headList

    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Selects desired columns and appends to a new dictionary."""
    result: dict[str, list[str]] = {}

    for name in names:
        result[name] = table[name]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Provides categorical frequency counts of observations."""
    counts: dict[str, int] = {}

    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts