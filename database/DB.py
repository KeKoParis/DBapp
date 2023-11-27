from loguru import logger
from sqlalchemy import create_engine, text, bindparam, INTEGER
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from dataClasses.dataClasses import Base, Owner, Passport, Inspector, Inspection


class DataBase:

    def __init__(self):
        self.__db__ = "mysql://root:0+8+1+0+2+0+0+3+@localhost/trafficpolice"
        self.__engine__ = create_engine(self.__db__, echo=True)
        self.__Session__ = sessionmaker(autoflush=False, bind=self.__engine__)

    def get_obj(self, table: str, stmt_id: int):
        query = text(f'select * from {table} where id = :id')
        query = query.bindparams(bindparam("id", type_=INTEGER))
        try:
            with self.__engine__.connect() as connect:
                result = connect.execute(query, {"id": stmt_id})

            return result.fetchall()
        except SQLAlchemyError as err:
            logger.info(err)
            return None

    def insert(self, data_class: Base):
        with self.__Session__(bind=self.__engine__, expire_on_commit=True) as db:
            try:
                db.add(data_class)
                db.commit()
            except SQLAlchemyError as err:
                logger.info(err)

    def delete(self, data_class: Base):
        with self.__Session__(bind=self.__engine__, expire_on_commit=True) as db:
            try:
                instance = db.merge(data_class)
                db.delete(instance)
                db.commit()
            except SQLAlchemyError as err:
                logger.info(err)

    def update(self, data_class: Base):
        pass


class DataBaseOwner(DataBase):
    def update(self, data_class: Owner):
        print("dataclass ", data_class.id)
        with self.__Session__(bind=self.__engine__, expire_on_commit=True) as db:
            try:
                db.query(Owner).filter(Owner.id == data_class.id).update({
                    "fullName": data_class.fullName,
                    "address": data_class.address,
                    "license": data_class.license,
                    "sex": data_class.sex,
                    "year": data_class.year
                })
                db.commit()
            except SQLAlchemyError as err:
                logger.info(err)


class DataBasePassport(DataBase):
    def update(self, data_class: Passport):
        with self.__Session__(bind=self.__engine__, expire_on_commit=True) as db:
            try:
                db.query(Passport).filter(Passport.id == data_class.id).update({
                    "ownerID": data_class.ownerID,
                    "passportNum": data_class.passportNum,
                    "carNum": data_class.carNum,
                    "engineNum": data_class.engineNum,
                    "colour": data_class.colour,
                    "brand": data_class.brand
                })
                db.commit()
            except SQLAlchemyError as err:
                logger.info(err)


class DataBaseInspector(DataBase):
    def update(self, data_class: Inspector):
        with self.__Session__(bind=self.__engine__, expire_on_commit=True) as db:
            try:
                db.query(Inspector).filter(Inspector.id == data_class.id).update({
                    "fullName": data_class.fullName,
                    "title": data_class.title,
                    "rank": data_class.rank
                })
                db.commit()
            except SQLAlchemyError as err:
                logger.info(err)


class DataBaseInspection(DataBase):
    def update(self, data_class: Inspection):
        with self.__Session__(bind=self.__engine__, expire_on_commit=True) as db:
            try:
                db.query(Inspection).filter(Inspection.id == data_class.id).update({
                    "passportID": data_class.passportID,
                    "date": data_class.date,
                    "inspectorID": data_class.inspectorID,
                    "result": data_class.result
                })
                db.commit()
            except SQLAlchemyError as err:
                logger.info(err)
