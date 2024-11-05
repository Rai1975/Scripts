from random import randint
import time

MESSAGE = list("Welcome back, Raihan!")
string_array = [""]*len(MESSAGE)
i = 0

while (i < len(MESSAGE)):
    string_array[i] = chr(randint(32,126))
    if string_array[i] == MESSAGE[i]:
        i += 1
    print("".join(string_array), end='\r')
    time.sleep(0.0005)

print_str = "".join(string_array)
print(f"\033[92m{print_str}\033[m")