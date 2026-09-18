import json
import re


def extract_json(text: str):

    text = text.strip()

    # remove markdown fences
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    # try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # fallback: extract first JSON object/array
    start_obj = text.find("{")
    start_arr = text.find("[")

    if start_obj == -1 and start_arr == -1:
        raise ValueError("No JSON found in LLM response")

    start = min([i for i in [start_obj, start_arr] if i != -1])

    end = max(text.rfind("}"), text.rfind("]")) + 1

    return json.loads(text[start:end])