class Parent:

    def last_name(self):
        print("Parent Class: R.K.Agnihotri")

class Child(Parent):

    def first_name(self):
        print("Child Class: Pratyush & Utkarsh")

    def last_name(self):
        print("Child Class: Agnihotri")

pratyush = Child()
pratyush.first_name()
pratyush.last_name()