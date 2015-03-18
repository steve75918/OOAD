from dogdoor            import *
from remote             import *
from time               import *
from bark_recognizer    import *
from bark               import *

door = DogDoor(3)
door.add_allowed_bark(Bark("rowlf"))
door.add_allowed_bark(Bark("rooowlf"))
door.add_allowed_bark(Bark("rawlf"))
door.add_allowed_bark(Bark("woof"))
remote = Remote(door)
bark_recognizer = BarkRecognizer(door)

# simulate the hardware hearing a bark
print("Bruce starts barking")
bark_recognizer.recognize(Bark("rowlf"))
print("\nBruce has gone outside...")

# sleep  10 seconds
sleep(10)

print("\nBruce's all done...")
print("\n...but he's stuck outside!")

# simulate the hardware hearing a bark(NOT Bruce)
small_dog_bark = Bark("yip")
print("A small dog starts barking.")
bark_recognizer.recognize(small_dog_bark)

sleep(5)

print("Bruce starts barking")
bark_recognizer.recognize(Bark("rooowlf"))

print("\nBruce's back inside...")