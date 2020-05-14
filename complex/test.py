import tests as tst
import os

DIR = os.listdir('testdata')
print(DIR)
for element in DIR:
     os.remove('testdata'+chr(92)+element)

# tst.getprintformtest()
# tst.loadgetsubject()
# tst.postsubjecttest('sravni')

# import apiclass as ac
# api = ac.apirequest('sravni')
# print(api.getprintform('892080200'))
