# Generated from Commands.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,3,2,34,8,2,1,2,3,2,37,8,2,1,3,1,3,1,4,1,
        4,1,4,1,4,1,4,1,5,3,5,47,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,58,8,5,1,6,1,6,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,
        1,0,4,9,1,0,20,24,70,0,19,1,0,0,0,2,28,1,0,0,0,4,36,1,0,0,0,6,38,
        1,0,0,0,8,40,1,0,0,0,10,57,1,0,0,0,12,59,1,0,0,0,14,61,1,0,0,0,16,
        18,3,2,1,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,
        0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,25,5,
        1,0,0,25,29,3,4,2,0,26,29,3,8,4,0,27,29,3,14,7,0,28,24,1,0,0,0,28,
        26,1,0,0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,2,0,0,31,33,5,28,0,
        0,32,34,5,3,0,0,33,32,1,0,0,0,33,34,1,0,0,0,34,37,1,0,0,0,35,37,
        3,6,3,0,36,30,1,0,0,0,36,35,1,0,0,0,37,5,1,0,0,0,38,39,7,0,0,0,39,
        7,1,0,0,0,40,41,5,10,0,0,41,42,5,28,0,0,42,43,3,10,5,0,43,44,5,26,
        0,0,44,9,1,0,0,0,45,47,3,12,6,0,46,45,1,0,0,0,46,47,1,0,0,0,47,48,
        1,0,0,0,48,58,5,11,0,0,49,58,5,12,0,0,50,58,5,13,0,0,51,58,5,14,
        0,0,52,58,5,15,0,0,53,58,5,16,0,0,54,58,5,17,0,0,55,58,5,18,0,0,
        56,58,5,19,0,0,57,46,1,0,0,0,57,49,1,0,0,0,57,50,1,0,0,0,57,51,1,
        0,0,0,57,52,1,0,0,0,57,53,1,0,0,0,57,54,1,0,0,0,57,55,1,0,0,0,57,
        56,1,0,0,0,58,11,1,0,0,0,59,60,7,1,0,0,60,13,1,0,0,0,61,62,5,25,
        0,0,62,63,5,28,0,0,63,15,1,0,0,0,6,19,28,33,36,46,57
    ]

class CommandsParser ( Parser ):

    grammarFileName = "Commands.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "'summon'", "'Player'", "'Creeper'", 
                     "'Skeleton'", "'Spider'", "'Slime'", "'Enderman'", 
                     "'Zombie'", "'give'", "'Sword'", "'Axe'", "'Pickaxe'", 
                     "'Bow'", "'Arrow'", "'Helmet'", "'Chestplate'", "'Leggings'", 
                     "'Boots'", "'Wooden'", "'Stone'", "'Iron'", "'Golden'", 
                     "'Diamond'", "'kill'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM_INT", "NUM_REAL", "NAME", 
                      "CADEIA", "WS" ]

    RULE_program = 0
    RULE_cmd = 1
    RULE_summon = 2
    RULE_type_mob = 3
    RULE_give = 4
    RULE_item = 5
    RULE_item_material = 6
    RULE_kill = 7

    ruleNames =  [ "program", "cmd", "summon", "type_mob", "give", "item", 
                   "item_material", "kill" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    NUM_INT=26
    NUM_REAL=27
    NAME=28
    CADEIA=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CommandsParser.EOF, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.CmdContext)
            else:
                return self.getTypedRuleContext(CommandsParser.CmdContext,i)


        def getRuleIndex(self):
            return CommandsParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = CommandsParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CommandsParser.T__0) | (1 << CommandsParser.T__9) | (1 << CommandsParser.T__24))) != 0):
                self.state = 16
                self.cmd()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(CommandsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def summon(self):
            return self.getTypedRuleContext(CommandsParser.SummonContext,0)


        def give(self):
            return self.getTypedRuleContext(CommandsParser.GiveContext,0)


        def kill(self):
            return self.getTypedRuleContext(CommandsParser.KillContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = CommandsParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cmd)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandsParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(CommandsParser.T__0)
                self.state = 25
                self.summon()
                pass
            elif token in [CommandsParser.T__9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.give()
                pass
            elif token in [CommandsParser.T__24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.kill()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(CommandsParser.NAME, 0)

        def type_mob(self):
            return self.getTypedRuleContext(CommandsParser.Type_mobContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_summon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummon" ):
                listener.enterSummon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummon" ):
                listener.exitSummon(self)




    def summon(self):

        localctx = CommandsParser.SummonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_summon)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandsParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(CommandsParser.T__1)
                self.state = 31
                self.match(CommandsParser.NAME)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CommandsParser.T__2:
                    self.state = 32
                    self.match(CommandsParser.T__2)


                pass
            elif token in [CommandsParser.T__3, CommandsParser.T__4, CommandsParser.T__5, CommandsParser.T__6, CommandsParser.T__7, CommandsParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.type_mob()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_mobContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandsParser.RULE_type_mob

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_mob" ):
                listener.enterType_mob(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_mob" ):
                listener.exitType_mob(self)




    def type_mob(self):

        localctx = CommandsParser.Type_mobContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type_mob)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CommandsParser.T__3) | (1 << CommandsParser.T__4) | (1 << CommandsParser.T__5) | (1 << CommandsParser.T__6) | (1 << CommandsParser.T__7) | (1 << CommandsParser.T__8))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(CommandsParser.NAME, 0)

        def item(self):
            return self.getTypedRuleContext(CommandsParser.ItemContext,0)


        def NUM_INT(self):
            return self.getToken(CommandsParser.NUM_INT, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_give

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGive" ):
                listener.enterGive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGive" ):
                listener.exitGive(self)




    def give(self):

        localctx = CommandsParser.GiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_give)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(CommandsParser.T__9)
            self.state = 41
            self.match(CommandsParser.NAME)
            self.state = 42
            self.item()
            self.state = 43
            self.match(CommandsParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item_material(self):
            return self.getTypedRuleContext(CommandsParser.Item_materialContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = CommandsParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_item)
        self._la = 0 # Token type
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CommandsParser.T__10, CommandsParser.T__19, CommandsParser.T__20, CommandsParser.T__21, CommandsParser.T__22, CommandsParser.T__23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CommandsParser.T__19) | (1 << CommandsParser.T__20) | (1 << CommandsParser.T__21) | (1 << CommandsParser.T__22) | (1 << CommandsParser.T__23))) != 0):
                    self.state = 45
                    self.item_material()


                self.state = 48
                self.match(CommandsParser.T__10)
                pass
            elif token in [CommandsParser.T__11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(CommandsParser.T__11)
                pass
            elif token in [CommandsParser.T__12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(CommandsParser.T__12)
                pass
            elif token in [CommandsParser.T__13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.match(CommandsParser.T__13)
                pass
            elif token in [CommandsParser.T__14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 52
                self.match(CommandsParser.T__14)
                pass
            elif token in [CommandsParser.T__15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 53
                self.match(CommandsParser.T__15)
                pass
            elif token in [CommandsParser.T__16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 54
                self.match(CommandsParser.T__16)
                pass
            elif token in [CommandsParser.T__17]:
                self.enterOuterAlt(localctx, 8)
                self.state = 55
                self.match(CommandsParser.T__17)
                pass
            elif token in [CommandsParser.T__18]:
                self.enterOuterAlt(localctx, 9)
                self.state = 56
                self.match(CommandsParser.T__18)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Item_materialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandsParser.RULE_item_material

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_material" ):
                listener.enterItem_material(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_material" ):
                listener.exitItem_material(self)




    def item_material(self):

        localctx = CommandsParser.Item_materialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_item_material)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CommandsParser.T__19) | (1 << CommandsParser.T__20) | (1 << CommandsParser.T__21) | (1 << CommandsParser.T__22) | (1 << CommandsParser.T__23))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KillContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(CommandsParser.NAME, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_kill

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKill" ):
                listener.enterKill(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKill" ):
                listener.exitKill(self)




    def kill(self):

        localctx = CommandsParser.KillContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_kill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(CommandsParser.T__24)
            self.state = 62
            self.match(CommandsParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





