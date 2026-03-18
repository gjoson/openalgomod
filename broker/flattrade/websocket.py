import websocket
import json

class FlattradeWS:

def __init__(self, uid, token):
    self.uid = uid
    self.token = token
    self.ws = websocket.WebSocketApp(
        "wss://piconnect.flattrade.in/PiConnectWSAPI/",
        on_open=self.on_open,
        on_message=self.on_message
    )

def on_open(self, ws):

    login = {
        "t": "c",
        "uid": self.uid,
        "actid": self.uid,
        "source": "API",
        "susertoken": self.token
    }

    ws.send(json.dumps(login))

def subscribe(self, exchange, token):

    sub = {
        "t": "t",
        "k": f"{exchange}|{token}"
    }

    self.ws.send(json.dumps(sub))

def on_message(self, ws, message):
    print(message)

def connect(self):
    self.ws.run_forever()
