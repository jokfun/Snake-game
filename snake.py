from random import randint

class Snake:
	def __init__(self,maxX=300,maxY=300):
		"""
			Snake Game
			Definition of :
			- the card (maxX = max width, maxY = max height)
			- the head of the snake
			- the content of the snake
			- the position of the prey
		"""
		#Map border
		self.maxX = maxX
		self.maxY = maxY

		"""
			direction :
			0 : down
			1 : left
			2 : up
			3 : right
		"""
		#Init the direction to the left
		self.direction = 1

		#Position of the head of the snake
		self.headX = int(self.maxX/2)
		self.headY = int(self.maxY/2)

		#Creation of the snake, each cursor has a part of the snake
		self.tail = [[self.headX,self.headY]]

		#Copy of the snake list but access to clues is more easily accessible
		self.dicUsed = {
			str([self.headX,self.headY]) : True
		}

		#Initial position of the prey
		self.createFood()

	def createFood(self):
		"""
			Random generation of prey coordinates
		"""
		self.foodX = randint(1,int((self.maxX-1)/10))*10
		self.foodY = randint(1,int((self.maxY-1)/10))*10
		while(str([self.foodX,self.foodY]) in self.dicUsed):
			self.foodX = randint(1,int((self.maxX-1)/10))*10
			self.foodY = randint(1,int((self.maxY-1)/10))*10

	def setDirection(self,value):
		"""
			Update the direction of the sepent
		"""
		self.direction = value

	def updateTail(self,remove=True):
		"""
			Update the head and tail of the snake
			remove==True : removes the tip of the tail
		"""

		#The new head represents the coordinates of a new iteration
		head = [self.headX,self.headY]
		#The head is inserted at the very beginning of the list
		self.tail.insert(0,head)
		self.dicUsed[str(head)] = True

		#If we have to delete the queue, we update the list and dictionary 
		#for the target element
		if remove==True:
			self.last = self.tail[-1][:]
			del self.dicUsed[str(self.last)]
			del self.tail[-1]


	def update(self):

		#Update the head of the snake
		if self.direction == 0:
			self.headY+=10
		elif self.direction == 2:
			self.headY-=10
		elif self.direction == 1:
			self.headX+=10
		else:
			self.headX-=10

		#Test the border
		if self.headX<0:
			self.headX=self.maxX
		elif self.headX==self.maxX:
			self.headX=0
		elif self.headY<0:
			self.headY=self.maxY
		elif self.headY==self.maxY:
			self.headY=0

		#Test if the snake bites himself, stop and return the score
		if str([self.headX,self.headY]) in self.dicUsed:
			return "end",len(self.tail)

		#Test if the snake eats food, then update its size
		if self.headX==self.foodX and self.headY==self.foodY:
			self.createFood()
			self.updateTail(False)
			return "eat",((self.headX,self.headY),(self.foodX,self.foodY))

		#If nothing new, just update the place of the head and the end of the tail
		else:
			self.updateTail()
			return "run",((self.last[0],self.last[1]),(self.headX,self.headY))