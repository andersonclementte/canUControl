from math import *
from server_base import Server

dt = 0.06;

def l1l1(x, y, u):
	return [-5.2*x + 2.5*y + 3.2*u, -9*x - 0.8*y + 5.0*u]
def l1l2(x, y, u):
	return [5.0*y, -0.9*y -9.0*x + 5*u]
def l1l3(x, y, u):
	return [2.0*y - 1.2*x, -0.4*y + 3.6*x - 5*u]
def l1l4(x, y, u):
	return [1.0*x - 0.4*y + 0.6*u, 1.8*x + 0.2*y - 5.0*u]

def l2l1(x, y, u):
	return [3*y + u, -3*sin(8*x) - y]
def l2l2(x, y, u):
	tn = atan(4*x)
	return [2*y - 2*x + tn + 2*u, 2*x - 2*y]
def l2l3(x, y, u):
	3*x*(0.5*x + 1.5*y) + 2.0*u, 3*(x-y) + u*u
def l2l4(x, y, u):
	-(x-0.7)*(x+0.7)/0.1 + 5.0*u, -y + 2*u

setValMax = 1.0

class Control:

	mathMatrix = [[l1l1, l1l2, l1l3, l1l4],
			[l2l1, l2l2, l2l3, l2l4] 
			]

	def __init__(self, verbose = False):

		self.verbose = verbose
		self.time = 0.0

	def control(self, received):
		#Received possui os parametros: x, y da posição
		#o mapa e o level para retornar a função de controle da matriz math
		#e as posições x, y do alvo
		x = received[3]
		y = received[4]
		stateFunction = self.mathMatrix[received[1]][received[2]]
		targerX = received[5]
		targerY = received[6]

		controlSignal = 0.0
		dMin = 100000000.0
		for ut1 = -setValMax; ut1 < setValMax; ut1 += 0.1:
			for ut2 = -setValMax; ut2 < setValMax; ut2 += 0.1:
				#TODO position = predictPosition(x, y, ut1, ut2, stateFunction, 100, 0.1) 
				#TODO distance = calculateClosest(targerX, targerY, position)
				pass
		pass

	def step(self, received):

		print(received)

		controlSignal = sin(self.time)

		self.time += dt

		return controlSignal


if __name__=='__main__':

	control = Control()

	server = Server(control)

	server.run()








