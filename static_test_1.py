import os, sys

def Add_numbers(a, b, c=5):
  result = a + b + c
  print("The result is: %d" % result)
  return  # 명시적 리턴값 없음

class person:
  def __init__(self, name, age):
    self.Name = name
    self.age = age

  def greet(self):  # 사용되지 않음
        print("Hello my name is", self.Name)

x = Add_numbers(1, 2)

if x == None:  # is None 권장
  print("No return value")

someList = [1,2,3]
print(someList[5])

def divide(x, y):
    return x / y

divide("100", 5)
