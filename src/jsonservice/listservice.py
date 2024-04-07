from .jsonservice_base import JsonServiceBase
import os
import json


class JsonListService(JsonServiceBase):
    def __init__(self, json_path: str, create_if_not_exists: bool = True):

        if not os.path.exists(json_path) and not create_if_not_exists:
            print(f"The given json file does not exists! ({json_path})")
            exit(1)

        if not os.path.exists(json_path):
            with open(json_path, 'w') as outfile:
                json.dump([], outfile)

        self._json_path = json_path
        json_data = open(self._json_path, 'r').read()
        self._data = json.loads(json_data)

    def write(self, path: str, value):
        pass

    def read(self, key):
        pass

    def read_index(self, index: int) -> dict | list | None:
        if type(self._data) is list:
            if index < len(self._data):
                return self._data[index]
        return None
