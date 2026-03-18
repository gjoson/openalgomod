import json
import requests

BASE_URL = "https://piconnect.flattrade.in/PiConnectAPI"

def flattrade_request(uid, token, endpoint, jdata):

```
payload = {
    "jData": json.dumps(jdata, separators=(",", ":")),
    "jKey": token
}

r = requests.post(
    f"{BASE_URL}/{endpoint}",
    data=payload
)

return r.json()
