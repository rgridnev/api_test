import datetime
import apiclass as ac
import connectiondata as cd
from generalfunc import b64tofile

def getprintformtest():
    print('Запускаем тест печатных форм')
    api = ac.apirequest('sravni')
    print('Проверяем дефолтную печатную форму ВЗР')
    response = api.getprintform('892316544')
    b64 = response[3]
    filename = 'sravni_892316544_vzrdefault.pdf'
    try:
        b64tofile(b64, filename)
        print(filename, 'Ok')
    except:
        print(response)

    print('Проверяем кастомную печатную форму ВЗР')
    response = api.getprintform('892316544', '9590')
    b64 = response[3]
    filename = 'sravni_892316544_vzr9590.pdf'
    try:
        b64tofile(b64, filename)
        print (filename, 'Ok')
    except:
        print(response)

    print('Проверяем еОСАГО')
    response = api.getprintform('892080200')
    b64 = response[3]
    filename = 'sravni_892316544_osagodefault.pdf'
    try:
        b64tofile(b64, filename)
        print (filename, 'Ok')
    except:
        print(response)

    print('Проверяем чужой полис')
    try:
        response = api.getprintform('892725116')
        b64 = response[3]
        filename = 'sravni_892316544_vzranothercreator.pdf'
        b64tofile(b64, filename)
        print (filename, response[2], 'Fail')
    except:
        print ('Ok')

    print('Проверяем чужой полис ОСАГО')
    try:
        response = api.getprintform('891254214')
        b64 = response[3]
        filename = 'sravni_892316544_osagoanothercreator.pdf'
        b64tofile(b64, filename)
        print (filename, response[2], 'Fail')
    except:
        print ('Ok')

    print('Проверяем другую печатную форму')
    try:
        response = api.getprintform('892316544', '7110')
        b64 = response[3]
        filename = 'sravni_892316544_vzranotherprintform.pdf'
        b64tofile(b64, filename)
        print (filename, response[2], 'Fail')
    except:
        print ('Ok')

    print('Проверяем аннулированный полис')
    try:
        response = api.getprintform('892163928')
        b64 = response[3]
        filename = 'sravni_892316544_vzranotherstatus.pdf'
        b64tofile(b64, filename)
        print (filename, response[2], 'Fail')
    except:
        print ('Ok')
