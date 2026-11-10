import time

name = input("What is your name? ")

print ("Thinking.", end="\r")
time.sleep(1)
print ("Thinking..", end="\r")
time.sleep(1)
print ("Thinking...", end="\r")
time.sleep(1)
print ("Thinking....", end="\r")
time.sleep(1)

print ("What an amazing name! Nice to meet you, " + name + "!")