import sys
from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl
from CommandsLexer import CommandsLexer
from CommandsParser import CommandsParser


def traverse(tree, rule_names, indent = 0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNodeImpl):
        print("{0}TOKEN='{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}{1}".format("  " * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, indent + 1)
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CommandsLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = CommandsParser(stream)
    tree = parser.program()
    #traverse(tree, parser.ruleNames)

if __name__ == '__main__':
    main(sys.argv)