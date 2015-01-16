from dogdoor import *
from remote  import *

door = DogDoor()
remote = Remote(door)

print("Fido barks to go outside...")
remote.press_button()

print("\nFido has gone outside...")
remote.press_button()

print("\nFido's all done...")
remote.press_button()

print("\nFido's back inside...")
remote.press_button()