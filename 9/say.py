import cowsay
import pyttsx3
import math

# engine = pyttsx3.init()

# this = input("Whats this? ")
# cowsay.cow(this)
# engine.say(this)
# engine.runAndWait(this)

linkedList = [1,2,3,4,5]
mid = math.ceil(len(linkedList)/2)
if len(linkedList) % 2 == 0:
    print((linkedList[mid::]))
else:
    print((linkedList[mid-1::]))
print(mid)