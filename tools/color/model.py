
class ColorCell:
    def __init__(self, col, idx, fill, width, height, text, textColor):
        self.col = col
        self.idx = idx
        self.fill = fill
        self.width = width
        self.height = height
        self.text = text
        self.textColor = textColor

class ColorRow:
    def __init__(self, row):
        self.row = row
        self.cell = []
        self.height = 0
        self.width = 0

class ColorGrp:
    def __init__(self, name):
        self.name = name
        self.row = []
        self.width = 0
        self.height = 0


class ColorSet:
    def __init__(self, name) :
        self.name = name
        self.width = 0
        self.height = 0
        self.grp = []



