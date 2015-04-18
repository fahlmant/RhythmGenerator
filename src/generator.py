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
        total_beat_copy = self.total_beats
        if (total_beat_copy - Element.length >= 0):
            self.total_beats -= Element.length
            self.notes.append(Element)


# Element class, has a type and length
class Element(object):

    type = 'Element'
    length = 0

    def __init__(self, type, length):
        self.type = type
        self.length = length


def get_length(length):

    if(length is 16):
        return 1
    elif(length is 8):
        return 2
    elif(length is 4):
        return 4
    elif(length is 2):
        return 8
    elif(length is 1):
        return 16


def run(measure_list):

    for m in measure_list:
        for j in range(m.total_beats):
            index = random.randint(0, 4)
            type_selector = random.randint(0, 10)
            if(type_selector >= 8):
                type_selector = 1
            else:
                type_selector = 0
            element_value = element_lengths[index]
            element_type = element_types[type_selector]
            element = Element(element_type, element_value)
            m.add_element(element)

    print_generation(measure_list)
    convert_to_lilypond(measure_list)


def print_generation(measure_list):

    for m in measure_list:
        print('|', end='')
        for n in m.notes:
            print(str(n.type) + str(n.length))
        print('|')


def convert_to_lilypond(measure_list):

    file = open("something.ly", "w+")
    file.write("\\version \"2.18.2\"\n\\relative f' {")
    for line in file:
        print(line)
    for m in measure_list:
        for j in range(len(m.notes)):
            element_length = get_length(m.notes[j].length)
            if (m.notes[j].type is "Note"):
                file.write("f" + str(element_length) + " ")
            else:
                file.write("r" + str(element_length) + " ")
    file.write("}")


def main():

    random.seed()
    measure_list = []
    for i in range(0, 8):
        m = Measure(16)
        measure_list.append(m)
    run(measure_list)


if __name__ == "__main__":
    main()
