from database import getData

a = getData.Get()
for i in a.get_owners(3):
    print(i)
