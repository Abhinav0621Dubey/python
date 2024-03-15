class person:
    def __init__(self,n,a):
        self.name = n
        self.age_group = a

    def info(self):
        print(f"your name is {self.name} and your age group is {self.age_group} ")

player1 = person("ravi",21)
player2 = person("raj",19)

player1.info()
player2.info()