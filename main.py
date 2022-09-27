import sys
from antlr4 import *
from visitor import Visitor
from visitorFiles.CommandsLexer import CommandsLexer
from visitorFiles.CommandsParser import CommandsParser
from CodeGenerator import CodeGenerator


class MyErrorStrategy(BailErrorStrategy):
    def recover(self, recognizer:Parser, e:RecognitionException):
        recognizer._errHandler.reportError(recognizer,e)
        raise Exception(e)
    

 
def main(argv):
    input_stream = FileStream(argv[1])
    
    lexer = CommandsLexer(input_stream)
        
    stream = CommonTokenStream(lexer)
    parser = CommandsParser(stream)
    tree = parser.program()
    visitor = Visitor()
    visitor.visit(tree)

    if(parser.getNumberOfSyntaxErrors() == 0): 
            
        print('Fim da Compilação')
        gerador = CodeGenerator()
        gerador.visitProgram(tree)
        generated_file = open('generated_file.py', 'w')
        generated_file.write(gerador.saida)
        generated_file.close()



if __name__ == '__main__':
    main(sys.argv)
