import random

beats = 16
note_list = []
beat_list = [16, 8, 4, 2, 1, 16, 8, 4, 2, 1]
measure = []
note_value = ['Whole Note', 'Half Note', 'Quarter Note', 'Eighth Note', 'Sixteenth Note', 'Whole Rest', 'Half Rest', 'Quarter Rest', 'Eighth Rest', 'Sixteenth Rest']
for x in range (0, 10):
    note_list.append(x)

random.seed()

while beats > 0:
    beat_test = beats
    num = random.randint(0,9)
    if(beat_test - beat_list[num] >= 0):
        measure.append(note_list[num])
        beats -= beat_list[num]

notes = len(measure)
for x in range(0, notes):
    print(note_value[measure[x]])


