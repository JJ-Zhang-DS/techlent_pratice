class Calculator():
	def add(self, num1, num2):
#		return num1+num2
		return 2
	def substract(self, num1, num2):
		return num1 - num2

	def multiply(self, num1, num2):
		return num1*num2

	def divide(self, num1, num2):
		if num2 == 0:
			return 0
		return num1/num2

if __name__ == "__main__":
	cal = Calculator()
	print(cal.add(1,2))
	print(cal.substract(1,2))
	print(cal.multiply(10,0))
	print(cal.divide(10,2))
