import os
import json


class JsonServiceBase:
    def _read(self, key) -> dict | list | None:
        if '.' in key:
            return self._read_subkey(key.split('.'), self._data)
        else:
            return self._read_subkey([key], self._data)


    def read_all(self) -> dict | list:
        return self._data


    def read_index(self, index: int) -> dict | list | None:
        if type(self._data) is list:
            if index < len(self._data):
                return self._data[index]
        return None


    def _read_subkey(self, keys: list[str], source: dict):
        if len(keys) == 0 or type(source) is not dict:
            return None

        if len(keys) == 1:

            if keys[0] in source.keys():
                return source[keys[0]]
            else:
                return None

        if keys[0] in source.keys():
            return self._read_subkey(keys[1:], source[keys[0]])

        return None


    def _write(self, path: str, value):
        pass


class JsonService:
    def __init__(self, json_path: str, create_if_not_exists: bool = True, default_data: type | None = None):


        if not os.path.exists(json_path) and not create_if_not_exists:
            print(f"The given json file does not exists! ({json_path})")
            exit(1)

        if default_data != {} and default_data != []:
            print("Default data can only be an empty dictionary or list!")
            exit(1)

        if not os.path.exists(json_path):
            with open(json_path, 'w') as outfile:
                json.dump(default_data, outfile)

        self._json_path = json_path
        json_data = open(self._json_path, 'r').read()
        self._data = json.loads(json_data)  # type:dict | list


    def __setitem__(self, key, value):
        self._write(key, value)

    def __getitem__(self, item):
        return self.read(item)


