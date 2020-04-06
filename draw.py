import curses

class draw:
    sh = sw = w = None
    def __init__(self, _w, _sh, _sw):
        self.w = _w
        self.sh = _sh
        self.sw = _sw
        
    def display(self, coords, char):
        for pos in coords:
            self.w.addch(coords[0], coords[1], char)

    def clear(self):
        for y in range(1, self.sh):
            for x in range(1, self.sw - 1):
                self.w.addch(y, x, ' ')

    def type(self, start, message):
        self.w.addstr(start[0], start[1], message)
