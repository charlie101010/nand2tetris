import sys
import code
import re

class Parser(object):

	def __init__(self, name):
		self.name = name

#read in the vm code from file
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
	        print contents_trimmed
	    	return contents_trimmed

#check to see if the current vm command is an arithmetic one
	def arithmetic_check(self, text):
		arithmetic_words = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]
		for word in arithmetic_words:
			if word in text:
				return True

#if the vm command is push or pop, determine which memory segment should be accessed
	def memory_segment(self, text):
		segment = ["local", "this", "that", "argument", "temp", "static",  "pointer", "constant"]
		for word in segment:
			if word in text:
				return word

#determine the command type of the current vm line
	def command_type(self, text):
		if "push" in text:
			return "C_PUSH"
		elif "pop" in text:
			return "C_POP"
		elif "call" in text:
			return "CALL"
		elif "function" in text:
			return "FUNC"
		elif self.arithmetic_check(text):
			return "C_ARITHMETIC"
		elif "if-goto" in text:
			return "IF"
		elif "goto" in text:
			return "GO"
		elif "label" in text:
			return "LABEL"
		elif "return" in text:
			return "RET"
		else:
			print "Invalid Command"


#iterate through each vm command and pass it to the methods from the codewriter class to translate and write to file
	def parse(self):
		trimmed = self.read_in()
		c = code.Code()
		for line in trimmed:
			command = self.command_type(line)
			if command == "C_PUSH":	
				arg1 = self.memory_segment(line)
				arg2 = line.split(arg1,1)[1]
				c.push(arg1, arg2, self.name)	
			elif command == "C_POP":
				arg1 = self.memory_segment(line)
				arg2 = line.split(arg1,1)[1]
				c.pop(arg1, arg2, self.name)
			elif command == "C_ARITHMETIC":
				c.arithmetic(line, self.name)
			elif command == "GO":
				arg1 = line.split("goto",1)[1]
				c.goto(arg1, self.name)
			elif command == "IF":
				arg1 = line.split("if-goto",1)[1]
				c.ifgoto(arg1, self.name)
			elif command == "LABEL":
				arg1 = line.split("label",1)[1]
				c.label(arg1, self.name)
			elif command == "FUNC":
				match = re.search('\d', line)
				ind = match.start()
				nVars = line[-1:]
				functionName = line.split("function",1)[1][:-1]
				# className = arg1.split(".",1)[0]
				# arg2 = arg1.split(".",1)[1]
				# functionName = arg2[:-1]
				print functionName
				c.func(functionName, nVars, self.name)
			elif command == "CALL":
				match = re.search('\d', line)
				ind = match.start()
				nArgs = line[-1:]
				functionName = line.split("call",1)[1][:-1]
				# className = arg1.split(".",1)[0]
				# arg2 = arg1.split(".",1)[1]
				# functionName = arg2[:-1]
				print functionName
				c.call(functionName, nArgs, self.name)
			elif command == "RET":
				c.ret(self.name)


	



	






