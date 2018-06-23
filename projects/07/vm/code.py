import sys


class Code(object):

	def __init__(self):
		self.name = "code"
		self.count = 0
		self.retcount = 0
		self.currentClass = ""

#initiate the process of translation for a given push command type and pass the assembly abbreviation for LCL, THIS, THAT, ARG...this can definitely be more efficient
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

		
#initiate the process of translation for a given pop command type and pass the assembly abbreviation for LCL, THIS, THAT, ARG...this can definitely be more efficient			
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
	
			
#execute the translation from vm to assembly code and write to file
	def four_segments_push(self, segment, arg1, arg2, name=None):
		if segment == "ARG" or segment == "LCL" or segment == "THIS" or segment == "THAT":
			list = [ "//push " + arg1 + " "+arg2, 
			"@"+ arg2,
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
			same = name.split('/')[-1]
			list = ["//push " + arg1 + " "+arg2, 
			'@'+ same +'.' + arg2,
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
			'A=M',
			'D=M',
			"@"+ str(location),
			'M=D']
			self.write_to_file(name, list)

		elif segment == "STAT":
			same = name.split('/')[-1]
			list = ["//pop " + arg1 + " "+arg2,
			'@SP',
			'M=M-1',
			'A=M',
			'D=M',
			'@'+ same +'.' + arg2,
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

	def arithmetic(self, command, name):
		
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
			list = ["//gt",
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
			'@TRUE'+str(self.count),
			'D;JGT',
			'D=0',
			'@FALSE'+str(self.count),
			'0;JMP',
			'(TRUE'+str(self.count)+')',
			'D=-1',
			'(FALSE'+str(self.count)+')',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)
			

		elif command == "lt":
			self.count = self.count+1
			list =  ["//lt",
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
			'@TRUE'+str(self.count),
			'D;JLT',
			'D=0',
			'@FALSE'+ str(self.count),
			'0;JMP',
			'(TRUE' +str(self.count)+')',
			'D=-1',
			'(FALSE' +str(self.count)+')',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)
			

		elif command == "eq":
			self.count = self.count + 1
			list =  ["//eq",
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
			'@TRUE'+str(self.count),
			'D;JEQ',
			'D=0',
			'@FALSE' +str(self.count),
			'0;JMP',
			'(TRUE' +str(self.count)+')',
			'D=-1',
			'(FALSE' +str(self.count)+')',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
			self.write_to_file(name, list)


	def goto(self, label, name):
		list =  ["//goto " + label,
		"@" + label,
		"0; JMP"]
		self.write_to_file(name, list)

	def ifgoto(self, label, name):
		list =  ["//if-goto " + label,
		"@SP",
		"M=M-1",
		"A=M",
		"D=M",
		"@"+label,
		"D;JNE"]
		self.write_to_file(name, list)

	def label(self, label, name):
		same = name.split('/')[-1]
		list =  ["//label " + same + "." + self.currentClass + "$" + label,
		"(" + label +")"]
		self.write_to_file(name, list)

	def call(self, className, functionName, nArgs, name):
		list =  ["//call " + functionName,
		"(" + same + "." + self.currentClass + "$" + label +")"]
		self.write_to_file(name, list)

	def func(self, className, functName, nVars, name):
		nVars = int(nVars)
		pushlocal = []
		pushlocal = [(pushlocal + self.funcHelper(str(i))) for i in range(nVars)]
		list =  ["//function " + className + "." + functName,
		"(" + className + "." + functName +")"
		]
		for item in range(len(pushlocal)):
			for line in pushlocal[item]:
				list.append(line)
		self.currentClass = className
		print self.currentClass
		self.write_to_file(name, list)

	def funcHelper(self, nVars):
		list = [ "//push " + "local" + " "+ nVars,
			"@"+ nVars,
			'D=A',
			'@LCL',
			'D=M+D',
			'A=D',
			'D=M',
			'@SP',
			'A=M',
			'M=D',
			'@SP',
			'M=M+1']
		return list

	def ret(self, name):
		list = ["//return" + self.currentClass,
		"@" + self.currentClass + "$ret." + str(self.retcount),
		"0; JMP"]
		self.retcount = self.retcount + 1
		self.write_to_file(name, list)




#method used to actually write to file
	def write_to_file(self, listname, list):
		with open(listname + '.asm', 'a') as the_file:
			for item in list:
				the_file.write("%s\n" % item)












