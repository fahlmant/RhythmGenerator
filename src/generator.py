import os
import random


class Measures(object):

    def __init__(self, beats):
        self.total_beats = beats
        self.notes = []

    def add_element(self, Element):
        self.notes += Element
        total_beat_copy = self.total_beats
        if (total_beat_copy - Element.length > 0):
            self.total_beats -= Element.length


class Element(object):

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
            # Pick random length
            # pick note or rest
            # add to measure
            # add beat to j
            j += 1
        i += 1


def print_generation():

    for i in range(8):
        # print each measure
        i += 1


def main():

    random.seed()
    measure_list = []
    m = Measures(16)
    for i in range(0, 8):
        measure_list.append(m)


if __name__ == "__main__":
    main()
