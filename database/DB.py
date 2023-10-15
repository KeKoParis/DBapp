from sqlalchemy import Column, INTEGER, VARCHAR, Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

db = "mysql://root:0+8+1+0+2+0+0+3+@localhost/trafficpolice"

engine = create_engine(db, echo=True)

Session = sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class Passport(Base):
    __tablename__ = "tech_passport"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    passportNum = Column(VARCHAR(30))
    carNum = Column(VARCHAR(10))
    engineNum = Column(VARCHAR(15))
    colour = Column(VARCHAR(6))
    brand = Column(VARCHAR(15))


class Owner(Base):
    __tablename__ = "owner"
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    fullName = Column(VARCHAR(40))
    address = Column(VARCHAR(45))
    year = Column(INTEGER)
    sex = Column(Enum('male', 'female'))
    licence = Column(VARCHAR(20))
    passportID = Column(INTEGER)


with Session(autoflush=False, bind=engine) as db:
    curr_passport = Passport(passportNum="eaf5fe", carNum="a545", engineNum="are65", colour="efd5fa",
                             brand="Toyota")
    db.add(curr_passport)
    db.commit()

    curr_owner = Owner(fullName="Jim", address="Minsk", year="1975", sex="male", licence="jefowfksm5",
                       passportID="1")

    db.add(curr_owner)
    db.commit()
    print(curr_owner.id)
