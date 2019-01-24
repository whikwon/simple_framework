class Registry(object):
    def __init__(self, name):
        self._name = name
        self._module_dict = dict()

    def register_module(self, mod_class):
        mod_name = mod_class.__name__
        self._module_dict[mod_name] = mod_class
        print("mod_class:", mod_class)
        print(f"{mod_name} registered")
        print("mod_class:", mod_class)
        return mod_class

print("registry initialized")
DETECTORS = Registry("detector")
