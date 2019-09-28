def flip_dict(input_dict):
    value_set = set(input_dict.values())
    return {x: [k for k, v in input_dict.items() if v == x] for x in value_set}


print(flip_dict({"CA": "US", "NY": "US", "ON": "CA"}))
