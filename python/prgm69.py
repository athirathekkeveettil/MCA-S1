# create a class time with private attributes hour,mintues,seconds overloaded '+' operator to find sum of 2 time

class Time:
    def __init__(self,h=0,m=0,s=0):
        self.__hour=h
        self.__minutes=m
        self.__seconds=s
    def __add__(self,other):
        total_seconds_self=self.__hour*3600+self.__minutes*60+self.__seconds
        total_seconds_other=other.__hour*3600+other.__minutes*60+other.__seconds
        total_seconds=total_seconds_self+ total_seconds_other
        remaining

        
