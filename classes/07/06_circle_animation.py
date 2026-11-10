import time
import paho.mqtt.client as mqtt

broker = "mqtt.sensical.es"
port = 1883
username = "demos"
password = "demos"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username, password)
client.connect(broker, port)
client.loop_start()

# 1. Rainbow: go through a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for color in colors:
    client.publish("lab/circle/color", color)
    time.sleep(0.5)

# 2. Breathing: grow and shrink the circle
for size in range(20, 150, 10):
    client.publish("lab/circle/size", size)
    time.sleep(0.1)

for size in range(150, 20, -10):
    client.publish("lab/circle/size", size)
    time.sleep(0.1)

# 3. Travel: move the circle from left to right
for x in range(50, 360, 10):
    client.publish("lab/circle/x", x)
    time.sleep(0.05)

# Go back to the middle
client.publish("lab/circle/x", 200)
client.publish("lab/circle/size", 50)
time.sleep(1)

client.loop_stop()
print ("Done!")
