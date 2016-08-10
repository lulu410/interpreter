#use a stack
class Interpreter:
	def __init__(self):
		self.stack = []
	
	def LOAD_VALUE(self,number):
		self.stack.append(number)

	def PRINT_ANSWER(self):
		answer = self.stack.pop()
		print answer

	def ADD_TWO_VALUES(self):
		num1 = self.stack.pop()
		num2 = self.stack.pop()
		answer = num1+num2
		self.stack.append(answer)

	def run(self,what_to_execute):
		instructions = what_to_execute["instructions"]
		numbers = what_to_execute["numbers"]
		for instr, arg in instructions:
			if instr == "LOAD_VALUE":
				num = numbers[arg]
				self.LOAD_VALUE(num)
			elif instr == "ADD_TWO_VALUES":
				self.ADD_TWO_VALUES()
			elif instr == "PRINT_ANSWER":
				self.PRINT_ANSWER()

what_to_execute = {
	"instructions": [("LOAD_VALUE", 0),  # the first number
					 ("LOAD_VALUE", 1),  # the second number
					 ("ADD_TWO_VALUES", None),
			         ("PRINT_ANSWER", None)],
	"numbers": [7, 5] }

interpreter = Interpreter()
interpreter.run(what_to_execute)
