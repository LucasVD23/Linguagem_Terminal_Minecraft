from xml.dom.minidom import Entity
from antlr4 import *
from EntitiesTable import EntitiesTable,Player,Mob
from visitorFiles.CommandsLexer import CommandsLexer
from visitorFiles.CommandsParser import CommandsParser
from visitorFiles.CommandsVisitor import CommandsVisitor

class Visitor(CommandsVisitor):
    entities_table = EntitiesTable()
    def visitProgram(self, ctx: CommandsParser.ProgramContext):
        return self.visitChildren(ctx)
    
    def visitCmd(self, ctx: CommandsParser.CmdContext):
        if (ctx.summon() is not None):
            return self.visitSummon(ctx.summon())
        elif (ctx.give() is not None):
            return self.visitGive(ctx.give())
        elif (ctx.kill() is not None):
            return self.visitKill(ctx.kill())
        # elif(ctx.gamemode() is not None):
        #     return self.visitGamemode(ctx.gamemode())
        # elif (ctx.time_set() is not None):
        #     return self.visitTime_set(ctx.time_set())
        # elif (ctx.weather() is not None):
        #     return self.visitWeather(ctx.weather())
        # elif (ctx.tp() is not None):
        #     return self.visitTp(ctx.tp())
        # elif (ctx.difficulty() is not None):
        #     return self.visitDifficulty(ctx.difficulty())
        
        return None

    def visitSummon(self, ctx: CommandsParser.SummonContext):
        name = ctx.NAME().getText()
        if(ctx.mob_type() is not None):
            new_entity = Mob(name)
            self.entities_table.add_entity(new_entity)
        else:
            new_entity = Player(name)
            self.entities_table.add_entity(new_entity)
        return None

    def visitGive(self, ctx: CommandsParser.GiveContext):
        if(ctx.NAME().getText() is not None):
            print("TESTE")
            name = ctx.NAME().getText()
            if(isinstance(self.entities_table.entities[name], Player)):
                self.entities_table.entities[name].add_inventory(int(ctx.NUM_INT().getText()))
            else:
                raise Exception("You can only give itens to Players")
        elif('@a' in ctx.getText()):
            for entity in self.entities_table.entities:
                if(isinstance(entity, Player)):
                    entity.add_inventory(int(ctx.NUM_INT().getText()))
        
        return None
    
    def visitKill(self,ctx:CommandsParser.KillContext):
        name = ctx.NAME().getText()
        self.entities_table.kill_entity(name)

        return None
