import tkinter
from PIL import  Image, ImageTk   # conda install pillow
import math
from random import randint


class Snake(tkinter.Canvas):
	def __init__(self):
		super().__init__(height=630, width=620, background="black", highlightthickness=0)
		self.score = 0
		self.snake_position = [(160,300),(140,300),(120,300),(100,300), (80,300), (60,300), (40,300)]
		self.food_position = self.start_food_again()

		self.direction = 'Right'
		self.bind_all("<Key>", self.on_key_press)

		try:
			self.snake_img = Image.open('./images/snake.png')
			self.snake_body = ImageTk.PhotoImage(self.snake_img)
			self.food_img = Image.open('./images/food.png')
			self.food = ImageTk.PhotoImage(self.food_img)
		except IOError as err:
			print(err)

		self.create_text(80, 50, text=f"Score: {self.score}", fill='#FFF', font=('TkDefaultFont', 24), tag="score")
		for x,y in self.snake_position:
			self.create_image(x, y, image=self.snake_body, tag='snake')

		self.create_image(*self.food_position, image=self.food, tag='food')

		self.after(200, self.actions) # game speed


	def move(self):
		headX, headY = self.snake_position[0]

		if self.direction == 'Left':
			new_head_pos = (headX - 20, headY)
		elif self.direction == 'Right':
			new_head_pos = (headX + 20, headY)
		elif self.direction == 'Down':
			new_head_pos = (headX, headY + 20)
		elif self.direction == 'Up':
			new_head_pos = (headX, headY - 20)

		self.snake_position = [new_head_pos] + self.snake_position[:-1]

		for s, p in zip(self.find_withtag('snake'), self.snake_position):
			self.coords(s,p)


	def actions(self):

		if self.collision_check():
			print('Game Over')
			self.create_text(300, 300, text=f"Game Over ,result: {self.score}", fill='#FFF', font=('TkDefaultFont', 24))
			return

		self.move()
		self.after(200, self.actions)
		self.food_collision_check()


	def collision_check(self):
		headX, headY = self.snake_position[0]
		return (headX, headY) in self.snake_position[1:] or headX in (0, 620) or headY in (0, 630)

	def food_collision_check(self):
		if self.snake_position[0] == self.food_position:
			self.score += 2
			self.snake_position.append(self.snake_position[-1])
			self.create_image(*self.snake_position[-1], image=self.snake_body, tag="snake")
			self.food_position = self.start_food_again()
			self.coords(self.find_withtag("food"), *self.food_position)

			score = self.find_withtag("score")
			self.itemconfigure(score, text=f"Score: {self.score}", tag="score")

	def start_food_again(self):
		while True:
			x_position = randint(2, 30)*20
			y_position = randint(2, 30)*20
			print(y_position, x_position)
			new_position = (x_position, y_position)
			return new_position


	def on_key_press(self, e):
		new_direction = e.keysym
		self.direction = new_direction
		print(self.direction)