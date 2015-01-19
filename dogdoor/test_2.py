from dogdoor import *
from remote  import *
from time    import *

door = DogDoor()
remote = Remote(door)

print("Fido barks to go outside...")
remote.press_button()

print("\nFido has gone outside...")
print("\nFido's all done...")

# sleep  10 seconds
sleep(10)

print("\n...but he's stuck outside!")
print("\nFido starts barking...")
print("...so Todd grabs the remote control.")
remote.press_button()

print("\nFido's back inside...")