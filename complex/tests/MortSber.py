import apiclass as ac
import generalfunc as gf

def mortsberprop(user, sum):
    api = ac.apirequest(user)
    print('Создаём котировку')
    api.mortsberpropcalc(sum)
    print('Создаём договор')
    agreement = api.mortsberpropagr(sum)
    try:
        isn = agreement[2]['result']['data']['isn']
        print('Ok', isn)
    except:
        print('Error!', agreement)
    # print('Получаем ссылку на оплату')
    # print(api.paylink(isn))
    print('Выпускаем договор')
    r = api.confirmagr(isn)
    if r[3]['code'] == 'success':
        print('Ok')
    else:
        print(r)

    print('Получаем печатную форму')
    b64 = api.getprintform(isn)[3]
    gf.b64tofile(b64, 'MortSberProp.pdf')
    print('Аннулируем договор')
    r = api.cancelagr(isn)
    if r[3]['code'] == 'success':
        print('Ok')
    else:
        print(r)
