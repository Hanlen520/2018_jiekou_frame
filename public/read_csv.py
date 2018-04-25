import os,io,csv
import xlrd

def _load_csv_file(csv_file):
    """ load csv file and check file content format
       @param
           csv_file: csv file path
           e.g. csv file content:
               username,password
               test1,111111
               test2,222222
               test3,333333
       @return
           list of parameter, each parameter is in dict format
           e.g.
           [
               {'username': 'test1', 'password': '111111'},
               {'username': 'test2', 'password': '222222'},
               {'username': 'test3', 'password': '333333'}
           ]
       """
    csv_content_list = []

    with io.open(csv_file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_content_list.append(row)

    return csv_content_list


def get_csv_data(csv_file):
    value_rows = []
    with open(csv_file, encoding='utf-8') as f:
        f_csv = csv.reader(f)
        next(f_csv)
        for r in f_csv:
            value_rows.append(r)

    return value_rows

def get_excel_data(excel_file):
    value_rows = []
    with open(excel_file, encoding='utf-8') as f:
        f_excel = xlrd.reader(f)
        next(f_excel)
        for r in f_excel:
            value_rows.append(r)

    return value_rows