from database.DB import *


def __new_data__(tup: tuple, dict2: dict):
    """
    tup is prev data, dict2 new data
    :param tup:
    :param dict2:
    :return: dict
    """
    keys = dict2.keys()
    print(dict2)
    j = 0
    for i in keys:
        if dict2[i] == "":
            dict2[i] = tup[j]
        j += 1
    print(dict2)
    return dict2


def update(dataclass: int, data: dict):
    if dataclass == 0:
        db = DataBaseOwner()
        obj_data = db.get_obj("owner", data['id'])[0]

        data = __new_data__(obj_data, data)

        obj = Owner(id=int(data['id']), fullName=data['fullName'], address=data['address'], year=int(data['year']),
                    sex=data['sex'], license=data['license'])
        print(obj.id)
        db.update(obj)
    if dataclass == 1:
        db = DataBasePassport()
        obj_data = db.get_obj("tech_passport", data['id'])[0]

        data = __new_data__(obj_data, data)

        obj = Passport(id=data['id'], ownerID=data['ownerID'], passportNum=data['passportNum'], carNum=data['carNum'],
                       engineNum=data['engineNum'], colour=data['colour'], brand=data['brand'])

        db.update(obj)
    if dataclass == 2:
        db = DataBaseInspector()
        obj_data = db.get_obj("inspector", data['id'])[0]

        data = __new_data__(obj_data, data)

        obj = Inspector(id=data['id'], fullName=data['fullName'], title=data['title'], rank=data['rank'])
        db.insert(obj)
    if dataclass == 3:
        db = DataBaseInspection()
        obj_data = db.get_obj("inspection", data['id'])[0]

        data = __new_data__(obj_data, data)

        obj = Inspection(id=data['id'], passportID=data['passportID'], date=data['date'],
                         inspectorID=data['inspectorID'], result=data['result'])

        db.update(obj)
