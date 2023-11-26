from sqlalchemy import Column, INTEGER, VARCHAR, Enum
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Passport(Base):
    __tablename__ = "tech_passport"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    ownerID = Column(INTEGER)
    passportNum = Column(VARCHAR(30))
    carNum = Column(VARCHAR(10))
    engineNum = Column(VARCHAR(20))
    colour = Column(VARCHAR(20))
    brand = Column(VARCHAR(15))


class Owner(Base):
    __tablename__ = "owner"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    fullName = Column(VARCHAR(40))
    address = Column(VARCHAR(45))
    year = Column(INTEGER)
    sex = Column(Enum('male', 'female'))
    licence = Column(VARCHAR(20))


class Inspector(Base):
    __tablename__ = "inspector"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    fullName = Column(VARCHAR(45))
    title = Column(VARCHAR(45))
    rank = Column(VARCHAR(45))


class Inspection(Base):
    __tablename__ = "inspection"
    id = Column(INTEGER, primary_key=True)
    passportID = Column(INTEGER)
    date = Column(INTEGER)
    inspectorID = Column(INTEGER)
    result = Column(Enum("+", "-"))
