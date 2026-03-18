import json
import requests

BASE_URL = "https://piconnect.flattrade.in/PiConnectAPI"


def flattrade_request(uid, token, endpoint, jdata, timeout=10):
    payload = {
        "jData": json.dumps(jdata, separators=(",", ":")),
        "jKey": token
    }
    r = requests.post(f"{BASE_URL}/{endpoint}", data=payload, timeout=timeout)
    try:
        return r.json()
    except Exception:
        return {"stat":"Not_Ok","emsg":"Invalid JSON response","raw": r.text}
