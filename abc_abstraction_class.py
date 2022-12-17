# import ABC == Abstraction Base Class
# if class has one or more abstraction method, we can call it abstract class
# abc module provides infrastructure for defining custon abstruction classes
# ou can add @abstractmethod decorator to make methods abstract
# ABCMeta class is a meta-class used to define ABC

from abc import ABCMeta, abstractclassmethod

class Building_Skeleton(metaclass = ABCMeta) :
    # note : we are constructing a class that inherit from ABCmeta class to define abstraction classes and methods
    # abstraction methods are just a function title or method without body, body will be defined in the inherited classes.
    # note, we use @abstractionmethods with every method inside the class base

    @abstractclassmethod
    def useConcrete(self):
        pass

    @abstractclassmethod
    def useSteel(self):
        pass

    def this_is_not_abstract(self):
        print(f"this is not abstract, so any class that inherits from me, will not be obligated to use it.")


class Hospital(Building_Skeleton) :
    # now, we've made a class that inherits from class base (Building_Skeleton)

    def useConcrete(self):
        print(f"now, you can use a method with body full of concrete :)")

class Stadium(Hospital):
    
    def useSteel(self):
        print(f"now, you can use abstraction method with a body that inherits from Hospital which eventually inherits from Building_Skeleton")


# let's take an instance from each class :

# building_one = Building_Skeleton()

# building_one.useConcrete()
#TypeError: Can't instantiate abstract class Building_Skeleton with abstract methods useConcrete, useSteel
# means you can't use .useConcrete() because it has no body, it's just a title

building_two = Stadium()
building_two.useConcrete()
building_two.useSteel()
