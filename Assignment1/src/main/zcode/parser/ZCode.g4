grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: (statements | main_decl | func_decl | NEWLINE)* EOF;	

//declarations: func_decl + var_decl
func_decl: FUNC_ ID LB paramList RB func_body?;
main_decl: FUNC_ 'main' LB RB func_body?;
func_body: blockStmt | returnStmt;
var_decl: (NUM | BOOL_ | STR_| VAR_ | DYNAMIC) singDecl | arrayT ID LSB sizeList RSB;
singDecl: ID (WIS expr)?;


//type
typ: primitive | arrayT; 
primitive: NUMBERS | BOOLS | STRS;
arrayT: primitive ID LSB indexExpr RSB;
indexExpr: NUMBERS indexTail | NUMBERS;
indexTail: CM NUMBERS indexTail | ;

//lists
argList: argument argT | ;
argT: CM argument argT | ;
argument: ID | literals;

paramList: param paramT | ;
paramT: CM param paramT | ;
param: primitive? ID | arrayT ;

stmt_list: statements stmtT | ;
stmtT: NEWLINE statements stmtT | ;

func_list: func_decl funcT | ;
funcT: NEWLINE func_decl funcT | ;

sizeList: INT_PART sizeT | INT_PART;
sizeT: CM INT_PART sizeT| ;

//expressions
expr: expr1 STRCONCAT expr1 | expr1;
expr1: expr2 (ASSIGN | EQ | DIFF | LT | GT | LTEQ | GTEQ) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | MINUS) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: expr7 LSB index_op RSB | expr8; //index operator
expr8: literals | arrayT | LB expr RB | ID | funcCallStmt; //operands

index_op: expr | expr CM index_op; 
funcCall: ID LCB argList RCB;

//statements
statements: (var_declStmt | assignStmt | ifStmt | forStmt | breakStmt | contStmt | returnStmt | funcCallStmt | blockStmt) NEWLINE;

var_declStmt: var_decl;
assignStmt: lhs WIS expr;

ifStmt: IF_ LB expr RB statements elifStmt elseStmt?;

elifStmt: elif1 elseifT | ;
elseifT: NEWLINE elif1 elseifT | ;
elif1: ELSE_IF LB expr RB statements;
elseStmt: ELSE_ statements;

forStmt: FOR_ ID UNTIL expr BY expr NEWLINE stmt_list;
breakStmt: BREAK_;
contStmt: CONT;
returnStmt: RET_ expr?;
funcCallStmt: funcCall;
blockStmt: BEGIN blockBody END;
blockBody: stmt_list | NEWLINE+;
lhs: ID | expr7;

// Lexer 
//Seperator
LSB:'[';
RSB: ']';
LCB: '{';
RCB: '}';
LB: '(';
RB: ')';
CM: ',';
COLON: ':';


//Operators
SM: ';';
ADD: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
ASSIGN: '=';
EQ: '==';
DIFF: '!=';
GT: '>';
LT: '<';
LTEQ: '<=';
GTEQ: '>=';
WIS: '<-';
NOT: 'not';
AND: 'and';
OR: 'OR';
STRCONCAT: '...';

//keywords
TRUE_: 'true';
FALSE_: 'false';
NUM: 'number';
BOOL_: 'bool';
STR_: 'string';
RET_: 'return';
VAR_: 'var';
DYNAMIC: 'dynamic';
FUNC_: 'func';
FOR_: 'for';
UNTIL: 'until';
BY: 'by';
BREAK_: 'break';
CONT: 'continue'; 

IF_: 'if';
ELSE_: 'else';
ELSE_IF: 'elif';
BEGIN: 'begin';
END: 'end';

INT_: 'int';
FLOAT_: 'float';
CONST_: 'const';
DOT: '.';

literals: NUMBERS | BOOLS | STRS;
NUMBERS: INT_PART+ (DOT INT_PART+ EXPO_PART? | EXPO_PART)?;
BOOLS: TRUE_ | FALSE_;

INT_PART: [0-9];
EXPO_PART: [Ee] (ADD | MINUS)? INT_PART+;
NEWLINE: '\n';

STRS: DQUOTE ( (ESCCHAR | STRCHAR)*) DQUOTE {self.text=self.text[1:-1]}; // [1:-1]
fragment DQUOTE  : '"';
fragment STRCHAR : ~[\\'"];
fragment ESCCHAR : (('\\b')|('\\f')|('\\r')|('\\n')|('\\t')|('\\\'')|('\\\\')|('\'"')); // \b \f \r \n \t ' \\ '"
fragment ILLESC  : ('\\' ~[bfrnt\\']) | ('\'' ~["]);

ID: [a-zA-Z_][a-zA-Z0-9_]*;
LINECMT: (('##' .*? ) | ('##' ~['##']* )) -> skip ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING	: '"' (ESCCHAR | STRCHAR)* EOF {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE	: '"' ((ESCCHAR | STRCHAR)*? ILLESC ) {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: .{raise ErrorToken(self.text)};