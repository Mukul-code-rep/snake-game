import turtle as t

start_pos = 0
move_dis = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    def __init__(self):
        self.turtles = []
        self.create()
        self.head = self.turtles[0]

    def create(self):
        for i in range(3):
            self.new_seg()
            self.turtles[i].goto(start_pos - i * 20, 0)

    def new_seg(self):
        new = t.Turtle(shape='square')
        new.color('white')
        new.penup()
        self.turtles.append(new)

    def extend(self):
        target_pos = self.turtles[-1].pos()
        self.new_seg()
        self.turtles[-1].goto(target_pos)

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].pos())
        self.head.fd(move_dis)

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)