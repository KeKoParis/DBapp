from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


class Get:
    def __init__(self):
        self.__db__ = "mysql://root:0+8+1+0+2+0+0+3+@localhost/trafficpolice"
        self.__engine__ = create_engine(self.__db__, echo=True)
        self.__Session__ = sessionmaker(autoflush=False, bind=self.__engine__)

    def get_inspector_on_date(self, date: int):
        query = text("""select * from getinspectiondate where date = :date""")
        with self.__engine__.connect() as connect:
            result = connect.execute(query, date=date)

        return result

    def get_car_inspections(self, engine_num: str):
        query = text("""select * from getcardata where engineNum = :engineNum""")
        with self.__engine__.connect() as connect:
            result = connect.execute(query, engineNum=engine_num)

        return result

    def get_inspectors(self, page: int):
        pass

    def get_passports(self, page):
        pass

    def get_owners(self, page):
        pass

    def get_inspections(self, page):
        pass