import requests

url = "https://sedp-gw.egat.co.th/api/commontemp"
# https://sedp-gw.egat.co.th/api/commonTempData

# payload = "{"
# payload += "\"pmv\":" + str(PMV) + ",";
# payload += "\"tgtTemp\":" + str(tgtTemp);
# payload += "}"

# payload = "[{"
# payload += "\"ts\":" + "2019-01-01 00:03:00" + ",";
# payload += "\"site\":" + "s0004"+ ",";
# payload += "\"group\":" + "air_iot"+ ",";
# payload += "\"item\":" + "temp"+ ",";
# payload += "\"value\":" + str(35);
# payload += "}]"

payload = "[{\"ts\" : \"2019-01-01 00:03:00\", \"site\" : \"s0004\", \"group\" : \"air_iot\", \"item\" : \"temp\",\"value\" : \"35\"}]"

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
