import base64
from fastapi import WebSocket, FastAPI


app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("started")
    await websocket.accept()
    try:
        while True:
            json = await websocket.receive_json()
            print(f"Received packet: {json['type']}")
            if json['type'] == "image":
                with open("imageToSave.jpg", "wb") as fh:
                    print(json['data']["base64"])
                    img = base64.b64decode(json['data']["base64"].replace("data:image/jpeg;base64,", ""))
                    fh.write(img)

    except Exception as e:
        print(e)
    finally:
        await websocket.close()