import httpx
from tools.fakers import get_random_email


create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)

login_payload = {"email": create_user_payload["email"], "password": create_user_payload["password"]}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
access_token = login_response.json()['token']['accessToken']

update_payload = {
  "email": "user@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
update_headers = {"Authorization": f"Bearer {access_token}"}
update_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response.json()["user"]["id"]}", headers=update_headers, json=update_payload)
print(update_response.json())
print("status_code:", update_response.status_code)
