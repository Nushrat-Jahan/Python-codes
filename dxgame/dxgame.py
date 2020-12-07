from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color, size, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, size, size, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.xspeed = random.randrange(-3,3)
        self.yspeed = -1
        self.hit_bottom = False
        self.score = 0

    def draw(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.yspeed = 3
        if pos[3] >= 400:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.xspeed = 3
        if pos[2] >= 500:
            self.xspeed = -3
        if self.hit_paddle(pos) == True:
            self.yspeed = -3
            self.xspeed = random.randrange(-3,3)
            self.score += 5

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.xspeed = 0
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.xspeed, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.xspeed = 0
        if pos[2] >= 500:
            self.xspeed = 0

    def move_left(self, evt):
        self.xspeed = -2
    def move_right(self, evt):
        self.xspeed = 2


tk = Tk()
tk.title("Ball Game")
canvas = Canvas(tk, width=500, height=400, bd=0, bg='light gray')
canvas.pack()
label = canvas.create_text(5, 5, anchor=NW, text="Score: 0")
tk.update()
paddle = Paddle(canvas, 'green')
ball = Ball(canvas, 'blue', 25, paddle)


while ball.hit_bottom == False:
    ball.draw()
    paddle.draw()
    canvas.itemconfig(label, text="Score: "+str(ball.score))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.015)


go_label = canvas.create_text(250,200,text="GAME OVER!!",font=("Times New Roman",30))
tk.update()