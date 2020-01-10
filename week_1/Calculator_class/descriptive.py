#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math

class Calculator:
    def __init__(self, data):
        new_d = data.sort()
        if (data == None):
            print("no data")
            pass
        self = self
        self.data = data
        self.data.sort()
        self.length = len(self.data)
        self.mean = sum(self.data) / self.length
#
#if self.length % 2 == 0:
#    median1 = self.data[self.length//2 - 1]
#    median2 = self.data[self.length//2]
#    self.median = (median1+median2) / 2
# else
#   self.median = self.data[(self.length-1)//2]
#
        if (self.length % 2 == 1): #is odd
            print(self.length)
            self.median = self.data[int((self.length - 1) /2)] #number in the middle
        else: #is even
            num1 = self.data[self.length // 2]
            num2 = self.data[(self.length // 2) - 1]
            self.median = (num1 + num2) / 2
        self.variance = (sum([(x - self.mean)**2 for x in data])) / (self.length)
        self.stand_dev = round(math.sqrt((sum([(x - self.mean)**2 for x in self.data])) / (self.length - 1)), 5)
    #given a list, return the number in the middle
    def median(self):
        self.data.sort()
        if self.length % 2: #is odd 0 is false
            self.median = data[(self.length - 1) /2] #number in the middle
        else: #is even
            self.median = (data[self.length / 2] + data[int((self.length / 2)) - 1]) / 2
    #given:value, list of values
    #extend the data attribute
    #no return
    def add_data(self, new_data):
        [self.data.append(nd) for nd in new_data]
        #self.data.extend(new_data)
        self.update(self.data)
    def variance(self):
        self.variance = (sum([(x - self.mean)**2 for x in self.data])) / (self.length)
    def stand_dev(self):
        self.stand_dev = (self.variance)**(1/2)
#updates internal variables after add/remove data
#length, mean, median, variance, stand_dev,
    def update(self, data):
        self.data = data
        self.data.sort()
        self.length = len(self.data)
        self.mean = sum(self.data) / self.length
        if (self.length % 2 == 1): #is odd
            print(self.length)
            self.median = self.data[int((self.length - 1) /2)] #number in the middle
        else: #is even
            num1 = self.data[self.length // 2]
            num2 = self.data[(self.length // 2) - 1]
            self.median = (num1 + num2) / 2
        self.variance = (sum([(x - self.mean)**2 for x in data])) / (self.length)
        self.stand_dev = round(math.sqrt((sum([(x - self.mean)**2 for x in self.data])) / (self.length - 1)), 5)

    #accept a list of numbers
    #remove any of the number in that list from your object data
    #return nothing
    def remove_data(self, trash):
        for element in trash:
            self.data.remove(element)
        self.update(self.data)
    def print_data(self):
        print(self.data)

    #def variance(self, data):
    #      return (sum([(x - self.mean)**2 for x in data])) / self.length
    #def stand_dev(self, data):
    #      return (variance(self, data))**(1/2)
