# Generated from Commands.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandsParser import CommandsParser
else:
    from CommandsParser import CommandsParser

# This class defines a complete listener for a parse tree produced by CommandsParser.
class CommandsListener(ParseTreeListener):

    # Enter a parse tree produced by CommandsParser#program.
    def enterProgram(self, ctx:CommandsParser.ProgramContext):
        pass

    # Exit a parse tree produced by CommandsParser#program.
    def exitProgram(self, ctx:CommandsParser.ProgramContext):
        pass


    # Enter a parse tree produced by CommandsParser#cmd.
    def enterCmd(self, ctx:CommandsParser.CmdContext):
        pass

    # Exit a parse tree produced by CommandsParser#cmd.
    def exitCmd(self, ctx:CommandsParser.CmdContext):
        pass


    # Enter a parse tree produced by CommandsParser#summon.
    def enterSummon(self, ctx:CommandsParser.SummonContext):
        pass

    # Exit a parse tree produced by CommandsParser#summon.
    def exitSummon(self, ctx:CommandsParser.SummonContext):
        pass


    # Enter a parse tree produced by CommandsParser#type_mob.
    def enterType_mob(self, ctx:CommandsParser.Type_mobContext):
        pass

    # Exit a parse tree produced by CommandsParser#type_mob.
    def exitType_mob(self, ctx:CommandsParser.Type_mobContext):
        pass


    # Enter a parse tree produced by CommandsParser#give.
    def enterGive(self, ctx:CommandsParser.GiveContext):
        pass

    # Exit a parse tree produced by CommandsParser#give.
    def exitGive(self, ctx:CommandsParser.GiveContext):
        pass


    # Enter a parse tree produced by CommandsParser#item.
    def enterItem(self, ctx:CommandsParser.ItemContext):
        pass

    # Exit a parse tree produced by CommandsParser#item.
    def exitItem(self, ctx:CommandsParser.ItemContext):
        pass


    # Enter a parse tree produced by CommandsParser#item_material.
    def enterItem_material(self, ctx:CommandsParser.Item_materialContext):
        pass

    # Exit a parse tree produced by CommandsParser#item_material.
    def exitItem_material(self, ctx:CommandsParser.Item_materialContext):
        pass


    # Enter a parse tree produced by CommandsParser#kill.
    def enterKill(self, ctx:CommandsParser.KillContext):
        pass

    # Exit a parse tree produced by CommandsParser#kill.
    def exitKill(self, ctx:CommandsParser.KillContext):
        pass



del CommandsParser