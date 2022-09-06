# Generated from Commands.g4 by ANTLR 4.11.1
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
        4,1,30,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,5,0,19,8,0,10,0,12,0,22,9,0,1,0,1,0,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,3,2,35,8,2,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,5,3,5,45,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,56,8,
        5,1,6,1,6,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,0,4,9,1,
        0,20,24,67,0,20,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,36,1,0,0,0,8,
        38,1,0,0,0,10,55,1,0,0,0,12,57,1,0,0,0,14,59,1,0,0,0,16,17,5,1,0,
        0,17,19,3,2,1,0,18,16,1,0,0,0,19,22,1,0,0,0,20,18,1,0,0,0,20,21,
        1,0,0,0,21,23,1,0,0,0,22,20,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,
        29,3,4,2,0,26,29,3,8,4,0,27,29,3,14,7,0,28,25,1,0,0,0,28,26,1,0,
        0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,2,0,0,31,34,5,28,0,0,32,35,
        3,6,3,0,33,35,5,3,0,0,34,32,1,0,0,0,34,33,1,0,0,0,35,5,1,0,0,0,36,
        37,7,0,0,0,37,7,1,0,0,0,38,39,5,10,0,0,39,40,5,28,0,0,40,41,3,10,
        5,0,41,42,5,26,0,0,42,9,1,0,0,0,43,45,3,12,6,0,44,43,1,0,0,0,44,
        45,1,0,0,0,45,46,1,0,0,0,46,56,5,11,0,0,47,56,5,12,0,0,48,56,5,13,
        0,0,49,56,5,14,0,0,50,56,5,15,0,0,51,56,5,16,0,0,52,56,5,17,0,0,
        53,56,5,18,0,0,54,56,5,19,0,0,55,44,1,0,0,0,55,47,1,0,0,0,55,48,
        1,0,0,0,55,49,1,0,0,0,55,50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,0,
        55,53,1,0,0,0,55,54,1,0,0,0,56,11,1,0,0,0,57,58,7,1,0,0,58,13,1,
        0,0,0,59,60,5,25,0,0,60,61,5,28,0,0,61,15,1,0,0,0,5,20,28,34,44,
        55
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
        self.checkVersion("4.11.1")
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
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 16
                self.match(CommandsParser.T__0)
                self.state = 17
                self.cmd()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 23
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
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.summon()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.give()
                pass
            elif token in [25]:
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(CommandsParser.T__1)
            self.state = 31
            self.match(CommandsParser.NAME)
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9]:
                self.state = 32
                self.type_mob()
                pass
            elif token in [3]:
                self.state = 33
                self.match(CommandsParser.T__2)
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
            self.state = 36
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0):
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
            self.state = 38
            self.match(CommandsParser.T__9)
            self.state = 39
            self.match(CommandsParser.NAME)
            self.state = 40
            self.item()
            self.state = 41
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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0:
                    self.state = 43
                    self.item_material()


                self.state = 46
                self.match(CommandsParser.T__10)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(CommandsParser.T__11)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(CommandsParser.T__12)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.match(CommandsParser.T__13)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.match(CommandsParser.T__14)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.match(CommandsParser.T__15)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.match(CommandsParser.T__16)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.match(CommandsParser.T__17)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 9)
                self.state = 54
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
            self.state = 57
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0):
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
            self.state = 59
            self.match(CommandsParser.T__24)
            self.state = 60
            self.match(CommandsParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





