import tkinter
import paho.mqtt.client as mqtt

broker = "mqtt.sensical.es"
port = 1883
username = "demos"
password = "demos"
topic = "lab/chat"

# Create a small window with a grey circle
window = tkinter.Tk()
window.title("MQTT light")

canvas = tkinter.Canvas(window, width=200, height=200, bg="white")
canvas.pack()

circle = canvas.create_oval(50, 50, 150, 150, fill="grey")

label = tkinter.Label(window, text="Waiting for messages...")
label.pack()

def turn_off():
    canvas.itemconfig(circle, fill="grey")

def on_connect(client, userdata, flags, reason_code, properties):
    client.subscribe(topic)
    label.config(text="Connecting to " + broker + ": " + str(reason_code))

# When a message arrives: turn the circle green, show the text,
# and turn it grey again after 1 second (1000 ms)
def on_message(client, userdata, message):
    text = message.payload.decode()
    canvas.itemconfig(circle, fill="green")
    label.config(text=text)
    window.after(1000, turn_off)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)

# Check for new messages every 100 ms, while the window keeps running
def check_messages():
    client.loop(timeout=0.01)
    window.after(100, check_messages)

check_messages()
window.mainloop()
