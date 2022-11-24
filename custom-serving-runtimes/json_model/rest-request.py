import requests
import json

inputs = {
    "name": "Foo Bar",
    "message": "Hello from Client (REST)!"
}

# NOTE: this uses characters rather than encoded bytes. It is recommended that you use the `mlserver` types to assist in the correct encoding.
inputs_string= json.dumps(inputs)

inference_request = {
    "inputs": [
        {
            "name": "echo_request",
            "shape": [len(inputs_string)],
            "datatype": "BYTES",
            "data": [inputs_string]
        }
    ]
}

endpoint = "http://localhost:8008/v2/models/my-json-model/infer"
response = requests.post(endpoint, json=inference_request)

print(response.json())
