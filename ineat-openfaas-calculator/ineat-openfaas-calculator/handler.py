import json
def handle(req):
    args_parse = json.loads(req)
    result = args_parse["operande1"] + args_parse["operande2"]
    return "Result : " + str(result)