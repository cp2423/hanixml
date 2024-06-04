import openpyxl
import os

STUDENT_IDS_FILENAME = "students.xlsx"


def get_workbook():
    if os.path.isfile(STUDENT_IDS_FILENAME):
        return openpyxl.load_workbook(filename=STUDENT_IDS_FILENAME)
    else:
        raise FileNotFoundError(STUDENT_IDS_FILENAME)


def get_student_ids():
    book = get_workbook()
    sheet = book.active
    return [row[0] for row in sheet.iter_rows(values_only=True)]
