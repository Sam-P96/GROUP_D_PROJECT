import sys
import time

def d_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

d_print("Hello, this was a mistake. I cant make this sentence any longer.")