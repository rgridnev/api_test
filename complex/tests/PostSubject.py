import datetime
import apiclass as ac

def NewSubject():
    Subject = {
                "lastname": "Тестовый", # фамилию не меняем, так как она используется в тесте на дубли е-ё-симв,
                "firstname": "ААРТуррр",
                "parentname": "Тестович",
                "sex": "М",
                "birthday": "1983-05-24T00:00:00",
                "latinname": "Gridnev Roman",
                "drivingdatebeg": "2004-01-01T00:00:00",
                "citizenship": "RUS",
                "address": [
                    {
                        "code": 2247,
                        "code_desc": "Фактический",
                        "text": "Московская обл, Мытищи г, Воровского ул, д. 5 кв 21",
                        "street_kladr_id": "50000044000005900"
                    },
                                        {
                        "code": 2246,
                        "code_desc": "Регистрация",
                        "text": "Москва, Красная площадь, 1 кв157",
                        #"street_kladr_id": "50000044000005900"
                    }
                ],
                "contact": [
                    {
                        "code": 2243,
                        "code_desc": "E-mail личный",
                        "text": "test@ya.ru"
                    },
                                    {
                        "code": 2240,
                        "text": "+7(926) 449-48-60"
                     },

                ],
                "document": [

                    {
                        "code": 1165,
                        "code_desc": "Паспорт гражданина России",
                         "series": "1111",
                         "number": "111111",
                        "issue_date": "2003-08-12T00:00:00",
                        "issue_by": "ОВД ОВД ОВД"
                    },
                    {
                    "code": 1145,
                    "code_desc": "Водительское удостоверение",
                    "series": "50ОТ",
                    "number": "432259",
                    "issue_date": "2018-01-25T00:00:00",
                    "issue_by": "ГИБДД"
                    }
               ]
            }
    return Subject

def postsubjecttest(user, details=False):
    mainresult = []
    print('Запускаем тест создания новых пользователей')
    api = ac.apirequest(user)
    timebeg = datetime.datetime.now()

    def writeresult(resp, created_subjisn, test_result):
        result = {'case': case,
                            'timeelapsed': resp[1],
                            'resp_html_code': resp[0],
                            'resp_status_code': resp[2]['status']['code'],
                            'resp_status_error': resp[2]['status']['message'],
                            'created_subjisn': created_subjisn,
                            'test_result': test_result
                           }
        mainresult.append(test_result)
        if details == True:
            print (result)




    case = 'Минимальный набор данных'
    if details == True:
        print (case)
    testsubject = NewSubject()
    del testsubject['parentname']
    del testsubject['sex']
    del testsubject['latinname']
    del testsubject['drivingdatebeg']
    del testsubject['citizenship']
    del testsubject['address']
    del testsubject['contact']
    del testsubject['document']
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None:
        created_subjisn = None
        test_result = 'Fail'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        test_result = 'Ok'

    writeresult(resp, created_subjisn, test_result)

    case = 'Два паспорта'
    if details == True:
        print (case)
    testsubject = NewSubject()
    testsubject['document'] = testsubject['document']*2
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
        created_subjisn = None
        test_result = 'Ok'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        test_result = 'Fail'

    writeresult(resp, created_subjisn, test_result)

    case = 'Два адреса'
    if details == True:
        print (case)
    testsubject = NewSubject()
    testsubject['address'] = testsubject['address']*2
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
        created_subjisn = None
        test_result = 'Ok'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        test_result = 'Fail'

    writeresult(resp, created_subjisn, test_result)

    case = 'Документы из прошлого'
    if details == True:
        print (case)
    testsubject = NewSubject()
    testsubject['document'][0]['issue_date'] = "1883-05-24"
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
        created_subjisn = None
        test_result = 'Ok'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        test_result = 'Fail'
    writeresult(resp, created_subjisn, test_result)

    case = 'Документы из будущего'
    if details == True:
        print (case)
    testsubject = NewSubject()
    testsubject['document'][0]['issue_date'] = "2883-05-24"
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
        created_subjisn = None
        test_result = 'Ok'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        test_result = 'Fail'
    writeresult(resp, created_subjisn, test_result)

    case = 'Паспорт выдан до 14 лет'
    if details == True:
        print (case)
    testsubject = NewSubject()
    testsubject['document'][0]['issue_date'] = "1984-05-24"
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
        created_subjisn = None
        test_result = 'Ok'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        test_result = 'Fail'
    writeresult(resp, created_subjisn, test_result)

    case = 'Телефон не нужного формата'
    if details == True:
        print (case)
    testsubject = NewSubject()
    testsubject['contact'][1]['text'] = "1984-05-24"
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
        created_subjisn = None
        test_result = 'Ok'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        test_result = 'Fail'
    writeresult(resp, created_subjisn, test_result)

    case = 'Паспорт без серии и номера'
    if details == True:
        print (case)
    testsubject = NewSubject()
    del testsubject['document'][0]['series']
    del testsubject['document'][0]['number']
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
        created_subjisn = None
        test_result = 'Ok'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        test_result = 'Fail'
    writeresult(resp, created_subjisn, test_result)

    case = 'Паспорт только серия и номер'
    if details == True:
        print (case)
    testsubject = NewSubject()
    del testsubject['document'][0]['code_desc']
    del testsubject['document'][0]['issue_date']
    del testsubject['document'][0]['issue_by']
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
        created_subjisn = None
        test_result = 'Fail'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        test_result = 'Ok'
    writeresult(resp, created_subjisn, test_result)

    case = 'Попытка создания дубля'
    if details == True:
        print (case)
        print ('Исходный контрагент')
    testsubject = NewSubject()
    if details == True:
        print (testsubject)
    resp = api.newsubject(testsubject)
    # обрабатываем случай, когда результат не вернулся
    if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
        created_subjisn = None
        test_result = 'Fail'
    else:
        created_subjisn = resp[2]['result']['data']['id']
        if details == True:
            print(testsubject)
            print('Новый контрагент: ', created_subjisn)
        testsubject = NewSubject()
        if details == True:
            print('----------')
            print ('Проверяем кейс с дублем по номеру телефона')
        del testsubject['sex']
        del testsubject['latinname']
        del testsubject['drivingdatebeg']
        del testsubject['citizenship']
        del testsubject['address']
        del testsubject['document']
        resp2 = api.newsubject(testsubject)
        created_subjisn2 = resp2[2]['result']['data']['id']
        if details == True:
            print(testsubject)
            print('Новый контрагент: ', created_subjisn2)
        testsubject = NewSubject()
        if details == True:
            print('----------')
            print ('Проверяем кейс с дублем по номеру паспорта и ВУ')
        del testsubject['sex']
        del testsubject['latinname']
        del testsubject['drivingdatebeg']
        del testsubject['citizenship']
        del testsubject['address']
        del testsubject['contact']
        resp3 = api.newsubject(testsubject)
        created_subjisn3 = resp3[2]['result']['data']['id']
        if details == True:
            print(testsubject)
            print('Новый контрагент: ', created_subjisn3)
        testsubject = NewSubject()
        if details == True:
            print('----------')
        testsubject = NewSubject()
        if details == True:
            print('----------')
            print ('Проверяем кейс с символами и е-ё в фамилии')
        testsubject["lastname"] = "Тёстовыи "
        resp5 = api.newsubject(testsubject)
        created_subjisn5 = resp5[2]['result']['data']['id']
        if details == True:
            print(testsubject)
            print('Новый контрагент: ', created_subjisn2)
            print ('Проверяем кейс с дублем по ФИО и дате рождения')
        del testsubject['sex']
        del testsubject['latinname']
        del testsubject['drivingdatebeg']
        del testsubject['citizenship']
        del testsubject['address']
        del testsubject['contact']
        del testsubject['document']
        resp4 = api.newsubject(testsubject)
        resp6 = api.newsubject(testsubject)
        created_subjisn4 = resp4[2]['result']['data']['id']
        created_subjisn6 = resp6[2]['result']['data']['id']
        if details == True:
            print(testsubject)
            print('Новый контрагент: ', created_subjisn4)
            print('Новый контрагент: ', created_subjisn6)
        if created_subjisn4 == created_subjisn6:
            if created_subjisn == created_subjisn2 == created_subjisn3 == created_subjisn5:
                test_result = 'Ok'
        else:
            test_result = 'Fail'
    writeresult(resp, created_subjisn, test_result)

    case = 'Многократная отправка данных'
    if details == True:
        print (case)
    testsubject = NewSubject()
    if details == True:
        print (testsubject)
    i = 0
    isn = set()
    while i <= 10:
        resp = api.newsubject(testsubject)
        # обрабатываем случай, когда результат не вернулся
        if resp[2].get('result') == None or resp[2].get('result') == {'data': None}:
            created_subjisn = resp[2]['result']['data']['id']
            test_result = 'Fail'
            created_subjisn = None

        else:
            created_subjisn = resp[2]['result']['data']['id']
            isn.add(created_subjisn)
        i += 1
    if len(isn) == 1:
        test_result = 'Ok'
    else:
        test_result = 'Fail'
    if details == True:
        print (str(isn))

    writeresult(resp, created_subjisn, test_result)

    timeend = datetime.datetime.now()
    if details == True:
        print('----------')
        print('----------')
        print('Время, затраченное на тест:', timeend-timebeg)

    else:
        if 'Fail' in mainresult:
            print('Fail')
        else:
            print('Ok')