from enum import Enum

from flask import Flask, render_template, request, redirect
from loguru import logger
from werkzeug.datastructures.structures import ImmutableMultiDict as imd

import model.delete
import model.insert
import model.update
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
        self.__pages__ = [0, 0, 0, 0]
        self.__date__ = -1
        self.__engine_num__ = ""

        self.__additional_tables_pages__ = [0, 0]
        self.__app__ = curr_app
        self.__addit_tables__ = list()
        self.__html_tables__ = list()
        self.__additional_tables__ = list()

        self.__table__ = Tables()

        logger.info('server is running')
        self.__run__()

    def __run__(self):
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

            self.__pages__ = [0, 0, 0, 0]
            self.__html_tables__.append(
                self.__table__.create_owner_list(self.__pages__[TEnum.owner.value])[0])
            self.__html_tables__.append(
                self.__table__.create_passport_list(self.__pages__[TEnum.passport.value])[0])
            self.__html_tables__.append(
                self.__table__.create_inspector_list(self.__pages__[TEnum.inspector.value])[0])
            self.__html_tables__.append(
                self.__table__.create_inspection_list(self.__pages__[TEnum.inspection.value])[0])

            logger.info('page formed success')
            return render_template('index.html', tables=self.__html_tables__, pages=self.__pages__)

        @self.__app__.route('/owner/next', methods=['POST'])
        def owner_next_page():
            curr_page = int(request.form['next'])

            res = self.__table__.create_owner_list(curr_page + 1)

            new_page = res[0]
            empty = res[1]

            if empty:
                self.__html_tables__[TEnum.owner.value] = new_page
                self.__pages__[TEnum.owner.value] += 1

            logger.info("owner next button ok")
            return redirect('/open/table/owner')

        @self.__app__.route('/owner/prev', methods=['POST'])
        def owner_prev_page():
            curr_page = int(request.form['prev'])

            if curr_page != 0:
                res = self.__table__.create_owner_list(curr_page - 1)
                new_page = res[0]
                empty = res[1]

                if empty:
                    self.__html_tables__[TEnum.owner.value] = new_page
                    self.__pages__[TEnum.owner.value] -= 1

            logger.info("owner prev button ok")
            return redirect('/open/table/owner')

        @self.__app__.route('/passport/next', methods=['POST'])
        def passport_next_page():
            curr_page = int(request.form['next'])

            res = self.__table__.create_passport_list(curr_page + 1)

            new_page = res[0]
            empty = res[1]

            if empty:
                self.__html_tables__[TEnum.passport.value] = new_page
                self.__pages__[TEnum.passport.value] += 1

            logger.info("passport next button ok")
            return redirect('/open/table/passport')

        @self.__app__.route('/passport/prev', methods=['POST'])
        def passport_prev_page():
            curr_page = int(request.form['prev'])

            if curr_page != 0:
                res = self.__table__.create_passport_list(curr_page - 1)
                new_page = res[0]
                empty = res[1]

                if empty:
                    self.__html_tables__[TEnum.passport.value] = new_page
                    self.__pages__[TEnum.passport.value] -= 1

            logger.info("passport prev button ok")
            return redirect('/open/table/passport')

        @self.__app__.route('/inspector/next', methods=['POST'])
        def inspector_next_page():
            curr_page = int(request.form['next'])

            res = self.__table__.create_inspector_list(curr_page + 1)

            new_page = res[0]
            empty = res[1]

            if empty:
                self.__html_tables__[TEnum.inspector.value] = new_page
                self.__pages__[TEnum.inspector.value] += 1

            logger.info("inspector next button ok")
            return redirect('/open/table/inspector')

        @self.__app__.route('/inspector/prev', methods=['POST'])
        def inspector_prev_page():
            curr_page = int(request.form['prev'])

            if curr_page != 0:
                res = self.__table__.create_inspector_list(curr_page - 1)
                new_page = res[0]
                empty = res[1]

                if empty:
                    self.__html_tables__[TEnum.inspector.value] = new_page
                    self.__pages__[TEnum.inspector.value] -= 1

            logger.info("inspector prev button ok")
            return redirect('/open/table/inspector')

        @self.__app__.route('/inspection/next', methods=['POST'])
        def inspection_next_page():
            curr_page = int(request.form['next'])

            res = self.__table__.create_inspection_list(curr_page + 1)

            new_page = res[0]
            empty = res[1]

            if empty:
                self.__html_tables__[TEnum.inspection.value] = new_page
                self.__pages__[TEnum.inspection.value] += 1

            logger.info("inspection next button ok")
            return redirect('/open/table/inspection')

        @self.__app__.route('/inspection/prev', methods=['POST'])
        def inspection_prev_page():
            curr_page = int(request.form['prev'])

            if curr_page != 0:
                res = self.__table__.create_inspection_list(curr_page - 1)
                new_page = res[0]
                empty = res[1]

                if empty:
                    self.__html_tables__[TEnum.inspection.value] = new_page
                    self.__pages__[TEnum.inspection.value] -= 1

            logger.info("inspection prev button ok")
            return redirect('/open/table/inspection')

        @self.__app__.route('/delete_owner', methods=['POST'])
        def del_owner():
            owner_id = int(request.form['id'])
            model.delete.delete(TEnum.owner.value, owner_id)
            return redirect('/')

        @self.__app__.route('/delete_passport', methods=['POST'])
        def del_passport():
            owner_id = int(request.form['id'])
            model.delete.delete(TEnum.passport.value, owner_id)
            return redirect('/')

        @self.__app__.route('/delete_inspector', methods=['POST'])
        def del_inspector():
            owner_id = int(request.form['id'])
            model.delete.delete(TEnum.inspector.value, owner_id)
            return redirect('/')

        @self.__app__.route('/delete_inspection', methods=['POST'])
        def del_inspection():
            owner_id = int(request.form['id'])
            model.delete.delete(TEnum.inspection.value, owner_id)
            return redirect('/')

        @self.__app__.route('/insert_owner', methods=['POST'])
        def insert_owner():
            raw_fields = request.form
            fields = imd.to_dict(raw_fields)
            model.insert.insert(TEnum.owner.value, fields)

            return redirect('/')

        @self.__app__.route('/change_owner', methods=['POST'])
        def update_owner():
            raw_fields = request.form
            fields = imd.to_dict(raw_fields)
            print(fields)
            model.update.update(TEnum.owner.value, fields)

            return redirect('/')

        @self.__app__.route('/change_passport', methods=['POST'])
        def update_passport():
            raw_fields = request.form
            fields = imd.to_dict(raw_fields)
            print(fields)
            model.update.update(TEnum.owner.value, fields)

            return redirect('/')

        @self.__app__.route('/change_inspector', methods=['POST'])
        def update_inspector():
            raw_fields = request.form
            fields = imd.to_dict(raw_fields)
            print(fields)
            model.update.update(TEnum.owner.value, fields)

            return redirect('/')

        @self.__app__.route('/change_inspection', methods=['POST'])
        def update_inspection():
            raw_fields = request.form
            fields = imd.to_dict(raw_fields)
            print(fields)
            model.update.update(TEnum.owner.value, fields)

            return redirect('/')

        @self.__app__.route('/add_inspection', methods=['POST'])
        def insert_inspection():
            raw_fields = request.form
            fields = imd.to_dict(raw_fields)
            model.insert.insert(TEnum.owner.value, fields)

            return redirect('/')

        @self.__app__.route('/add_inspector', methods=['POST'])
        def insert_inspector():
            raw_fields = request.form
            fields = imd.to_dict(raw_fields)
            model.insert.insert(TEnum.owner.value, fields)

            return redirect('/')

        @self.__app__.route('/add_passport', methods=['POST'])
        def insert_passport():
            raw_fields = request.form
            fields = imd.to_dict(raw_fields)
            model.insert.insert(TEnum.owner.value, fields)

            return redirect('/')

        @self.__app__.route('/open/table/owner', methods=['POST'])
        def open_owner_table():
            return render_template('owner/owner_table.html', tables=self.__html_tables__, pages=self.__pages__)

        @self.__app__.route('/open/table/owner')
        def render_owner():
            return render_template('owner/owner_table.html', tables=self.__html_tables__, pages=self.__pages__)

        @self.__app__.route('/open/table/passport', methods=['POST'])
        def open_passport_table():
            return render_template('passport/passport_table.html', tables=self.__html_tables__, pages=self.__pages__)

        @self.__app__.route('/open/table/passport')
        def render_passport():
            return render_template('passport/passport_table.html', tables=self.__html_tables__, pages=self.__pages__)

        @self.__app__.route('/open/table/inspector', methods=['POST'])
        def open_inspector_table():
            return render_template('inspector/inspector_table.html', tables=self.__html_tables__, pages=self.__pages__)

        @self.__app__.route('/open/table/inspector')
        def render_inspector():
            return render_template('inspector/inspector_table.html', tables=self.__html_tables__, pages=self.__pages__)

        @self.__app__.route('/open/table/inspection', methods=['POST'])
        def open_inspection_table():
            return render_template('inspection/inspection_table.html', tables=self.__html_tables__,
                                   pages=self.__pages__)

        @self.__app__.route('/open/table/inspection')
        def render_inspection():
            return render_template('inspection/inspection_table.html', tables=self.__html_tables__,
                                   pages=self.__pages__)

        @self.__app__.route('/render/main', methods=['POST'])
        def render_main():
            return redirect('/')

        @self.__app__.route('/owner/crud', methods=['POST'])
        def owner_crud():
            return render_template('owner/owner_crud.html')

        @self.__app__.route('/passport/crud', methods=['POST'])
        def passport_crud():
            return render_template('passport/passport_crud.html')

        @self.__app__.route('/inspector/crud', methods=['POST'])
        def inspector_crud():
            return render_template('inspector/inspector_crud.html')

        @self.__app__.route('/inspection/crud', methods=['POST'])
        def inspection_crud():
            return render_template('inspection/inspection_crud.html')

        @self.__app__.route('/additional_tables', methods=['POST'])
        def additional_tables():
            self.__addit_tables__ = self.__table__.create_additional_list(self.__additional_tables_pages__[0],
                                                                          self.__additional_tables_pages__[1], 0, '0')
            return render_template('additional_tables.html', additional_tables=self.__addit_tables__[0],
                                   pages=self.__additional_tables_pages__)

        @self.__app__.route('/get_additional_tables', methods=['POST'])
        def get_additional_tables():
            engine_num = request.form['engine']
            date = request.form['date']
            date = date.replace("-", "")
            if date == "":
                date = '0'
            self.__date__ = date
            self.__engine_num__ = engine_num

            self.__addit_tables__ = self.__table__.create_additional_list(self.__additional_tables_pages__[0],
                                                                          self.__additional_tables_pages__[1],
                                                                          int(date),
                                                                          str(engine_num))

            return render_template('additional_tables.html', additional_tables=self.__addit_tables__[0],
                                   pages=self.__additional_tables_pages__)

        @self.__app__.route('/additional_tables_rend')
        def just_addit_tables():
            return render_template('additional_tables.html', additional_tables=self.__addit_tables__[0],
                                   pages=self.__additional_tables_pages__)

        @self.__app__.route('/car_addit/next', methods=['POST'])
        def inspector_addit_next_page():
            curr_page = int(request.form['next'])

            res = self.__table__.create_additional_list(curr_page + 1,
                                                        self.__additional_tables_pages__[1],
                                                        self.__date__,
                                                        self.__engine_num__)

            new_page = res[0]
            empty = res[1]

            if empty:
                self.__additional_tables__ = new_page
                self.__additional_tables_pages__[0] += 1

            logger.info("additional table next button ok")
            return redirect('/additional_tables_rend')

        @self.__app__.route('/car_addit/prev', methods=['POST'])
        def inspector_addit_prev_page():
            curr_page = int(request.form['prev'])

            if curr_page != 0:
                res = self.__table__.create_additional_list(curr_page - 1,
                                                            self.__additional_tables_pages__[1],
                                                            self.__date__,
                                                            self.__engine_num__)
                new_page = res[0]
                empty = res[2]

                if empty:
                    self.__additional_tables__ = new_page
                    self.__additional_tables_pages__[0] -= 1

            logger.info("additional table prev button ok")
            return redirect('/additional_tables_rend')

        @self.__app__.route('/engine/next', methods=['POST'])
        def car_addit_next_page():
            curr_page = int(request.form['next'])

            res = self.__table__.create_additional_list(self.__additional_tables_pages__[1],
                                                        curr_page + 1,
                                                        self.__date__,
                                                        self.__engine_num__)

            new_page = res[0]
            empty = res[2]

            if empty:
                self.__additional_tables__ = new_page
                self.__additional_tables_pages__[1] += 1

            logger.info("additional table next button ok")
            return redirect('/additional_tables_rend')

        @self.__app__.route('/engine/prev', methods=['POST'])
        def car_addit_prev_page():
            curr_page = int(request.form['prev'])

            if curr_page != 0:
                res = self.__table__.create_additional_list(self.__additional_tables_pages__[0],
                                                            curr_page - 1,
                                                            self.__date__,
                                                            self.__engine_num__)
                new_page = res[0]
                empty = res[2]

                if empty:
                    self.__additional_tables__ = new_page
                    self.__additional_tables_pages__[1] -= 1

            logger.info("additional table prev button ok")
            return redirect('/additional_tables_rend')

        @self.__app__.route('/inspections_by_date', methods=['POST'])
        def inspections_by_date():
            return render_template('car_num_period/car_num_period.html')

        @self.__app__.route('/get_inspections_by_date', methods=['POST'])
        def get_inspections_by_date():
            first_date = request.form['first_date']
            second_date = request.form['second_date']
            first_date = first_date.replace("-", "")
            second_date = second_date.replace("-", "")

            if first_date == "" or second_date == "":
                return redirect("/inspections_by_date")

            table = self.__table__.create_get_car_period(int(first_date), int(second_date))

            return render_template('car_num_period/car_num_period.html', table=table)


if __name__ == '__main__':
    app = Flask(__name__)
    temp = Templates(app)
    app.run('0.0.0.0', 7000, debug=True)
