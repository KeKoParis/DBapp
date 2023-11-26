from database.DB import *


def insert(dataclass: int, data: dict):
    db = DataBase()
    if dataclass == 0:
        obj = Owner(id=data[0], fullName=data[1], address=data[2], year=data[3], sex=data[4],
                    license=data[5])
        db.insert(obj)
    if dataclass == 1:
        obj = Owner(id=data[0], ownerID=data[1], passportNum=data[2], carNum=data[3],
                    engineNum=data[4], colour=data[5], beand=data[6])
        db.insert(obj)
    if dataclass == 2:
        obj = Owner(id=data[0], fullName=data[1], title=data[2], rank=data[3])
        db.insert(obj)
    if dataclass == 3:
        obj = Owner(id=data[0], passportID=data[1], date=data[2], inspectorID=data[3],
                    result=data[4])
        db.insert(obj)
