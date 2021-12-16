import json
from typing import Union
from config import Config
import jsonschema


class GeneralChecker:
    @staticmethod
    def validate_json(item: Union[str, dict], path_to_schema: str):
        try:
            if isinstance(item, str):
                item = json.loads(item)
            with open(f"{Config().base_path}/{path_to_schema}") as file:
                schema = json.load(file)
            jsonschema.validate(item, schema)
            return True
        except jsonschema.exceptions.ValidationError as e:
            return f"JSON не валиден по схеме: {e}"
        except json.decoder.JSONDecodeError as e:
            return f"JSON сформирован некорректно: {e}"

    def validate_items(self, items_dict: dict, path_to_schema: str):
        res_set = {True}
        for item in items_dict:
            res_set.add(self.validate_json(item, path_to_schema))
        return res_set
