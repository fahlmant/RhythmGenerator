import os
import random

# Note lengths by 16th note values
element_lengths = [1, 2, 4, 8, 16]
element_types = ['Note', 'Rest']


# Measure class, holds up to total_beats beats in a list of Elements
class Measure(object):

    def __init__(self, beats):
        self.total_beats = beats
        self.notes = []

    def add_element(self, Element):
        self.notes += Element
        total_beat_copy = self.total_beats
        if (total_beat_copy - Element.length > 0):
            self.total_beats -= Element.length
            self.notes.appent(Element)


# Element class, has a type and length
class Element(object):

    type = 'Element'
    length = 0

    def __init__(self, type, length):
        self.type = type
        self.length = length



def run(*measure_list):

    for i in measure_list:
        for j in range(16):
            index = random.randint(0, 4)
            type_selector = random.randint(0, 1)
            element_value = element_lengths[index]
            element_type = element_types[type_selector]
            element = Element(element_type, element_value)
            


def print_generation():

    for i in range(8):
        # print each measure
        i += 1


def main():

    random.seed()
    measure_list = []
    for i in range(0, 8):
        m = Measure(16)
        measure_list.append(m)
    run(measure_list)


if __name__ == "__main__":
    main()
