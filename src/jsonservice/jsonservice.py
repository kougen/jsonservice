import json
import os
from .dictservice import JsonDictService
from .listservice import JsonListService
from .jsonservice_base import JsonServiceBase


class JsonService:
    def __init__(self, json_path: str, create_if_not_exists: bool = True, default_type: type | None = None):
        if default_type is not None and default_type not in [dict, list]:
            print("Default type can only be dict or list!")
            exit(1)

        if default_type is list:
            self.__service = JsonListService(json_path, create_if_not_exists)  # type: JsonServiceBase
        else:
            self.__service = JsonDictService(json_path, create_if_not_exists)  # type: JsonServiceBase

    def __setitem__(self, key, value):
        self.__service.write(key, value)

    def __getitem__(self, item):
        return self.__service.read(item)
