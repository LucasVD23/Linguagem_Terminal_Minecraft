# Generated from Commands.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandsParser import CommandsParser
else:
    from CommandsParser import CommandsParser

# This class defines a complete generic visitor for a parse tree produced by CommandsParser.

class CommandsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommandsParser#program.
    def visitProgram(self, ctx:CommandsParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#cmd.
    def visitCmd(self, ctx:CommandsParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#summon.
    def visitSummon(self, ctx:CommandsParser.SummonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#type_mob.
    def visitType_mob(self, ctx:CommandsParser.Type_mobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#give.
    def visitGive(self, ctx:CommandsParser.GiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#item.
    def visitItem(self, ctx:CommandsParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#item_material.
    def visitItem_material(self, ctx:CommandsParser.Item_materialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#kill.
    def visitKill(self, ctx:CommandsParser.KillContext):
        return self.visitChildren(ctx)



del CommandsParser