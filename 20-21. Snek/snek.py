from turtle import Turtle

class Snek:

    def __init__(self, dlugosc=3):
        self.segmenty = []
        self.dlugosc = dlugosc
        self.create_snek()

    def create_snek(self):
        for i in range(self.dlugosc):
            self.segmenty.append(self.segment_weza((-i*20, 0)))


    def segment_weza(self, position):
        ti = Turtle(shape="square")
        ti.color("white")
        ti.penup()
        ti.goto(position)
        return ti

    def move(self, dist=20):
        for seg_num in range(len(self.segmenty) -1, 0, -1):
            new_position = self.segmenty[seg_num-1].position()
            self.segmenty[seg_num].goto(new_position)
        self.segmenty[0].forward(dist)    

    def reset_snek(self):
        for s in self.segmenty:
            s.goto(1000,1000)
        self.segmenty.clear()    
        self.create_snek()


    def extend(self):
        self.segmenty.append(self.segment_weza(self.segmenty[-1].position()))    

    def up(self):
        if self.segmenty[0].heading() != 270:
            self.segmenty[0].seth(90)

    def down(self):
         if self.segmenty[0].heading() != 90:
            self.segmenty[0].seth(270)

    def right(self):
         if self.segmenty[0].heading() != 180:
            self.segmenty[0].seth(0)

    def left(self):
         if self.segmenty[0].heading() != 0:
            self.segmenty[0].seth(180)   