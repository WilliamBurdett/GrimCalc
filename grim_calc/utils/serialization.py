import json
from typing import Any, Dict

import jsonpickle


def encode(any_obj: Any) -> Dict[str, Any]:
    json_str = jsonpickle.encode(any_obj)
    return json.loads(json_str)


def decode(any_json: Dict[str, Any]) -> Any:
    json_str = json.dumps(any_json)
    return jsonpickle.decode(json_str)
