import hashlib
import requests
from utils.config import get_broker_api_key, get_broker_api_secret

API_KEY = get_broker_api_key()
API_SECRET = get_broker_api_secret()
AUTH_URL = "https://authapi.flattrade.in/trade/apitoken"

def flattrade_auth(code, client=None):
    """Exchange Flattrade code for session token and return (token, uid, error)

    Returns:
        token (str) or None
        uid (str) or None
        error_message (str) or None
    """
    if not code:
        return None, None, "No code provided"

    raw = API_KEY + code + API_SECRET
    sha256 = hashlib.sha256(raw.encode()).hexdigest()

    payload = {
        "api_key": API_KEY,
        "request_code": code,
        "api_secret": sha256
    }

    try:
        r = requests.post(AUTH_URL, json=payload, timeout=10)
        data = r.json()
    except Exception as e:
        return None, None, f"HTTP error: {e}"

    if data.get("stat") != "Ok":
        return None, None, data.get("emsg") or "Auth failed"

    token = data.get("token")
    if not token:
        return None, None, "No token returned"

    # client param from redirect is the uid
    uid = client
    return token, uid, None
