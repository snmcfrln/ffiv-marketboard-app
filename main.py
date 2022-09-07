import requests

dataCenters = requests.get("https://universalis.app/api/v2/data-centers")

print(dataCenters.status_code)
print(dataCenters.json())