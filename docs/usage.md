# Usage

## Creating a new JSON Service

You have several options when creating a new JSON Service:

1. Create a new JSON Service (creates a new file if it doesn't exist)
    ```py
    from jsonservice import JsonService

    json_service = JsonService('data.json')
    ```

2. Create a new JSON Service (will throw an error if the file doesn't exist)
    ```py
    from jsonservice import JsonService

    json_service = JsonService('data.json', create_file_if_not_exists=False)
    ```

3. You can choose the base of the JSON to either be a list or a dictionary
    ```py
    from jsonservice import JsonService

    # Create a new JSON Service with a dictionary as the base (default)
    json_service_dict = JsonService('data.json', default_data={})
   
    # Create a new JSON Service with a list as the base
    json_service_list = JsonService('data.json', default_data=[])
    ```
   
## Reading from a JSON file

You can read from a JSON file using the `read` method:

```py
from jsonservice import JsonService

json_service = JsonService('data.json')

# Read the entire JSON file
data = json_service.read()