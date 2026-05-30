import socketio
import websocket
import json

# ===== CONFIG =====
STREAMLABS_TOKEN = "YourSocketTokenHere" #You find it here: https://streamlabs.com/dashboard#/settings/api-settings -> API Token -> Your Socket API Token !!! Do not share !!!
STREAMERBOT_WS = "ws://127.0.0.1:8080"

REWARD_ACTIONS = {
	#Here your Rewards
	#"StreamlabsRewardName": "StreamerBotActionName" add comma after the " if you add another one. Please note Capitalization.
}

DEFAULT_ACTION = "Streamlabs Default"




# ================= STREAMER.BOT SEND =================
sb_ws = None

def connect_streamerbot():
    global sb_ws

    try:
        if sb_ws:
            sb_ws.ping()
            return sb_ws
    except:
        pass

    print("Connecting to Streamer.bot...")
    sb_ws = websocket.create_connection(STREAMERBOT_WS)

    return sb_ws

def send_to_streamerbot(action, user, text, reward):
    global sb_ws

    payload = {
        "request": "DoAction",
        "id": "Streamlabstostreamerbot",
        "action": {
            "name": action
        },
        "args": {
            "user": user,
            "text": text,
            "reward": reward
        }
    }

    try:
        ws = connect_streamerbot()

        ws.send(json.dumps(payload))
        print("Sent to Streamer.bot:", action)

    except Exception as e:
        print("Send error:", e)

        with ws_lock:
            try:
                sb_ws.close()
            except:
                pass

            sb_ws = None


# ================= STREAMLABS =================
sio = socketio.Client(logger=False, engineio_logger=False)


@sio.event
def connect():
    print("Streamlabs connected")


@sio.on("event")
def on_event(data):
    try:
        msg = data.get("message", [{}])[0]

        if msg.get("type") != "redemption":
            return

        user = msg.get("name")
        text = msg.get("message")
        reward = msg.get("redemption_name")

        print(f"Redemption: {reward} {user} {text}")

        action = REWARD_ACTIONS.get(reward, DEFAULT_ACTION)

        send_to_streamerbot(action, user, text, reward)

    except Exception as e:
        print("Parse error:", e)


@sio.event
def disconnect():
    print("Streamlabs disconnected")


# ================= START =================
try:
    sio.connect(
        f"https://sockets.streamlabs.com?token={STREAMLABS_TOKEN}",
        transports=["websocket"],
        wait_timeout=10
    )

    print("Listening...")
    sio.wait()

except Exception as e:
    print("ERROR:", repr(e))
