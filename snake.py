import curses
class snake:
    sh = sw = snk_x = snk_y = size = 0
    snake_arr = [[0, 0]]
    w = screen = None

    def __init__(self, args): #w, sh, sw, screen
        self.w, self.sh, self.sw = args
        self.snk_x = args[2]/4            #snk_x is 1/4 of the s width.
        self.snk_y = args[1]/2            #snk_y is half of the s height.
        self.snake_arr = [
            [self.snk_y, self.snk_x],
            [self.snk_y, self.snk_x-1],
            [self.snk_y, self.snk_x-2]
        ]
        self.size = 3
        
    def feed(self):
        self.size += 1
        
    #     2
    #  1      3
    #     0
    #returns -1 if game over, otherwise returns array of segment coordinates
    def move(self, direction):
        new_head = [self.snake_arr[0][0], self.snake_arr[0][1]]
        if direction == 0:
           new_head[0] += 1
        elif direction == 1:
            new_head[1] -= 2
        elif direction == 2:
            new_head[0] -= 1
        else:
            new_head[1] += 2

        if new_head[0] in [0, self.sh] or new_head[1] in [0, self.sw] or new_head in self.snake_arr[1:]:
            return -1
        self.snake_arr.insert(0, new_head)
        if(len(self.snake_arr) > self.size):
            tail = self.snake_arr.pop()
            self.w.addch(int(tail[0]), int(tail[1]), ' ')
        return self.snake_arr
    
    

