def dict_to_string(d):
    return ', '.join(f"{k}:{v}" for k, v in d.items())
d = {'a': 1, 'b': 2}
print(dict_to_string
