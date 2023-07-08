import requests
import time
from urllib.parse import urljoin

base_url = 'http://18.216.212.47:5601'
endpoint = ''
headers = {
    'kbn-xsrf': 'true',
}

params = {
    'jobParams': "(browserTimezone:America/Barbados,columns:!(),objectType:search,searchSource:(fields:!((field:'*',include_unmapped:true)),filter:!((meta:(field:timestamp,index:'90943e30-9a47-11e8-b64d-95841ca0b247',params:()),query:(range:(timestamp:(format:strict_date_optional_time,gte:now-7d,lte:now))))),index:'90943e30-9a47-11e8-b64d-95841ca0b247',parent:(filter:!(),index:'90943e30-9a47-11e8-b64d-95841ca0b247',query:(language:kuery,query:'')),sort:!((timestamp:desc)),trackTotalHits:!t),title:'test post url',version:'7.17.11')",
}

response = requests.post(
    'http://18.216.212.47:5601/api/reporting/generate/csv_searchsource',
    params=params,
    headers=headers,
    auth=('elastic', ''),
)
if response.status_code == 200:
    json_response = response.json()
    print(type(json_response['path']))
    test = str(json_response['path'])
    endpoint = test.strip()
    #endpoint = json_response['path']
    endpoint = '/api/reporting/jobs/download/lju9qap800ry3512ad8xoj4b'
    print(endpoint)
    print(type(endpoint))
    #full_URL = urljoin(base_url, endpoint)
    #full_URL = base_url+endpoint
    #print(full_URL)
    '''
    response1 = requests.get(full_URL)
    with open('outputpi4.csv', 'wb') as f:
        f.write(response1.content)
    '''
    
else:
    print('Failed to retrieve the JSON response. Status code:', response.status_code)


print(endpoint)
full_URL = base_url+endpoint
#full_URL = 'http://18.216.212.47:5601/api/reporting/jobs/download/lju8s6am00ry3512ad8ox8nk'
print(full_URL)
response1 = requests.get(full_URL)
with open('outputpi2.csv', 'wb') as f:
    f.write(response1.content)


'''
import requests
import urllib.parse

url = 'http://18.216.212.47:5601/api/reporting/generate/csv_searchsource'
job_params = '(browserTimezone:America/Barbados,columns:!(),objectType:search,searchSource:(fields:!((field:\'*\',include_unmapped:true)),filter:!((meta:(field:timestamp,index:90943e30-9a47-11e8-b64d-95841ca0b247,params:()),query:(range:(timestamp:(format:strict_date_optional_time,gte:now-7d,lte:now))))),index:90943e30-9a47-11e8-b64d-95841ca0b247,parent:(filter:!(),index:90943e30-9a47-11e8-b64d-95841ca0b247,query:(language:kuery,query:\'\'))),sort:!((timestamp:desc)),trackTotalHits:!t),title:\'test post url\',version:\'7.17.11\'):now)))'
params = {
    'jobParams': urllib.parse.quote(job_params)
}
headers = {
    'kbn-xsrf': 'true'
}
auth = ('elastic', '')

response = requests.post(url, params=params, headers=headers, auth=auth)

if response.status_code == 200:
    json_response = response.json()
    print(json_response)
else:
    print('Failed to retrieve the JSON response. Status code:', response.status_code)
'''
