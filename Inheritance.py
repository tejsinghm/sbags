# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:56:42 2022

@author: HP
"""

# Concept of Private & Public: In python we just _ to keep private
# Concept of Inheritance
# class user():
#    de sign_in(self):
#     print(" logged in")
    
# class Wizard(user):
#   def __init__(self ,name,sex):
#    self.name=name
#    self.power=sex
#   def attack(self):
#     print(f' attacking with the power of  {self.power}')
# class archer(user):
#   def __init__(self,name,num_arrows):
#    self.name=name
#    self.num_arrows=num_arrows
   
#   def attack(self):
#     print(f' attacking with the arrows: arrows left-  {self.num_arrows}')
    
# Wizard1=Wizard('Merlin', 50)
# archer1=archer('Robin',100)
# Wizard1.attack()
# archer1.attack()
# # print(Wizard1)
# wizard2=Wizard('Merlin', 'M')
# print(isinstance(wizard2,Wizard ))
# print(isinstance(wizard2,user))
# #PLOYMORPHISM
# for char in [Wizard, archer]:
#     print(Wizard1.attack())
# # print(wizard1.sign_in())

class A:
   num=10
   # pass
   
class B(A):
    num=3
    
    # pass
class C(A):
    num=1
    # pass
class D(B,C):

    pass

printee(D.num)
print(D.mro())
dffdfdfdfdfdf







