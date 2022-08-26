
import requests
from requests.auth import HTTPBasicAuth
import json
import io

# In the url mention the Jira url used
url = "https://ashima-rawat.atlassian.net/rest/api/2/issue/"

# We are using HTTPBasicAuth authentication method here.
# For that create a JIRA api token and mention your userid and token down in the brackets()
auth = HTTPBasicAuth("ashima.rawat2@gmail.com", "uHJpsCMLZ5gsapqHlzhO5308")

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

url='https://www.random.com'
data=json.dumps(all_issues)
headers={'Content-Type': 'application/json'}

response = requests.post(url, data=data, headers=headers)

payload = json.dumps( 
    {
    "fields": {
       "project":
       {
          "key": "JIR"         # Here in the key write the key of your project for which issue needs to be created
       },
       "summary": "via RestApi.",
       "description": "Creating of an issue using project keys and issue type names using the REST API",
       "issuetype": {
          "name": "Task"      # Here in the name section, write the name of the issuetype you want to create.
       }
   }
})
  
response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))