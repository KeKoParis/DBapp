from IPython.display import HTML

from database.getData import Get
from model.table_headers import *


class Tables:

    def __init__(self):
        self.__get_obj__ = Get()

    @staticmethod
    def __wrap__(elements: list, html_table: str):
        for i in elements:
            html_table += "<tr>"
            for j in range(len(i)):
                html_table += "<td>" + str(i[j]) + "</td>"

            html_table += "</tr>"
        html_table = "<table>" + html_table + "</table>"

        return HTML(html_table)

    def create_owner_list(self, page: int):
        html_table = owner_header

        elements = self.__get_obj__.get_owners(page)

        html_table = self.__wrap__(elements, html_table)

        empty = True
        if len(elements) == 0:
            empty = False

        return html_table, empty

    def create_passport_list(self, page: int):
        html_table = passports_header

        elements = self.__get_obj__.get_passports(page)

        html_table = self.__wrap__(elements, html_table)

        empty = True
        if len(elements) == 0:
            empty = False

        return html_table, empty

    def create_inspector_list(self, page: int):
        html_table = inspector_header

        elements = self.__get_obj__.get_inspectors(page)

        html_table = self.__wrap__(elements, html_table)

        empty = True
        if len(elements) == 0:
            empty = False

        return html_table, empty

    def create_inspection_list(self, page: int):
        html_table = inspection_header

        elements = self.__get_obj__.get_inspections(page)

        html_table = self.__wrap__(elements, html_table)

        empty = True
        if len(elements) == 0:
            empty = False

        return html_table, empty

    def create_additional_list(self, getcardata_page: int, getinspectiondate_page: int, date: int, engine_num: str):
        additional_tables = self.__get_obj__.get_additional_tables(getcardata_page, getinspectiondate_page, date,
                                                                   engine_num)
        html_getcardata_table = get_inspection_date_header
        html_getinspectiondate_table = get_car_data_header

        result = list()

        page1: bool
        page2: bool

        if additional_tables is None:
            result.append(HTML("<h2>Get car data<h2>"))
            result.append(HTML("<h2>Get car data<h2>"))
            return result, False, False

        if not (additional_tables[0] is None):
            getcardata_table = additional_tables[0]
            html_getcardata_table = self.__wrap__(getcardata_table, html_getcardata_table)
            page1 = True
        else:
            html_getcardata_table = self.__wrap__([], html_getcardata_table)
            page1 = False

        if not (additional_tables[1] is None):
            getinspectiondate_table = additional_tables[1]
            html_getinspectiondate_table = self.__wrap__(getinspectiondate_table, html_getinspectiondate_table)
            page2 = True
        else:
            html_getinspectiondate_table = self.__wrap__([], html_getinspectiondate_table)
            page2 = False

        result.append(HTML("<h2>Get car data<h2>"))
        result.append(html_getcardata_table)
        result.append(HTML("<h2>Get car data<h2>"))
        result.append(html_getinspectiondate_table)

        return result, page1, page2

    def create_get_car_period(self, first_date: int, second_date: int):
        html_table = create_get_car_period

        elements = self.__get_obj__.get_car_period(first_date, second_date)

        html_table = self.__wrap__(elements, html_table)

        return html_table
