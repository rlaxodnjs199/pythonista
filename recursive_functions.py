from collections.abc import MutableMapping

# Flatten a dictionary in Python
INPUT = {"a": 1, "c": {"a": 2, "b": {"x": 3, "y": 4, "z": 5}}, "d": [6, 7, 8]}


def flatten_dict(
    d: MutableMapping, parent_key: str = "", separator: str = "."
) -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + separator + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, separator).items())
        else:
            items.append((new_key, v))
    return dict(items)



if __name__ == "__main__":
    print(flatten_dict(INPUT))

# Comments
# MutableMapping : abstract class to determine dictionary objects
# isistance(v, MutableMapping) to check if v is dictionary
# dictionary.items() -> [(), ()] : array of tuples
# list.append() vs list.extend() : When add only one element -> use append(), when add more than one elements -> use extend()
