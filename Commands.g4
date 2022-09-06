grammar Commands;

// Lexer
NUM_INT 				: ('0'..'9')+;
NUM_REAL				: ('0'..'9')+ ('.' ('0'..'9')+)?;

NAME					: ('a'..'z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;

CADEIA 	: '\'' ( ESC_SEQ | ~('\''|'\\') )* '\'';
fragment ESC_SEQ: '\\\'';

// Ignorando espaços, tabulação, retorno e quebra de linha
WS  					:   ( ' ' | '\t' | '\r' | '\n') -> skip;

// Parser

program:
  ('/'cmd)* EOF;

cmd:  summon | give | kill | gamemode | time_set | weather | tp | difficulty;

summon: 'summon' NAME (mob_type|'Player');

mob_type: 'Creeper'|'Skeleton'| 'Spider'| 'Slime' | 'Enderman'| 'Zombie';

give: 'give' ('@a'|NAME) item NUM_INT;

item: item_material? 'Sword'|'Axe'|'Pickaxe'|'Bow'|'Arrow'|'Helmet'|'Chestplate'|'Leggings'|'Boots';

item_material:  'Wooden'| 'Stone' | 'Iron'| 'Golden'| 'Diamond';

kill: 'kill' NAME;

gamemode: 'gamemode' NUM_INT;

time_set: 'time set' (time_string|NUM_INT);

time_string: 'day'|'noon'|'midday'|'sunset'|'dusk'|'midnight'|'sunrise'|'dawn';

weather: 'weather' weather_type;

weather_type: 'clear' | 'rain' | 'snow' | 'thunder';

tp: 'tp' NAME NUM_INT NUM_INT NUM_INT;

difficulty: 'difficulty' difficulty_level;

difficulty_level: 'peaceful' | 'easy' | 'normal' | 'hard';