# Class 05 - MQTT

## 1. Install

```
pip install -r requirements.txt
```

## 2. Run

Run an example:

```
python 01_subscribe.py
python 02_chat.py
python 03_light.py
python 04_circle.py
python 05_circle_controller.py
python 06_circle_animation.py
```

Stop an example with `Ctrl + C`.

## 3. Examples list

- `01_subscribe.py`: listens and prints every message.
- `02_chat.py`: write your name, then write messages to chat with the class.
- `03_light.py`: a circle turns green when a new message arrives.
- `04_circle.py`: a circle you control with messages.
- `05_circle_controller.py`: change the circle by typing.
- `06_circle_animation.py`: makes the circle do a little animation.

Tip: open two terminals. Run `02_chat.py` in one and `03_light.py` in the other.

## 4. Circle

Run `04_circle.py` in one terminal and leave it open. Then, in another terminal, send messages. Each subtopic changes one thing:

| Topic                  | Example message   |
|------------------------|-------------------|
| `lab/circle/color`      | `red` or `#ff00ff` |
| `lab/circle/size`       | `80`              |
| `lab/circle/x`          | `100`             |
| `lab/circle/y`          | `300`             |
| `lab/circle/background` | `black`           |

Send them with `05_circle_controller.py`, or make your own animation by changing `06_circle_animation.py`.
