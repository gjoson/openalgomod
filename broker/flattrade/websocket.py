import websocket
import json
import threading
import time

class FlattradeWS:
    def __init__(self, uid, token, on_message_callback=None):
        self.uid = uid
        self.token = token
        self.on_message_callback = on_message_callback
        self.ws = websocket.WebSocketApp(
            "wss://piconnect.flattrade.in/PiConnectWSAPI/",
            on_open=self._on_open,
            on_message=self._on_message,
            on_close=self._on_close,
            on_error=self._on_error
        )
        self._thread = None

    def _on_open(self, ws):
        login = {
            "t": "c",
            "uid": self.uid,
            "actid": self.uid,
            "source": "API",
            "susertoken": self.token
        }
        ws.send(json.dumps(login))

    def subscribe(self, exchange, token_id):
        # token_id example: "26000"
        sub = {"t": "t", "k": f"{exchange}|{token_id}"}
        self.ws.send(json.dumps(sub))

    def _on_message(self, ws, message):
        if self.on_message_callback:
            self.on_message_callback(message)
        else:
            print("WS MSG:", message)

    def _on_close(self, ws, code, reason):
        print("WS closed", code, reason)

    def _on_error(self, ws, error):
        print("WS error", error)

    def start(self):
        self._thread = threading.Thread(target=self.ws.run_forever, daemon=True)
        self._thread.start()
        # small wait to let socket open
        time.sleep(0.5)

    def stop(self):
        try:
            self.ws.close()
        except Exception:
            pass
