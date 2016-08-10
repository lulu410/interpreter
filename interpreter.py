#use a stack
class Interpreter:
	def __init__(self):
		self.stack = []
		self.environment = {}


	def LOAD_VALUE(self, number):
		self.stack.append(number)


	def LOAD_VALUE(self,name):
		val = environment[name]
		self.stack.append(val)


	def STORE_NAME(self, name):
		val = self.stack.pop()
		self.environment[name] = val

	
	def PRINT_ANSWER(self):
		answer = self.stack.pop()
		print answer


	def ADD_TWO_VALUES(self):
		num1 = self.stack.pop()
		num2 = self.stack.pop()
		answer = num1+num2
		self.stack.append(answer)


	def parse_argument(self, instr, arg, what_to_execute):
		numbers = ["LOAD_VALUE"]
		names = ["LOAD_VALUE", "STORE_NAME"]

		if instruction in numbers:
			arg = what_to_execute["numbers"][arg]
		elif instruction in names:
			arg = what_to_execute["names"][arg]

		return arg


	def run(self,what_to_execute):
		instructions = what_to_execute["instructions"]
		for instr, arg in instructions:
			arg = self.parse_argument(instr, arg, what_to_execute)
			if instr == "LOAD_VALUE":
				self.LOAD_VALUE(num)
			elif instr == "ADD_TWO_VALUES":
				self.ADD_TWO_VALUES()
			elif instr == "PRINT_ANSWER":
				self.PRINT_ANSWER()
			elif instr == "STORE_NAME":
				self,STORE_NAME(arg)
			elif instruction == "LOAD_VALUE":
				self.LOAD_VALUE(arg)


what_to_execute = {
	"instructions": [("LOAD_VALUE", 0),  # the first number
					 ("LOAD_VALUE", 1),  # the second number
					 ("ADD_TWO_VALUES", None),
			         ("PRINT_ANSWER", None)],
	"numbers": [7, 5] }

interpreter = Interpreter()
interpreter.run(what_to_execute)
