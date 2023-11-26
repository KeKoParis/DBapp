from database.DB import *


def delete(dataclass: int, stmt_id: int):
    db = DataBase()
    if dataclass == 0:
        obj_data = db.get_obj("owner", stmt_id)[0]
        obj = Owner(id=obj_data[0], fullName=obj_data[1], address=obj_data[2], year=obj_data[3], sex=obj_data[4],
                    licence=obj_data[5])
        db.delete(obj)
    if dataclass == 1:
        obj_data = db.get_obj("tech_passport", stmt_id)
        obj = Owner(id=obj_data[0], ownerID=obj_data[1], passportNum=obj_data[2], carNum=obj_data[3],
                    engineNum=obj_data[4], colour=obj_data[5], beand=obj_data[6])
        db.delete(obj)
    if dataclass == 2:
        obj_data = db.get_obj("inspector", stmt_id)
        obj = Owner(id=obj_data[0], fullName=obj_data[1], title=obj_data[2], rank=obj_data[3])
        db.delete(obj)
    if dataclass == 3:
        obj_data = db.get_obj("inspection", stmt_id)
        obj = Owner(id=obj_data[0], passportID=obj_data[1], date=obj_data[2], inspectorID=obj_data[3],
                    result=obj_data[4])
        db.delete(obj)
