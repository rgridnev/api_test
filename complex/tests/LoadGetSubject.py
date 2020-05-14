import datetime, csv
import apiclass as ac
import connectiondata as cd

def loadgetsubject():
    print('Запущен нагрузочный тест LoadGetSubject')
    timebeg = datetime.datetime.now()

    with open('testdata/test_users.csv', newline='') as file:
         test_users = csv.reader(file)
         isns = list(test_users)[0]
         print('Количество тестовых контрагентов:',  len(isns))
         print('Количество тестовых пользователей:', len(cd.users.keys()))
         for user in cd.users.keys():
             print(user)
             api = ac.apirequest(user)
             for isn in isns:
                 resp = api.getsubject(isn)

    timeend = datetime.datetime.now()

    print('Время, затраченное на тест:', timeend-timebeg)
    print('Среднее время исполнения запроса:', (timeend - timebeg)/(len(isns) * len(cd.users.keys())))