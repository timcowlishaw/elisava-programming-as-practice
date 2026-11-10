import paho.mqtt.client as mqtt

broker = "mqtt.sensical.es"
port = 1883
username = "demos"
password = "demos"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username, password)
client.connect(broker, port)
client.loop_start()

print ("You can change: color, size, x, y, background")
print ("Colors can be names (red, blue, pink...) or codes (#ff00ff)")

while True:
    parameter = input("What do you want to change? ")
    value = input("New value? ")

    # Each parameter has its own subtopic: lab/circle/color, lab/circle/size...
    client.publish("lab/circle/" + parameter, value)
    print ("Sent " + value + " to lab/circle/" + parameter)
