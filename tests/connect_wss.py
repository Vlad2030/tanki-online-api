import asyncio
import websocket
websocket.enableTrace(True)

WSS_URL: str = "c8.eu.tankionline.com"
WSS_PORT: int = 19090


def on_message(wsapp, message):
    print(message)


wsapp = websocket.WebSocketApp(url=f"wss://{WSS_URL}:{WSS_PORT}", on_message=on_message)
wsapp.run_forever() 