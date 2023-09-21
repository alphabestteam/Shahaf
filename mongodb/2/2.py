import pymongo

def main():
    connection = 'mongodb://localhost:32768/'
    client = pymongo.MongoClient(connection)

    database = client["Aviv's_people"]

    collection_1 = database['family']
    family = [{'name': 'mother', 'age': 45, 'occupation': 'teacher'},
              {'name': 'father', 'age': 46, 'occupation': 'engineer'},
              {'name': 'brother', 'age': 12, 'occupation': 'school'},
              {'name': 'sister', 'age': 24, 'occupation': 'student'}]
    my_family = collection_1.insert_many(family)

    for member in collection_1.find():
        print(member)

    collection_2 = database['friends']
    friends = [{'name': 'Amit', 'age': 20, 'occupation': 'waiter', '_id': '11'},
              {'name': 'Yonatan', 'age': 24, 'occupation': 'student', '_id': '22'},
              {'name': 'Noa', 'age': 22, 'occupation': 'student', '_id': '33'},
              {'name': 'Michal', 'age': 21, 'occupation': 'baker', '_id': '44'}]
    my_friends = collection_2.insert_many(friends)

    for member in collection_2.find():
        print(member)

    collection_3 = database['army']
    aviv = {'name': 'Aviv', 'age': 20, 'occupation': 'backend'}
    lihi = {'name': 'Lihi', 'age': 21, 'occupation': 'QA'}
    gabi = {'name': 'Gabi', 'age': 22, 'occupation': 'DevOps'}
    ori = {'name': 'Ori', 'age': 23, 'occupation': 'front-end'}
    ido = {'name': 'Ido', 'age': 22, 'occupation': 'developer'}
    yarden = {'name': 'Yarden', 'age': 24, 'occupation': 'Devops'}

    army1 = collection_3.insert_one(aviv)
    army2 = collection_3.insert_one(lihi)
    army3 = collection_3.insert_one(gabi)
    army4 = collection_3.insert_one(ori)
    army5 = collection_3.insert_one(ido)
    army6 = collection_3.insert_one(yarden)

    for member in collection_3.find():
        print(member)

    original_michal = { 'name': 'Michal', 'age': 21, 'occupation': 'baker', '_id': '44' }
    collection_2.delete_one(original_michal)
    

if __name__ == "__main__":
    main()