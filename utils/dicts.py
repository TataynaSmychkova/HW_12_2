def get_val(collection, key, default='git'):
    if isinstance(collection, dict):
        if key in collection.keys():
            return collection[key]
        return default
    return "Не верные данные"

