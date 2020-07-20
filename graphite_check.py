import requests
import json
import sys

url = "https://play.grafana.org/api/datasources/proxy/1/render?target=aliasByNode(movingAverage(scaleToSeconds(apps.fakesite.*.counters.requests.count,%201),%202),%202)&format=json&from=-5min"
response_string = requests.get(url)
normal = float(sys.argv[1])
warning = float(sys.argv[2])
target_name = sys.argv[3]
response_json = response_string.json()
targets = len(response_json)
counter = 0
if targets < 1:
    print("UNKNOWN")
    sys.exit(3)
else:
    for i in range(targets):
        if response_json[i]['target'] == target_name:
            datapoints = len(response_json[i]['datapoints'])
            for j in range(datapoints):
                counter = 1
                if response_json[i]['datapoints'][j][0] != None and response_json[i]['datapoints'][j][0] > warning:
                    print("CRITICAL")
                    sys.exit(2)
                if response_json[i]['datapoints'][j][0] != None and response_json[i]['datapoints'][j][0] > normal:
                    print("WARNING")
                    sys.exit(1)

if counter == 0:
    print("UNKNOWN")
    sys.exit(3)
else:
    print("OK")
    sys.exit(0)
