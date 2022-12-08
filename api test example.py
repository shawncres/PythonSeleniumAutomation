from azure.identity import InteractiveBrowserCredential
import json
import requests



HIVEMIND_COMMISSIONING_V1_BASE_URL = "https://attabotics-hivemind-commissioning-api-test.azurewebsites.net/api/v1"



def join_url_parts(*args):
    return '/'.join(args)
credential = InteractiveBrowserCredential(tenant_id="71834f06-a94d-424c-8343-784f61bb658b", client_id="ebfed274-c052-45e2-b15e-f240a5f9c59b")
token = credential.get_token("https://attabotics.com/test/Commissioning.Read.All", tenant_id="71834f06-a94d-424c-8343-784f61bb658b").token
headers = {"Authorization": f'Bearer {token}', 'Content-Type': 'application/json'}
def get_request_as_json(url):
    request = requests.get(url, headers=headers)
    return json.loads(request.content)
def put_request_as_json(url, data):
    request = requests.put(url, data, headers=headers)
    return json.loads(request.content)



ant = get_request_as_json(join_url_parts(HIVEMIND_COMMISSIONING_V1_BASE_URL, "Ants","GG745"))

##ant["isInCommission"] = False
##
##
##updated_ant = put_request_as_json(join_url_parts(HIVEMIND_COMMISSIONING_V1_BASE_URL, "Ants", "7a36df72-4231-43de-a5a3-001a25458a3a"), json.dumps(ant))
##

print(ant)



