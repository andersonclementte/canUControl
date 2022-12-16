from math import *
from server_base import Server

dt = 0.06;

class Control:

	def __init__(self, verbose = False):

		self.verbose = verbose
		self.time = 0.0
	

	def step(self, received):


		controlSignal = 0
		print(received)
		for a in range(len(received)):
			if received[1] == 1.0:
				if received[2] == 1.0:
					controlSignal = sin(2*self.time)
				if received[2] == 2.0:
					controlSignal = sin(self.time)
				if received[2] == 3.0:
					controlSignal = 1.5*sin(5*self.time)
					if received[4] < -0.50:
						controlSignal = -0.9
					if received[4] > 0.50:
						controlSignal = 0.9
				if received[2] == 4.0:
					controlSignal = sin(20*self.time)
					if received[4] < -0.50:
						controlSignal = -0.9
					if received[4] > 0.50:
						controlSignal = 0.9
			if received[1] == 2.0:
				if received[2] == 1.0:
					controlSignal = sin(self.time)
				if received[2] == 2.0:
					controlSignal = sin(10*self.time)
					if received[4] < -0.55:
						controlSignal = 0.9
					if received[4] > 0.55:
						controlSignal = -0.9
				if received[2] == 3.0:
					controlSignal = 0.1*sin(self.time) - 0.2
				if received[2] == 4.0:
					controlSignal = 2*sin(5*self.time)
		self.time += dt

		return controlSignal
	

if __name__=='__main__':

	control = Control()

	server = Server(control)

	server.run()








