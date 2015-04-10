import os
import random


class Measures:

    def __init__(self, beats):
        self.total_beats = beats
        self.notes = [Element() for i in range(self.total_beats)]

    def add_element(self, Element):
        self.notes += Element
        if (self.total_beats > 0):
            self.total_beats -= Element.length


class Element:

    type = 'Element'
    length = 0

    def __init__(self, type, length):
        self.type = type
        self.length = length


class Note(Element):

    type = 'Note'
    length = 0


class Rest(Element):

    type = 'Rest'
    length = 0


def run():

    for i in range(8):
        for j in range(16):
            #Pick random length
            #pick note or rest
            #add to measure
            #add beat to j
            j += 1
        i+= 1


def print_generation():

    for i in range(8):
        #print each measure
        i+= 1
y7

def main():

    random.seed()
    measure_list = []
    for i in range(0, 8):
        measure_list.append('hi')
    run()


if __name__ == "__main__":
    main()
