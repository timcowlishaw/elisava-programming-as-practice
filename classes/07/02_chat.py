import paho.mqtt.client as mqtt

broker = "mqtt.sensical.es"
port = 1883
username = "demos"
password = "demos"
topic = "lab/chat"

name = input("What is your name? ")

def on_connect(client, userdata, flags, reason_code, properties):
    print ("Connecting to " + broker + ": " + str(reason_code))
    print ("Write a message and press Enter to send it.")
    client.subscribe(topic)

def on_message(client, userdata, message):
    text = message.payload.decode()
    print (text)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)

# Listen in the background, so we can still type with input()
client.loop_start()

while True:
    text = input()
    client.publish(topic, name + ": " + text)
