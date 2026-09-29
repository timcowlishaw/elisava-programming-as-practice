import time

limit = 4

name = input("What is your name? ")

print ("Thinking.", end="\r")
time.sleep(1)
print ("Thinking..", end="\r")
time.sleep(1)
print ("Thinking...", end="\r")
time.sleep(1)
print ("Thinking....")
time.sleep(1)

name_length = len(name)

if (name_length > limit):
    print ("What a long name! Nice to meet you, " + name + "!")
else:
    print ("What a short name! Nice to meet you, " + name + "!")


