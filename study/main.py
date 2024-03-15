# //Hierarchical Inherihance//


class Grandpa:
    def __init__(self,dob,Bloodgrp):
        self.dob  = dob
        self.Bloodgrp = Bloodgrp

    def info(self):
        print(f"the date of birth of Grandpa is {self.dob}and his blood group is {self.Bloodgrp}")

class Dad (Grandpa):
    def __init__(self,dob,Bloodgrp,work):
        super().__init__(dob,Bloodgrp)
        self.work = work

    def info(self):
        print(f"the date of birth of dad is {self.dob}and his blood group is {self.Bloodgrp} and he is a {self.work}")
 
class Grandma(Grandpa):
    def __init__(self,dob,Bloodgrp,birthplace):
        super().__init__(dob,Bloodgrp)
        self.birthplace = birthplace

    def info(self):
        print(f"the date of birth of Grandma is {self.dob}and his blood group is {self.Bloodgrp} and she belongs to {self.birthplace}")

class son(Dad):
    def __init__(self,dob,Bloodgrp,work,education):
        super().__init__(dob,Bloodgrp,work)
        self.educaton = education

    def info(self):
        print(f"my date of birth  is {self.dob}and my  blood group is {self.Bloodgrp} and i have done my {self.educaton}")


class sister(Dad):
    def __init__(self,dob,Bloodgrp,work,SclName):
        super().__init__(dob,Bloodgrp,work)
        self.SclName  =  SclName

    def info(self):
        print(f"the date of birth of sisterf is {self.dob}and her blood group is {self.Bloodgrp} and she studies in  {self.SclName} school")


g = Grandpa("1947","o+")
g.info()

d = Dad("1969","o+","Engineer")
d.info()

gm = Grandma("1950","a+","Jaipur")
gm.info()

s = son ("2001","o-","student","B.Tech")
s.info()

sis = sister("2003","b+","student","DPHS")
sis.info()


