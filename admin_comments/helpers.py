from importlib import import_module


def get_class_from_str(name):
    components = name.split('.')
    return getattr(import_module(".".join(components[:-1])), components[-1])


__all__ = ['get_class_from_str']
