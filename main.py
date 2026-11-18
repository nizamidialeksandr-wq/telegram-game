import os
from dotenv import load_dotenv

load_dotenv()
foo = os.getenv("FOO")

print("hello world")
print(foo)