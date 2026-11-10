import paho.mqtt.client as mqtt

# The broker is the "post office": everyone connects to it
broker = "mqtt.sensical.es"
port = 1883
username = "demos"
password = "demos"

# The topic is the "channel" we want to listen to
topic = "lab/chat"

# This function runs when we connect to the broker
def on_connect(client, userdata, flags, reason_code, properties):
    print ("Connecting to " + broker + ": " + str(reason_code))
    client.subscribe(topic)
    print ("Listening to " + topic)

# This function runs every time a new message arrives
def on_message(client, userdata, message):
    text = message.payload.decode()
    print ("New message on " + message.topic + ": " + text)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)

# Keep listening forever (stop with Ctrl+C)
client.loop_forever()
