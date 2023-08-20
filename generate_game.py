import os
import time
import json
import random
import g4f

# supported args
print(g4f.Provider.Ails.params)

# The user can input games like: checker, tic-tac-toe, chess
gameName = input(f"Enter the game you want to play: ")

# according to the gameName the user input, the algorithm asks the ChatGPT to generate game file
# and launch it, so the user can play it directly.
response = g4f.ChatCompletion.create(model=g4f.Model.gpt_4, provider=g4f.Provider.GetGpt, messages=[
                                     {"role": "user", "content": "Generate a Python script to play game of " + gameName}])

# splits the response line by line, so we can store it in the file
responseLines = response.splitlines()

fname = 'generated.py'

# store the response in the file "generated.py", and only reserve the code section
with open(fname, 'w') as f:
  startPythonLog = 0
  for line in responseLines:
    if line == "```":
      break
    if startPythonLog == 1:
      f.write(line + "\n")
    if line == "```python":
      startPythonLog = 1

# execute the generated file, so the game start
with open("generated.py") as f:
    exec(f.read())


