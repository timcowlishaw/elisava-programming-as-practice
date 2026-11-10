import tkinter
import paho.mqtt.client as mqtt

broker = "mqtt.sensical.es"
port = 1883
username = "demos"
password = "demos"

# The "#" means: listen to lab/circle and ALL its subtopics
# For example: lab/circle/color, lab/circle/size, lab/circle/x...
topic = "lab/circle/#"

# How the circle looks at the start
x = 200
y = 200
size = 50
color = "grey"

# Create a window with the circle
window = tkinter.Tk()
window.title("MQTT circle")

canvas = tkinter.Canvas(window, width=400, height=400, bg="white")
canvas.pack()

circle = canvas.create_oval(0, 0, 0, 0, fill=color, outline="")

label = tkinter.Label(window, text="Waiting for messages...")
label.pack()

# Draw the circle with the current x, y, size and color
def draw():
    canvas.coords(circle, x - size, y - size, x + size, y + size)
    canvas.itemconfig(circle, fill=color)

def on_connect(client, userdata, flags, reason_code, properties):
    client.subscribe(topic)
    label.config(text="Connecting to " + broker + ": " + str(reason_code))

# The topic tells us WHAT to change, the message tells us the NEW VALUE
# For example: topic "lab/circle/color" with message "red"
def on_message(client, userdata, message):
    global x, y, size, color

    value = message.payload.decode()
    label.config(text=message.topic + " = " + value)

    try:
        if message.topic == "lab/circle/color":
            color = value
        elif message.topic == "lab/circle/size":
            size = int(value)
        elif message.topic == "lab/circle/x":
            x = int(value)
        elif message.topic == "lab/circle/y":
            y = int(value)
        elif message.topic == "lab/circle/background":
            canvas.config(bg=value)
        draw()
    except:
        # If the value makes no sense (like size "banana"), ignore it
        label.config(text="I don't understand: " + message.topic + " = " + value)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)

# Check for new messages every 50 ms, while the window keeps running
def check_messages():
    client.loop(timeout=0.01)
    window.after(50, check_messages)

draw()
check_messages()
window.mainloop()
