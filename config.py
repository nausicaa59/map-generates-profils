import sys
import json
import os

# init env file...
env = {}
with open('env.json') as json_data:
	env = json.load(json_data)
	env["ROOT_DIR"] = os.path.dirname(os.path.abspath(__file__))
	sys.path.append(env["model"]["path"])


