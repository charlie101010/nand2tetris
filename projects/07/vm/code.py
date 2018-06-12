import sys


class Code(object):

	def __init__(self):
		self.name = "code"

	def push(self, arg1, arg2):
		if arg1 == "local":
			 self.four_segments("LCL", arg1, arg2)
		elif arg1 == "this":
			 self.four_segments("THIS", arg1, arg2)
		elif arg1 == "that":
			 self.four_segments("THAT", arg1, arg2)
		elif arg1 == "argument":
			 self.four_segments("ARG", arg1, arg2)
			
	def pop(self, arg1, arg2):
		print "pop"


	def four_segments(self, segment, arg1, arg2):
		print "//push " + arg1 + " "+arg2 +'\n'\
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
		'@M=D'