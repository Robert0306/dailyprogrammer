# challenge #342 major scales.


solfegDict = {"Do": 0, "Re": 2, "Mi": 4, "Fa": 5, "So": 7, "La": 9, "Ti": 11}
noteList = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"
            , "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def majorScale(scale, solfeg):
    return noteList[(noteList.index(scale) + solfegDict[solfeg])]


print(majorScale("C", "Re"))
print(majorScale("C", "So"))
print(majorScale("E", "Re"))
