import requests
import time

base_url = 'http://18.216.212.47:5601'
headers = {
    'kbn-xsrf': 'true',
}

params = {
    'jobParams': "(browserTimezone:America/Barbados,columns:!(),objectType:search,searchSource:(fields:!((field:'*',include_unmapped:true)),filter:!((meta:(field:timestamp,index:'90943e30-9a47-11e8-b64d-95841ca0b247',params:()),query:(range:(timestamp:(format:strict_date_optional_time,gte:now-7d,lte:now))))),index:'90943e30-9a47-11e8-b64d-95841ca0b247',parent:(filter:!(),index:'90943e30-9a47-11e8-b64d-95841ca0b247',query:(language:kuery,query:'')),sort:!((timestamp:desc)),trackTotalHits:!t),title:'test post url',version:'7.17.11')",
}

# Make a POST request to return endpoint of a CSV report.
#Endpoint contained in path field of the JSON response.
response = requests.post(
    'http://18.216.212.47:5601/api/reporting/generate/csv_searchsource',
    params=params,
    headers=headers,
    auth=('elastic', ''),
)

if response.status_code == 200:
    # Extract the endpoint from the JSON response
    json_response = response.json()
    endpoint = json_response["path"]

    # Construct the full URL by combining the base URL and the endpoint
    full_URL = base_url + endpoint


    # Wait for 5 seconds
    time.sleep(5)

    # Make a GET request to the full URL to download the CSV report
    response = requests.get(full_URL)

    # Write the content of the response to a file named 'output.csv'
    with open('output.csv', 'wb') as f:
        f.write(response.content)
else:
    print('Failed to retrieve the JSON response. Status code:', response.status_code)
