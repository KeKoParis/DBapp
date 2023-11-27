from loguru import logger
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker


class Get:
    def __init__(self):
        self.__db__ = "mysql://root:0+8+1+0+2+0+0+3+@localhost/trafficpolice"
        self.__engine__ = create_engine(self.__db__, echo=True)
        self.__Session__ = sessionmaker(autoflush=False, bind=self.__engine__)

    def get_inspector_on_date(self, date: int, page: int):
        query = text("""
                    select * from getinspectiondate
                    where date = :date 
                    limit 10 offset : pages
                    """)

        try:
            with self.__engine__.connect() as connect:
                result = connect.execute(query, {"date": date, "pages": page * 10})

            return result.fetchall()
        except SQLAlchemyError as err:
            logger.info(err)
            return None

    def get_car_inspections(self, engine_num: str, page: int):
        query = text("""
                    select * from getcardata 
                    where engineNum = :engineNum
                    limit 10 offset :pages
                    """)
        try:
            with self.__engine__.connect() as connect:
                result = connect.execute(query, {"engineNum": engine_num, "pages": page * 10})

            return result.fetchall()
        except SQLAlchemyError as err:
            logger.info(err)
            return None

    def get_inspectors(self, page: int):
        query = text("""
                select * from inspector
                limit 10 offset :pages
                """)

        try:
            with self.__engine__.connect() as connect:
                result = connect.execute(query, {"pages": page * 10})

            return result.fetchall()
        except SQLAlchemyError as err:
            logger.info(err)
            return None

    def get_passports(self, page):
        query = text("""
                select * from tech_passport
                limit 10 offset :pages
                """)

        try:
            with self.__engine__.connect() as connect:
                result = connect.execute(query, {"pages": page * 10})

            return result.fetchall()
        except SQLAlchemyError as err:
            logger.info(err)
            return None

    def get_owners(self, page):
        query = text("""
                select * from owner
                limit 10 offset :pages
                """)

        try:
            with self.__engine__.connect() as connect:
                result = connect.execute(query, {"pages": page * 10})

            return result.fetchall()
        except SQLAlchemyError as err:
            logger.info(err)
            return None

    def get_inspections(self, page):
        query = text("""
                select * from inspection
                limit 10 offset :pages
                """)

        try:
            with self.__engine__.connect() as connect:
                result = connect.execute(query, {"pages": page * 10})

            return result.fetchall()
        except SQLAlchemyError as err:
            logger.info(err)
            return None

    def get_additional_tables(self):

        query = text("""
        select * from getcardata
        limit 10 offset :pages
        """)