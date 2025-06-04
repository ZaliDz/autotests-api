import httpx

login_data = {"email": "user@example.com", "password": "string"}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_data)
access_token = login_response.json()["token"]["accessToken"]

headers = {"Authorization": f"Bearer {access_token}"}

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(me_response.json())
print("status_code:", me_response.status_code)
