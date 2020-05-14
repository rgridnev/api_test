import generalfunc as gf
import connectiondata as cd
import requests, json, datetime

class apirequest():
    """getsubject - выдаёт данные о контрагенте по ISN
       newsubject - создаёт или отдаёт существующего контрагента по его данным
    """

    def __init__(self, user):
        self.token = gf.GetToken(user)
        self.api_call_headers = {'Authorization': 'Bearer ' + self.token}

    def getsubject(self, subjisn):
        resp = []
        timebeg = datetime.datetime.now()
        api_call_response = requests.get(cd.test_api_url + '/subject/' + str(subjisn), headers=self.api_call_headers,
                                         verify=False)
        subject = json.loads(api_call_response.text)
        timeend = datetime.datetime.now()

        resp.append(api_call_response.status_code)
        resp.append((timeend - timebeg).microseconds / 1000)
        resp.append(json.loads(api_call_response.text))
        return resp

    def newsubject(self, subject):
        resp = []
        timebeg = datetime.datetime.now()
        api_call_response = requests.post(cd.test_api_url + '/subject', json=subject, headers=self.api_call_headers,
                                          verify=False)
        # subject = json.loads(api_call_response.text)
        timeend = datetime.datetime.now()

        resp.append(api_call_response.status_code)
        resp.append((timeend - timebeg).microseconds / 1000)
        resp.append(json.loads(api_call_response.text))
        return resp

    def getprintform(self, agrisn, formisn=None):
        resp = []
        timebeg = datetime.datetime.now()
        if formisn != None:
            form_headers = self.api_call_headers.copy()
            form_headers.update({"pf_id": formisn})
        else:
            form_headers = self.api_call_headers
        api_call_response = requests.get(cd.test_api_url + '/print/agreement/' + str(agrisn), headers=form_headers,
                                         verify=False)
        formjson = json.loads(api_call_response.text)
        callid = formjson['call_id']
        timeend = datetime.datetime.now()
        resp.append(api_call_response.status_code)
        resp.append((timeend - timebeg).microseconds / 1000)
        resp.append(callid)
        try:
            form = formjson['result']['data']['document']['bytes'].replace("\n", "")
            resp.append(form)
        except:
            error = formjson['status']['message']
            resp.append(error)
        return resp

    def paylink(self, agrisn, sms=False, email=False, webhook=None):
        resp = []
        request = {}
        request['isn'] = agrisn
        request['sms'] = str(sms)
        request['email'] = str(email)
        if webhook != None:
            request['webhook'] = str(webhook)
        print(request)
        timebeg = datetime.datetime.now()
        form_headers = self.api_call_headers
        api_call_response = requests.post(cd.test_api_url + '/payment/link/agreement', json=request, headers=form_headers,
                                          verify=False)
        linkjson = json.loads(api_call_response.text)
        callid = linkjson['call_id']
        timeend = datetime.datetime.now()
        resp.append(api_call_response.status_code)
        resp.append((timeend - timebeg).microseconds / 1000)
        resp.append(callid)
        try:
            link = linkjson['result']['data']['payment_link']
            resp.append(link)
        except:
            error = linkjson['status']['message']
            resp.append(error)
        return resp

    def cancelagr(self, agrisn):
        resp = []
        timebeg = datetime.datetime.now()
        form_headers = self.api_call_headers
        api_call_response = requests.put(cd.test_api_url + '/agreement/set/annul/' + str(agrisn), headers=form_headers,
                                         verify=False)
        respjson = json.loads(api_call_response.text)
        callid = respjson['call_id']
        timeend = datetime.datetime.now()
        resp.append(api_call_response.status_code)
        resp.append((timeend - timebeg).microseconds / 1000)
        resp.append(callid)
        data = respjson['status']
        resp.append(data)
        return resp

    def confirmagr(self, agrisn):
        resp = []
        timebeg = datetime.datetime.now()
        form_headers = self.api_call_headers
        api_call_response = requests.put(cd.test_api_url + '/agreement/set/released/' + str(agrisn), headers=form_headers,
                                         verify=False)
        respjson = json.loads(api_call_response.text)
        callid = respjson['call_id']
        timeend = datetime.datetime.now()
        resp.append(api_call_response.status_code)
        resp.append((timeend - timebeg).microseconds / 1000)
        resp.append(callid)
        data = respjson['status']
        resp.append(data)
        return resp