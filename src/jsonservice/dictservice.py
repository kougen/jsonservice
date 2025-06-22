from .jsonservice_base import JsonServiceBase
import json
import os


class JsonDictService(JsonServiceBase):
    def __init__(self, json_path: str, create_if_not_exists: bool = True):

        if not os.path.exists(json_path) and not create_if_not_exists:
            print(f"The given json file does not exists! ({json_path})")
            exit(1)

        if not os.path.exists(json_path):
            with open(json_path, 'w') as outfile:
                json.dump({}, outfile)

        self._json_path = json_path
        json_data = open(self._json_path, 'r').read()
        self._data = json.loads(json_data)  # type:dict

    def write(self, path: str, value):
        keys = path.split('.')
        result = self._data

        temp = result
        for i, key in enumerate(keys[:-1]):
            if key not in temp:
                temp[key] = {}
            temp = temp[key]

        temp[keys[-1]] = value

        with open(self._json_path, "w") as outfile:
            json.dump(self._data, outfile)

    def write_sub_list(self, root_key: str, path: str, value):
        keys = path.split('.')
        result = self._data

        temp = result[root_key]
        for i, key in enumerate(keys[:-1]):
            if key not in temp:
                temp[key] = {}
            temp = temp[key]

        temp[keys[-1]] = value

        with open(self._json_path, "w") as outfile:
            json.dump(self._data, outfile)

    def __read_subkey(self, keys: list[str], source: dict):
        if len(keys) == 0 or type(source) is not dict:
            return None

        if len(keys) == 1:

            if keys[0] in source.keys():
                return source[keys[0]]
            else:
                return None

        if keys[0] in source.keys():
            return self.__read_subkey(keys[1:], source[keys[0]])

        return None

    def read(self, key):
        if '.' in key:
            return self.__read_subkey(key.split('.'), self._data)
        else:
            return self.__read_subkey([key], self._data)
