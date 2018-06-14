import sys


class Code(object):

	def __init__(self):
		self.name = "code"
		self.count = 0

	def push(self, arg1, arg2, name):
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
		elif arg1 == "pointer":
			 self.four_segments_push("POI", arg1, arg2)
		elif arg1 == "static":
			 self.four_segments_push("STAT", arg1, arg2, name)
		

			
	def pop(self, arg1, arg2, name):
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
		elif arg1 == "static":
			 self.four_segments_pop("STAT", arg1, arg2, name)
		elif arg1 == "pointer":
			 self.four_segments_pop("POI", arg1, arg2)
	
			

	def four_segments_push(self, segment, arg1, arg2, name=None):
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


		elif segment == "STAT":
			name = name.split('/')[-1]
			print "//push " + arg1 + " "+arg2 +'\n'\
			'@'+ name +'.' + arg2 + '\n'\
			'D=M' + '\n'\
			'@SP' + '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'

		elif segment == "POI":
			if arg2 == "0":
				print "//push " + arg1 + " "+arg2 +'\n'\
				'@THIS'+ '\n'\
				'D=M' + '\n'\
				'@SP' + '\n'\
				'A=M' + '\n'\
				'M=D' + '\n'\
				'@SP' + '\n'\
				'M=M+1'

			elif arg2 =="1":
				print "//push " + arg1 + " "+arg2 +'\n'\
				'@THAT'+ '\n'\
				'D=M' + '\n'\
				'@SP' + '\n'\
				'A=M' + '\n'\
				'M=D' + '\n'\
				'@SP' + '\n'\
				'M=M+1'


	def four_segments_pop(self, segment, arg1, arg2, name=None):
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

		elif segment == "STAT":
			name = name.split('/')[-1]
			print "//pop " + arg1 + " "+arg2 +'\n'\
			'@SP' +'\n'\
			'M=M-1' +'\n'\
			'A=M' +'\n'\
			'D=M' +'\n'\
			'@'+ name +'.' + arg2 + '\n'\
			'M=D'

		elif segment == "POI":
			if arg2 == "0":
				print "//pop " + arg1 + " "+arg2 +'\n'\
				'@SP' + '\n'\
				'M=M-1' + '\n'\
				'A=M' +'\n'\
				'D=M' + '\n'\
				'@THIS'+ '\n'\
				'M=D' + '\n'\
				
			elif arg2 =="1":
				print "//pop " + arg1 + " "+arg2 +'\n'\
				'@SP' + '\n'\
				'M=M-1' + '\n'\
				'A=M' +'\n'\
				'D=M' + '\n'\
				'@THAT'+ '\n'\
				'M=D' + '\n'\

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

		elif command == "neg":
			print "//neg"+'\n'\
			"@SP" + '\n'\
			'D=M-1' + '\n'\
			'A=D'+ '\n'\
			'M=-M'
			
		elif command == "not":
			print "//not"+'\n'\
			"@SP" + '\n'\
			'D=M-1' + '\n'\
			'A=D'+ '\n'\
			'M=!M' 

		elif command == "or":
			print "//or"+'\n'\
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
			'D=D|M' + '\n'\
			'@SP' + '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'

		elif command == "and":
			print "//and"+'\n'\
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
			'D=D&M' + '\n'\
			'@SP' + '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'

		elif command == "gt":
			self.count = self.count + 1
			print "//gt"+'\n'\
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
			'@TRUE'+str(self.count) + '\n'\
			'D;JGT' + '\n'\
			'D=0' + '\n'\
			'@FALSE'+str(self.count) + '\n'\
			'0;JMP' + '\n'\
			'(TRUE'+str(self.count)+')' + '\n'\
			'D=-1' + '\n'\
			'(FALSE'+str(self.count)+')' + '\n'\
			'@SP' + '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'
			

		elif command == "lt":
			self.count = self.count+1
			print "//lt"+'\n'\
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
			'@TRUE'+str(self.count) + '\n'\
			'D;JLT' + '\n'\
			'D=0' + '\n'\
			'@FALSE'+ str(self.count)+ '\n'\
			'0;JMP' + '\n'\
			'(TRUE' +str(self.count)+')' + '\n'\
			'D=-1' + '\n'\
			'(FALSE' +str(self.count)+')' + '\n'\
			'@SP' + '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'
			

		elif command == "eq":
			self.count = self.count + 1
			print "//eq"+'\n'\
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
			'@TRUE'+str(self.count) + '\n'\
			'D;JEQ' + '\n'\
			'D=0' + '\n'\
			'@FALSE' +str(self.count) + '\n'\
			'0;JMP' + '\n'\
			'(TRUE' +str(self.count)+')' + '\n'\
			'D=-1' + '\n'\
			'(FALSE' +str(self.count)+')' + '\n'\
			'@SP' + '\n'\
			'A=M' + '\n'\
			'M=D' + '\n'\
			'@SP' + '\n'\
			'M=M+1'






