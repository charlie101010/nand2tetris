import sys
import parser


name = sys.argv[1][:-3]
name = name
p = parser.Parser(name)
p.parse()
