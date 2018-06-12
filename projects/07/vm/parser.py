import sys
import code

class Parser(object):

	def __init__(self):
		self.name = "parser"

	def read_in(self):
		f = open(sys.argv[1],"r")
		contents = f.readlines()
		f.closed
		contents_trimmed = [];
		for line in contents:
			line = line.partition('//')[0]
	        	line = line.rstrip()
	        	line = line.replace(" ", "")
	        	if len(line) != 0:
	        		contents_trimmed.append(line)
	    	return contents_trimmed

	def arithmetic_check(self, text):
		arithmetic_words = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]
		for word in arithmetic_words:
			if word in text:
				return True

	def memory_segment(self, text):
		segment = ["local", "this", "that", "argument", "temp", "static", "constant", "pointer"]
		for word in segment:
			if word in text:
				return word


	def command_type(self, text):
		if "push" in text:
			return "C_PUSH"
		elif "pop" in text:
			return "C_POP"
		elif self.arithmetic_check(text):
			return "C_ARITHMETIC"
		else:
			print "Invalid Command"


	def parse(self):
		trimmed = self.read_in()
		c = code.Code()
		for line in trimmed:
			command = self.command_type(line)
			if command == "C_PUSH":
				arg1 = self.memory_segment(line)
				arg2 = line.split(arg1,1)[1]
				c.push(arg1, arg2)
			elif command == "C_POP":
				arg1 = self.memory_segment(line)
				arg2 = line.split(arg1,1)[1]
			elif command == "C_ARITHMETIC":
				specific = line



	






