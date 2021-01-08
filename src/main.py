# import debugpy

# debugpy.listen(("0.0.0.0", 5890))
# print("Waiting for debugger client to attach")
# debugpy.wait_for_client()

import json


def lambda_handler(event, context):
    print(json.dumps(event, indent=2))
    return event
