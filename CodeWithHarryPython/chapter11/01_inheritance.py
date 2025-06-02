class Parent:
    def responsibility(self):
        print(f"Parent responsibility is take care of {self.name} because {self.name} is the child")

class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")

a=Child()
a.name="Darshan"
a.responsibility()
a.play()