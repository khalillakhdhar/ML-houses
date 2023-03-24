# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:15:20 2023

@author: khali
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")
p1=Person("Khalil",32)
p2=Person("Ali",62)

p1.say_hello()
p2.say_hello()