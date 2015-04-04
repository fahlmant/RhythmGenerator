
class Measures:
    total_beats = 0
    notes = [Elements() for i in range (total_beats)]
    def __init__(self, beats):
        self.notes = []
        self.total_beats = beats
    def add_element(Element):
        notes += Element
        if (total_beats > 0):
            total_beats -= Element.length

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
    length = 0;

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

def main():
    run()

if __name__ == "__main__": main()
