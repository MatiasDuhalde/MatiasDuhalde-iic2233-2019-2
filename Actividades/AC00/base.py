# Seccion para importar liberías
import math

# Snippet obtenido de StackOverflow, para ignorar el error de las funciones 
# trigonométricas de la librería math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper
# Fuente: https://stackoverflow.com/questions/8595973/truncate-to-three-decimals-in-python/8595991

def calcDistancia(p1, p2):
	return math.sqrt(sum([(p2[i]-p1[i])**2 for i in range(2)]))

def calcAngulo(p1,p2,p3):
	"""Angulo entre dos puntos con vértice en p1."""
	p12 = calcDistancia(p1,p2)
	p13 = calcDistancia(p1,p3) 
	p23 = calcDistancia(p2,p3) 
	# Ley de los cosenos
	return math.acos((p12**2+p13**2-p23**2)/(2*p12*p13))

class Cuadrado(object):
	
	"""Recibe 4 puntos en forma de tupla con el formato (x, y). Estos puntos 
	deben estar ordenados contra las manecillas del reloj.
	"""

	def __init__(self, *args):
		self.puntos = [*args]
		self.p1, self.p2, self.p3, self.p4 = self.puntos
		if not self.es_cuadrado():
			raise ValueError("No es cuadrado")


	def es_cuadrado(self):
		for i in range(1,5):
			if truncate(calcAngulo(self.puntos[i%4], self.puntos[(i+1)%4], 
			self.puntos[(i-1)%4]), 6) != truncate(math.pi/2,6):
				return False
		return True
	
	def obtener_area(self):
		return calcDistancia(self.p1, self.p2)**2
		
	def obtener_perimetro(self):
		return calcDistancia(self.p1, self.p2)*4
		
	def __str__(self):
		return "{:10} {}\n{:10} {}\n{:10} {}".format("Tipo:", "Cuadrado", 
	"Area:", str(self.obtener_area()), "Perimetro:", 
	str(self.obtener_perimetro()))


class Triangulo(object):
	def __init__(self, *args):
		self.p1, self.p2, self.p3 = args
		
	def obtener_area(self):
		pass
		
	def obtener_perimetro(self):
		pass
		
	def es_equilatero(self):
		pass
		
	def __str__(self):
		return """ this """


if __name__ == '__main__':
	q = Cuadrado((0,0), (0,2), (2,2), (2,0))
	print(q)
	