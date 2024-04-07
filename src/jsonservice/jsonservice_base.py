
class JsonServiceBase:
    def read(self, key) -> dict | list | None:
        pass

    def read_all(self) -> dict | list:
        pass

    def read_index(self, index: int) -> dict | list | None:
        pass

    def write(self, path: str, value):
        """
        Write a value to a dictionary or list.
        :param path: The path to the value in the dictionary or list. Example: 'settings.lighthouse'
        :param value: The value to write.
        :return: None
        """
        pass

    def write_sub_list(self, root_key: str, path: str, value):
        """
        Write a value to a list in a dictionary or list.

        :param root_key: The key of the dictionary or list. If the root_key is a list, the index will be used. If the
        root_key is a dictionary, the key will be used.
        :param path: The path to the list in the dictionary or list.
        :param value: The value to write.
        :return: None
        """
        pass
