# JSON Service for Python

Makes it easy to read and write JSON files in Python.
It supports complex nested data structures and is very easy to use.

## Installation

```bash
pip install jsonservice
```

## Usage

```py
from jsonservice import JsonService

# Create a new JSON Service (creates a new file if it doesn't exist)
json_service = JsonService('data.json')

# Create a new JSON Service (will throw an error if the file doesn't exist)
json_service2 = JsonService('data2.json', create_file_if_not_exists=False)

# Creates a 'settings' object in the JSON file with a 'lights' property set to 'on'
json_service.write("settings.lights", "on")
```
