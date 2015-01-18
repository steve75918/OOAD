from dogdoor import *
from remote  import *

door = DogDoor()
remote = Remote(door)

print("Fido barks to go outside...")
remote.press_button()

print("\nFido has gone outside...")

print("\nFido's all done...")
# Fido done everything in time limit

print("\nFido's back inside...")