from dogdoor 			import *
from remote  			import *
from time    			import *
from bark_recognizer 	import *

door = DogDoor(3)
remote = Remote(door)
bark_recongnizer = BarkRecognizer(door)

print("Fido barks to go outside...")
# remote.press_button()
bark_recongnizer.recognize("woof")

print("\nFido has gone outside...")
print("\nFido's all done...")

# sleep  10 seconds
sleep(10)

print("\n...but he's stuck outside!")
print("\nFido starts barking...")
# print("...so Todd grabs the remote control.")
# remote.press_button()
bark_recongnizer.recognize("woof")

print("\nFido's back inside...")