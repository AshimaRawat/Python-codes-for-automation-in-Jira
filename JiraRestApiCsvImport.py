
import requests
import json
import io
url= "https://ashima-rawat.atlassian.net/rest/api/2/issue/"
headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
}
with io.open("sample.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()

data=data.split("\n")
for rows in data:
 
 payload=json.dumps(
    {
    "fields": {
       "project":
       {
          "key": rows.split(",")[0]
       },
       "summary": rows.split(",")[1],
       "description": rows.split(",")[2],
       "issuetype": {
          "name": "Task"
       }
   }
}
)
 response=requests.post(url,headers=headers,data=payload,auth=("ashima.rawat2@gmail.com", "uHJpsCMLZ5gsapqHlzhO5308"))
 print(response.text)
