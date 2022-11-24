import requests
import json
import grpc
import mlserver.grpc.converters as converters
import mlserver.grpc.dataplane_pb2_grpc as dataplane
import mlserver.types as types

# model_name = "json-hello-world"
model_name = "my-json-model"
inputs = {
    "name": "Foo Bar",
    "message": "Hello from Client (gRPC)!"
}
inputs_bytes = json.dumps(inputs).encode("UTF-8")

inference_request = types.InferenceRequest(
    inputs=[
        types.RequestInput(
            name="echo_request",
            shape=[len(inputs_bytes)],
            datatype="BYTES",
            data=[inputs_bytes],
            parameters=types.Parameters(content_type="str")
        )
    ]
)

inference_request_g = converters.ModelInferRequestConverter.from_types(
    inference_request,
    model_name=model_name,
    model_version=None
)

# grpc_channel = grpc.insecure_channel("localhost:8081")
grpc_channel = grpc.insecure_channel("localhost:8033")
grpc_stub = dataplane.GRPCInferenceServiceStub(grpc_channel)

response = grpc_stub.ModelInfer(inference_request_g)
print(response)
