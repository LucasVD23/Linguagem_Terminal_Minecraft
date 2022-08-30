import sys
from antlr4 import *

from CommandsLexer import CommandsLexer
from CommandsParser import CommandsParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CommandsLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CommandsParser(stream)
    tree = parser.program()
 
if __name__ == '__main__':
    main(sys.argv)