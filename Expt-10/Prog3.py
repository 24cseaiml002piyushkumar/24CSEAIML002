class father:
    def skill(self):
        print("Leader")
class mother:
    def skill2(self):
        print("Cooking")
class child(father,mother):
    def skill3(self):
        print("Playing")
c=child()
c.skill()
c.skill2()
c.skill3()