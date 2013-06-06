class DirectAttr:
    """A model attribute that comes straight from the API."""
    def __init__(self, local_name, api_name, local_type, api_type):
        """Initializes the DirectAttr instance.

           `local_name`: The name we'll use for the attribute locally (e.g. "label" or
               "requires_pvops")
           `api_name`: The used by the API for the attribute (e.g. u"LABEL" or u"REQUIRESPVOPS")
           `local_type`: The type of object we'll use locally for the attribute (e.g. `bool` or
               `FooObject`)
           `api_type`: The type of object the API expects for the attribute (e.g. `int` or
               `unicode`)"""
        self.local_name = local_name
        self.api_name = api_name
        self.local_type = local_type
        self.api_type = api_type


class LinkedAttr:
    """A model attribute that corresponds to another object in the API."""


class Model:
    direct_attrs = []
    linked_attrs = []

    @classmethod
    def from_api_dict(cls, api_dict):
        """Factory method that instantiates Model subclasses from API-returned dicts."""
        inst = cls()
        for attr in cls.direct_attrs:
            try:
                api_value = api_dict[attr.api_name]
            except KeyError:
                raise KeyError("API did not return required '%s' value for '%s' object" %
                               (attr.api_name, cls.__name__))
            setattr(inst, attr.local_name, attr.local_type(api_value))
        return inst
