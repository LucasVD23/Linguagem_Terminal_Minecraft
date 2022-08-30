grammar Commands;

// Lexer
NUM_INT 				: ('0'..'9')+;
NUM_REAL				: ('0'..'9')+ ('.' ('0'..'9')+)?;

NAME					: ('a'..'z'|'A'..'Z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;

CADEIA 	: '\'' ( ESC_SEQ | ~('\''|'\\') )* '\'';
fragment ESC_SEQ: '\\\'';

// Ignorando espaços, tabulação, retorno e quebra de linha
WS  					:   ( ' ' | '\t' | '\r' | '\n') -> skip;

// Parser

program:
  (cmd)* EOF;

cmd: '/' summon | give | kill;

summon: 'summon' NAME 'Player'|type_mob;

type_mob: 'Creeper'|'Skeleton'| 'Spider'| 'Slime' | 'Enderman'| 'Zombie';

give: 'give' NAME item NUM_INT;

item: item_material? 'Sword'|'Axe'|'Pickaxe'|'Bow'|'Arrow'|'Helmet'|'Chestplate'|'Leggings'|'Boots';

item_material:  'Wooden'| 'Stone' | 'Iron'| 'Golden'| 'Diamond';

kill: 'kill' NAME;