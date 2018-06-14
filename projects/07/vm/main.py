import sys
import parser


name = sys.argv[1][:-3]
name = name
p = parser.Parser(name)
contents = p.parse()
# with open(name, 'w') as the_file:
# 	for item in contents:
# 		the_file.write("%s\n" % item)