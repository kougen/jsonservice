import os
import sys
from pathlib import Path
path_root = Path(__file__).parents[1]
sys.path.append(os.path.join(path_root, 'src'))

from jsonservice import JsonService

users_path = os.path.join(path_root, 'data', 'tests.json')

if __name__ == "__main__":
    service = JsonService(users_path)
    service.write('settings.lighthouse', 'on')




