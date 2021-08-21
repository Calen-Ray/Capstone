import requests
import json
import prettytable

headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['CXUFOODHOMELB0203M', 'CXUFOODHOMELB0204M'],"startyear":"2014", "endyear":"2019"})
p = requests.post('https://api.bls.gov/publicAPI/v1/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)

print(json_data['Results']['series'])

# for x in json_data['Results']['series'][0]['data']:
#     print(x)


# https://data.bls.gov/cgi-bin/dbdown?REQUEST_ERROR_MESSAGE