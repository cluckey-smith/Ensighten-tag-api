import requests
import base64
import pprint


from urllib2 import Request, urlopen


def get_tag(access_token):

  headers = {
    'Authorization': 'Bearer ' + str(access_token),
    'Accept': 'application/json'
  }
  url = 'https://manage-api.ensighten.com/manage/spaces/<space-number>/deployments'

  response = requests.get(url, headers=headers)
  return response.json()



def get_trigger(access_token):

  headers = {
    'Authorization': 'Bearer ' + str(access_token),
    'Accept': 'application/json'
  }
  url = 'https://manage-api.ensighten.com/manage/conditions'

  response = requests.get(url, headers=headers)
  return response.json()


def create_condition(condition_name, access_token):
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + str(access_token),
    'Accept': 'application/json'
  }

  body = {
    'comparatorId': 3,
    'modifierIds': [],
    'typeId': 2,
    'value': '.*'
  }
  url = 'https://manage-api.ensighten.com/manage/conditions/<conditionsId>'
  response = requests.post(url, headers=headers)
  return response


def create_tag(tag_name, access_token):

  headers = {
    'Content-Type':'application/json',
    'Authorization': 'Bearer ' + str(access_token),
    'Accept': 'application/json'
  }

  body = {
    "name": tag_name,
    "executionTime": "immediate",
    "comments": "comment for the app",
    "code": "console.log(\"testing app creation\");",
    "dependentDeployments": [
      {
        "deploymentId": "DeploymentId",
        "spaceId": "<spaceId>"
      }
    ],
    "conditionIds": [
      "ConditionID"
    ]
  }

  url = 'https://manage-api.ensighten.com/manage/spaces/<spaceID>/deployments'
  response = requests.post(url, headers=headers, data=body)
  return response

def authenticate(auth_64):

  headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic ' + auth_64
  }

  body = {

    'grant_type' : 'password'
  }

  url='https://manage-api.ensighten.com/auth/token'
  response = requests.post(url, headers=headers, data=body)
  return response


""" CHECKING THE PRE-EXISTING TAGs WITH THE SAME TAG NAME """
""" PASS THE EXCEL DETAILS IN THIS FUNCTION"""

def management(access_token ):
  tags = get_tag(access_token)
  tag_name = 'Demo'
  tag_list = []

  for _ in tags:
    tag_list.append(_['name'])

  print tag_list

  triggers = get_trigger(access_token)
  condition_name = 'Demo trigger'
  trigger_list = []

  for _ in tags:
    tag_list.append(_['name'])

  pprint.pprint(triggers)
  create_condition(condition_name, access_token)

  for _ in triggers:
    tag_list.append(_['name'])

  print trigger_list

  if tag_name in tag_list:
    print "Tag name already exists"

  else:
    create = create_tag(tag_name, access_token)

def main():

  account_name = '<account_name>'
  username = '<username>'
  password = '<password>'

  auth_64 = base64.b64encode(str(account_name)+':' +str(username)+':' +str(password))

  auth_keys = authenticate(auth_64)
  print auth_keys.json()
  access_token = auth_keys.json()['access_token']
  print access_token

  manager = management(access_token)

if __name__ == '__main__':

  main()

