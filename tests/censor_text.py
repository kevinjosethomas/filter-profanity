import time
from profanity import Profanity

lipsum = "This code is actually not idiotic trash! It's not as stupid as you expect it to be! It looks pretty shit, but it's actually really fast :)"

unspecified_time = 0
specified_time = 0

for i in range(2):
    time1 = time.time()
    Profanity.censor(lipsum)
    unspecified_time = time.time() - time1

for i in range(2):
    time2 = time.time()
    Profanity.censor(lipsum, "!)(#*$(#*($)))")
    specified_time = time.time() - time2

print(f"Unspecified Character Total - {unspecified_time}")
print(f"Unspecified Character Average - {unspecified_time / 2}")
print(f"Specified Character Total - {specified_time}")
print(f"Specified Character Average - {specified_time / 2}")
