from antlr4 import *
from EntitiesTable import EntitiesTable,Player,Mob
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
        elif(ctx.gamemode() is not None):
            return self.visitGamemode(ctx.gamemode())
        elif (ctx.time_set() is not None):
            return self.visitTime_set(ctx.time_set())
        elif (ctx.weather() is not None):
            return self.visitWeather(ctx.weather())
        elif (ctx.tp() is not None):
            return self.visitTp(ctx.tp())
        elif (ctx.difficulty() is not None):
            return self.visitDifficulty(ctx.difficulty())
        
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
        if (int(ctx.NUM_INT().getText()) < 1):
            raise Exception("You can't give a negative quantity of items, please type a positive value")
        elif(ctx.NAME() is not None):
            name = ctx.NAME().getText()
            if(not(self.entities_table.verify_entity_exists(name))):
                raise Exception("Player " + name +  " doesn't exist")
            elif(isinstance(self.entities_table.entities[name], Player)):
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
    
    def visitGamemode(self, ctx:CommandsParser.GamemodeContext):
        if(int(ctx.NUM_INT().getText()) < 0 or int(ctx.NUM_INT().getText())>3):
            raise Exception('Invalid value for gamemode, type 0 for survival, 1  for creative, 2 for adventure or 3 for spectator')
        return None
    
    def visitTime_set(self, ctx: CommandsParser.Time_setContext):
        if(ctx.NUM_INT() is not None):
            num_val = int(ctx.NUM_INT().getText())
            if(num_val > 2300 or num_val < 0):
                raise Exception('Invalid  timestamp, timestamp must be between 0 and 23000')
        return None
        
    def visitTp(self, ctx: CommandsParser.TpContext):
        if(ctx.NAME() is not None):
            name = ctx.NAME().getText()
            if(not(self.entities_table.verify_entity_exists(name))):
                raise Exception("Player " + name + " doesn't exist")
            elif(not(isinstance(self.entities_table.entities[name],Player))):
                raise Exception("Entity " + name + " is not a player")
        return None
