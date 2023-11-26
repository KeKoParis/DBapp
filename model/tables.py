from IPython.display import HTML

from database.getData import Get
from model.table_headers import owner_header, passports_header, inspection_header, inspector_header


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
