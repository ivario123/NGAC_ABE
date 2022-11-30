"""
    NGAC attribute abstraction class

    This class is used to implement attributes
"""


from .ngac_object import NgacObject


class Attribute(NgacObject):
    """
    NGAC attribute abstraction class

    This class is only for typing.
    """

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return self.__str__()

    def get_attribute(self) -> str:
        return self.__str__()

    def __eq__(self, __o: "Attribute") -> bool:
        return self.__str__() == __o.__str__()  # They are just string wrappers

    def __hash__(self) -> int:
        return hash(self.__str__())


class ObjectAttribute(Attribute):
    """
    ObjectAttribute abstraction

    Serves typing purposes
    """

    def __init__(self, object_attribute: str):
        # super.__init__(obj_attr)
        self.object_attribute = object_attribute

    def __str__(self) -> str:
        return self.object_attribute


class UserAttribute(Attribute):
    """
    UserAttribute abstraction

    Serves typing purposes
    """

    def __init__(self, user_attr: str):
        #
        if (type(user_attr) == list and len(user_attr) == 1) or type(user_attr) not in [
            str,
            list,
        ]:
            raise TypeError
        elif type(user_attr) == list:
            self.user_attr = user_attr[0]
        else:
            self.user_attr = user_attr

    # self.user_attr = user_attr

    def __str__(self) -> str:
        return self.user_attr


def test_ngac_attribute():
    """
    Test attribute class
    """
    attr = ObjectAttribute("SomeAttribute")
    assert attr.get_attribute() == "SomeAttribute"

    attr2 = UserAttribute("SomeAttribute")
    assert attr2.get_attribute() == "SomeAttribute"

    assert attr == attr2


def test_attr_repr():
    """
    Test attribute class
    """
    attr = ObjectAttribute("SomeAttribute")
    assert attr.__repr__() == "SomeAttribute"

    attr2 = UserAttribute("SomeAttribute")
    assert attr2.__repr__() == "SomeAttribute"

    assert attr == attr2
    assert attr.__hash__() == attr2.__hash__()
    assert attr.__str__() == attr2.__str__()
