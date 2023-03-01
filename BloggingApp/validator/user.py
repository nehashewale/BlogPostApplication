from jsonschema import validate


schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "username": {"type": "string"},
      "required": [
        "name", "username"
      ]
    }
  }


def validate_user_schema(body):
    try:
        validate(body,schema)
        return True
    except:
        return False