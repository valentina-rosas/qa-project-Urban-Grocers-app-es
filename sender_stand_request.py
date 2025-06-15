import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})

response = get_logs()
print(response.status_code)
print(response.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def get_new_user_token():
    user_body = data.user_body
    auth_token = get_new_user_token()
    response_user = post_new_user(user_body)
    return response_user.json()["authToken"]

def get_kit_model():
    return requests.get(configuration.URL_SERVICE + configuration.KIT_MODEL_PATH)

response = get_kit_model()
print(response.status_code)

def post_new_client_kit(kit_body):
    response = post_new_user(data.user_body).json()
    auth_token = response['authToken']
    auth_header = data.headers.copy()
    auth_header["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body, headers=auth_header)
