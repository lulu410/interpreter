class VirtualMachineError(Exception):
	pass

class VirtualMachine(object):
	def __init__(self):
		self.frames = []
		self.frame = None
		self.return_value = None
		self.last_exception = None

	def run(self, code, global_names=None, local_names=None):
		frame = self.make_frame(code, global_names=global_names, 
								local_names=local_names)

	def make_frame(self, code, callargs={}, global_names=None, local_names=None)


class Frame(object):
	def __init__(self, code_obj, global_names, local_names, prev_frame):
		self.code_obj = code_obj
		self.global_names = global_names
		self.local_names = local_names
		self.prev_frame = prev_frame
		self.stack = []
		if prev_frame:
			self.builtin_names = prev_frame.builtin_names
		else:
			self.builtin_names = local_names['__builtins__']
			if hasattr(self.builtin_names, '__dict__'):
				self.builtin_names = self.builtin_names.__dict__

		self.last_exception = 0
		self.block_stack = []