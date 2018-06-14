import sys
import parser

#Store filename from read
name = sys.argv[1][:-3]
name = name

#Parse, translate and write assembly code
p = parser.Parser(name)
p.parse()
