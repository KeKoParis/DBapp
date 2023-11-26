from enum import Enum

from flask import Flask, render_template, request, redirect
from loguru import logger

from model.tables import Tables

# logger.remove()
logger.add('program.log', format='{time} {level} {message}', level='INFO')


class TEnum(Enum):
    """
    Table enum
    """
    owner = 0
    passport = 1
    inspector = 2
    inspection = 3


class Templates:

    def __init__(self, curr_app):
        self.__pages__ = [0, 0, 0, 0]
        self.__app__ = curr_app
        self.__html_tables__ = list()
        self.__table__ = Tables()

        logger.info('server is running')
        self.run()

    def run(self):
        @self.__app__.route('/')
        def main_page():
            """
            Displays tables, buttons, pages. Order of the tables:
                0. Owner
                1. Passport
                2. Inspector
                3. Inspection
            :return: render_template
            """

            if len(self.__html_tables__) == 0:
                self.__html_tables__.append(
                    self.__table__.create_owner_list(self.__pages__[TEnum.owner.value])[0])
                self.__html_tables__.append(
                    self.__table__.create_passport_list(self.__pages__[TEnum.passport.value])[0])
                self.__html_tables__.append(
                    self.__table__.create_inspector_list(self.__pages__[TEnum.inspector.value])[0])
                self.__html_tables__.append(
                    self.__table__.create_inspection_list(self.__pages__[TEnum.inspection.value])[0])

            logger.info('main_page success')
            return render_template('main.html', tables=self.__html_tables__, pages=self.__pages__)

        @self.__app__.route('/owner/next', methods=['POST'])
        def owner_next_page():
            curr_page = int(request.form['next'])

            res = self.__table__.create_owner_list(curr_page + 1)
            new_page = res[0]
            empty = res[1]

            if empty:
                self.__html_tables__[TEnum.owner.value] = new_page
                self.__pages__[TEnum.owner.value] += 1

            return redirect('/')


if __name__ == '__main__':
    app = Flask(__name__)
    temp = Templates(app)
    app.run('0.0.0.0', 7000, debug=True)
