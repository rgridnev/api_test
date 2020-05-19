import tests as tst
import os


DIR = os.listdir('testresult')
# print(DIR)
for element in DIR:
     os.remove('testresult'+chr(92)+element)

tst.mortsberprop('sravni', 5000000)
tst.getprintformtest()
tst.postsubjecttest('che')
# tst.loadgetsubject()

# import apiclass as ac
# api = ac.apirequest('sravni')
# print(api.cancelagr(892962392))

# import testdata
# print (testdata.sberprop)

# import generalfunc as gf
# gf.soaphash('Auth')
