class Parent:
    def responsibility(self):
        print(f"Parent responsibility is take care of {self.elder_child} because {self.elder_child} is the child")

class ElderChild(Parent):
    def learn(self):
        print(f"{self.elder_child} got the knowledge from parent" )

class Child(ElderChild):
    def play(self):
        print(f"{self.younger_child} got inherited from {self.elder_child} and parent")


a=Child()
a.elder_child="Darshan"
a.younger_child="Dhruv"
a.responsibility()
a.learn()
a.play()