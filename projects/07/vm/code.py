import sys


class Code(object):

	def __init__(self):
		self.name = "code"
		self.count = 0

	def push(self, arg1, arg2, name):
		if arg1 == "local":
			self.four_segments_push("LCL", arg1, arg2, name)
		elif arg1 == "this":
			self.four_segments_push("THIS", arg1, arg2, name)
		elif arg1 == "that":
			self.four_segments_push("THAT", arg1, arg2, name)
		elif arg1 == "argument":
			self.four_segments_push("ARG", arg1, arg2, name)
		elif arg1 == "temp":
			self.four_segments_push("TEMP", arg1, arg2, name)
		elif arg1 == "constant":
			self.four_segments_push("CONST", arg1, arg2, name)
		elif arg1 == "pointer":
			self.four_segments_push("POI", arg1, arg2, name)
		elif arg1 == "static":
			 self.four_segments_push("STAT", arg1, arg2, name)
		

			
	def pop(self, arg1, arg2, name):
		if arg1 == "local":
			self.four_segments_pop("LCL", arg1, arg2, name)
		elif arg1 == "this":
			self.four_segments_pop("THIS", arg1, arg2, name)
		elif arg1 == "that":
			self.four_segments_pop("THAT", arg1, arg2, name)
		elif arg1 == "argument":
			self.four_segments_pop("ARG", arg1, arg2, name)
		elif arg1 == "temp":
			self.four_segments_pop("TEMP", arg1, arg2, name)
		elif arg1 == "static":
			self.four_segments_pop("STAT", arg1, arg2, name)
		elif arg1 == "pointer":
			self.four_segments_pop("POI", arg1, arg2, name)
	
			

	def four_segments_push(self, segment, arg1, arg2, name=None):
		if segment == "ARG" or segment == "LCL" or segment == "THIS" or segment == "THAT":
			list = [ "//push " + arg1 + " "+arg2, 
			"@"+ arg2 ,
			'D=A',
			'@'+ segment,
			'D=M+D',
			'A=D',
			'D=M',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)

		elif segment == "TEMP":
			location = int(arg2) + 5
			list = ["//push " + arg1 + " "+arg2,
			"@"+ str(location),
			'D=M',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)

		elif segment == "CONST":
			location = int(arg2)
			list =["//push " + arg1 + " "+arg2,
			"@"+ str(location),
			'D=A',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)


		elif segment == "STAT":
			name = name.split('/')[-1]
			list = ["//push " + arg1 + " "+arg2, 
			'@'+ name +'.' + arg2,
			'D=M',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)

		elif segment == "POI":
			if arg2 == "0":
				list = ["//push " + arg1 + " "+arg2,
				'@THIS',
				'D=M',
				'@SP',
				'A=M',
				'M=D',
				'@SP',
				'M=M+1']
				self.write_to_file(name, list)

			elif arg2 =="1":
				list = ["//push " + arg1 + " "+arg2,
				'@THAT',
				'D=M',
				'@SP',
				'A=M',
				'M=D',
				'@SP',
				'M=M+1']
				self.write_to_file(name, list)


	def four_segments_pop(self, segment, arg1, arg2, name=None):
		if segment == "ARG" or segment == "LCL" or segment == "THIS" or segment == "THAT":
			list = ["//pop " + arg1 + " "+arg2,
			"@"+arg2,
			'D=A',
			'@'+ segment,
			'D=M+D',
			'@addr',
			'M=D',
			'@SP',
			'M=M-1',
			'A=M',
			'D=M',
			'@addr',
			'A=M', 
			'M=D']
			self.write_to_file(name, list)

		elif segment == "TEMP":
			location = int(arg2) + 5
			list = ["//pop " + arg1 + " "+arg2,
			'@SP',
			'M=M-1',
			'A=M'
			'D=M',
			"@"+ str(location),
			'M=D']
			self.write_to_file(name, list)

		elif segment == "STAT":
			name = name.split('/')[-1]
			list = ["//pop " + arg1 + " "+arg2,
			'@SP',
			'M=M-1',
			'A=M',
			'D=M',
			'@'+ name +'.' + arg2,
			'M=D']
			self.write_to_file(name, list)

		elif segment == "POI":
			if arg2 == "0":
				list = ["//pop " + arg1 + " "+arg2,
				'@SP',
				'M=M-1',
				'A=M',
				'D=M',
				'@THIS',
				'M=D']
				self.write_to_file(name, list)
				
			elif arg2 =="1":
				list = ["//pop " + arg1 + " "+arg2,
				'@SP',
				'M=M-1',
				'A=M',
				'D=M',
				'@THAT',
				'M=D']
				self.write_to_file(name, list)

	def arithmetic(self, command):
		
		if command == "add":
			list = ["//add",
			"@SP",
			'M=M-1',
			'A=M',
			'D=M',
			'@addr',
			'M=D',
			'@SP',
			'M=M-1',
			'A=M',
			'D=M',
			'@addr',
			'D=M+D',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)

		elif command == "sub":
			list = ["//sub",
			"@SP",
			'M=M-1',
			'A=M',
			'D=M',
			'@addr',
			'M=D',
			'@SP',
			'M=M-1',
			'A=M',
			'D=M',
			'@addr',
			'D=D-M',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)

		elif command == "neg":
			list = ["//neg",
			"@SP",
			'D=M-1',
			'A=D',
			'M=-M']
			self.write_to_file(name, list)
			
		elif command == "not":
			list = ["//not",
			"@SP",
			'D=M-1',
			'A=D',
			'M=!M' ]
			self.write_to_file(name, list)

		elif command == "or":
			list = ["//or",
			"@SP",
			'M=M-1',
			'A=M',
			'D=M',
			'@addr',
			'M=D',
			'@SP',
			'M=M-1',
			'A=M',
			'D=M',
			'@addr',
			'D=D|M',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)

		elif command == "and":
			list =  ["//and",
			"@SP",
			'M=M-1',
			'A=M',
			'D=M',
			'@addr',
			'M=D',
			'@SP',
			'M=M-1',
			'A=M',
			'D=M',
			'@addr',
			'D=D&M',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)

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
			self.write_to_file(name, list)
			

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
			self.write_to_file(name, list)
			

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
			self.write_to_file(name, list)


	def write_to_file(self, listname, list):
				with open(listname+ '.asm', 'a') as the_file:
					for item in list:
						the_file.write("%s\n" % item)






