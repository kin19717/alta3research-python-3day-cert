#!/usr/bin/env python3
"""Altas Certification
    Reading a personalinfo.txt and store in a list and output the statement"""
import os, sys
import io

# A class to specific personal info
class Person:
    #constructor
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    #output function
    def myfunc(abc):
      print(f"Hello my name is {abc.name}. I am {abc.age} years old. My weight is {abc.weight} and {abc.height}ft tall")


#main function
def main():
    persons = []
    #read a txt file
    with open("personinfo.txt", "r") as file:
        data = [x.rstrip('\n').split(" ") for x in file.readlines() ]
        persons.append(data) #store in the list
        name= persons[0][0][0] #define name in the position of the arraylist
        year= persons[0][0][1] #define year in the position of the arraylist
        weight= persons[0][0][2] #define weight in the position of the arraylist
        height= persons[0][0][3] #define height in the position of the arraylist
        p1 =Person(name, year, weight, height) #define value be store using Class
        p1.myfunc() #call myfunc to outout the print statement 

        name= persons[0][1][0] #define name in the position of the arraylist
        year= persons[0][1][1] #define year in the position of the arraylist
        weight= persons[0][1][2] #define weight in the position of the arraylist
        height= persons[0][1][3] #define height in the position of the arraylist
        p1 =Person(name, year, weight, height) #define value be store using Class
        p1.myfunc() #call myfunc to outout the print statement
if __name__ == "__main__":
    main()



