class Grandparent:
    def property(self):
        print("Parent property")     
class Parent(Grandparent):
    def business(self):
        print("Businees")
class child(Parent):
    def education(self):
        print("Education")
c=child()
c.property()
c.business()
c.education()