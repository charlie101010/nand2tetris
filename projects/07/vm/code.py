import sys


class Code(object):

	def __init__(self):
		self.name = "code"

	def push(self, arg1, arg2):
		if arg1 == "local":
			 self.four_segments_push("LCL", arg1, arg2)
		elif arg1 == "this":
			 self.four_segments_push("THIS", arg1, arg2)
		elif arg1 == "that":
			 self.four_segments_push("THAT", arg1, arg2)
		elif arg1 == "argument":
			 self.four_segments_push("ARG", arg1, arg2)
		elif arg1 == "temp":
			 self.four_segments_push("TEMP", arg1, arg2)
		elif arg1 == "constant":
			 self.four_segments_push("CONST", arg1, arg2)
			
	def pop(self, arg1, arg2):
		if arg1 == "local":
			 self.four_segments_pop("LCL", arg1, arg2)
		elif arg1 == "this":
			 self.four_segments_pop("THIS", arg1, arg2)
		elif arg1 == "that":
			 self.four_segments_pop("THAT", arg1, arg2)
		elif arg1 == "argument":
			 self.four_segments_pop("ARG", arg1, arg2)
		elif arg1 == "temp":
			 self.four_segments_pop("TEMP", arg1, arg2)
			

	def four_segments_push(self, segment, arg1, arg2):
		if segment == "ARG" or segment == "LCL" or segment == "THIS" or segment == "THAT":
			print "//push " + arg1 + " "+arg2 +'\n'\
			"@"+ arg2 + '\n'\
			'D=A' + '\n'\
			'@'+ segment + '\n'\
			'D=M+D' + '\n'\
			'A=D' + '\n'\
			'D=M' + '\n'\
			'@SP' + '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'

		elif segment == "TEMP":
			location = int(arg2) + 5
			print "//push " + arg1 + " "+arg2 +'\n'\
			"@"+ str(location)+ '\n'\
			'D=M' + '\n'\
			'@SP'  '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'

		elif segment == "CONST":
			location = int(arg2)
			print "//push " + arg1 + " "+arg2 +'\n'\
			"@"+ str(location)+ '\n'\
			'D=A' + '\n'\
			'@SP'  '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'


	def four_segments_pop(self, segment, arg1, arg2):
		if segment == "ARG" or segment == "LCL" or segment == "THIS" or segment == "THAT":
			print "//pop " + arg1 + " "+arg2 +'\n'\
			"@"+arg2 + '\n'\
			'D=A' + '\n'\
			'@'+ segment + '\n'\
			'D=M+D' + '\n'\
			'@addr' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M-1' + '\n'\
			'A=M' + '\n'\
			'D=M' + '\n'\
			'@addr' + '\n'\
			'A=M' + '\n'\
			'M=D'

		elif segment == "TEMP":
			location = int(arg2) + 5
			print "//pop " + arg1 + " "+arg2 +'\n'\
			'@SP' + '\n'\
			'M=M-1'  '\n'\
			'A=M' + '\n'\
			'D=M' + '\n'\
			"@"+ str(location)+ '\n'\
			'M=D'


	def arithmetic(self, command):
		if command == "add":
			print "//add"+'\n'\
			"@SP" + '\n'\
			'M=M-1' + '\n'\
			'A=M'+ '\n'\
			'D=M' + '\n'\
			'@addr' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M-1' + '\n'\
			'A=M' + '\n'\
			'D=M' + '\n'\
			'@addr' + '\n'\
			'D=M+D' + '\n'\
			'@SP' + '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'

		elif command == "sub":
			print "//sub"+'\n'\
			"@SP" + '\n'\
			'M=M-1' + '\n'\
			'A=M'+ '\n'\
			'D=M' + '\n'\
			'@addr' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M-1' + '\n'\
			'A=M' + '\n'\
			'D=M' + '\n'\
			'@addr' + '\n'\
			'D=D-M' + '\n'\
			'@SP' + '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'




