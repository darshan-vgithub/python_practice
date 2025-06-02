class Parent1:
    def responsibility(self):
        print(f"Parent1 responsibility of parent1 of {self.name} is to take care of {self.name} because {self.name} is the child")


class Parent2:
    def extraresponsibility(self):
        print(f"Parent2 responsibility of parent2 of {self.name} is to take care of {self.name} because {self.name} is the child and also take care of the education in {self.school}")

class Child(Parent1,Parent2):
    def play(self):
        print(f"{self.name} is playing")


a=Child()
a.name="Darshan"
a.school="University od Standford"
a.responsibility()
a.extraresponsibility()
a.play()