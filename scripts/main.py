import os
import sys
from pathlib import Path
path_root = Path(__file__).parents[1]
sys.path.append(os.path.join(path_root, 'src'))

from jsonservice import JsonService

users_path = os.path.join(path_root, 'data', 'tests.json')

def test_json_service_dict():
    service = JsonService(users_path)
    service.write('settings.lighthouse', 'on')

    dummy = {
        'name': 'John Doe',
        'email': 'john@doe.com',
        'age': 25
    }

    print(service.read_all())

    service.write('users.john', dummy)

    print(service.read_all())

if __name__ == "__main__":
    test_json_service_dict()





