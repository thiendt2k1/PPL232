grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: func_list*  main_decl func_list* EOF;
main_decl: Newline* FUN main_call;
main_call: 'main' PRL PRR Newline (blk_stmt | rt_stmt);
func_list: func_decl func_tail | ;
func_tail: func_decl func_tail | ;

lit: NUMLIT | BOOLIT | STRLIT ; 

data_type: prida_type | arr_type;
prida_type: NUM | BOOL | STR ;
arr_type: prida_type SBL mulindex SBR ;
mulindex: NUMLIT numtail ;
numtail: CM NUMLIT numtail | ;
arr_val: SBL numBlist SBR ;
numBlist: SBL NUMLIT SBR numBtail;
numBtail: CM SBL NUMLIT SBR numBtail |;
	//5
expr: expr1 MOR expr1 | expr1 ;
expr1: expr2 (EQ | NEQ | ASG | SL | GT | GEQ | SEQ) expr2 | expr2 ;
expr2: expr2 (AND | OR) expr3 | expr3 ; 
expr3 : expr3 (ADD | SUB) expr4 | expr4 ; 	
expr4 : expr4 (MUL | DIV | MOD) expr5 | expr5 ; 
expr5 : NOT expr5 | expr6 ; 
expr6 : SUB expr6 | expr7 ; 	
expr7 : expr7 (SBL CM SBR) | expr8 ; 	
expr8 : lit | PRL expr PRR | Newline;
	//6 

var_decl: (prida_type | DYN) IDENTIFIER expr* | obvar | arr_type IDENTIFIER ;
obvar: VAR IDENTIFIER SDIV expr;
func_decl: FUN funcall_stmt Newline (rt_stmt | blk_stmt)*;
param: data_type ('&' IDENTIFIER | IDENTIFIER) ;
param_cmlist: param CM param_cmlist ;

 	//7
stmt: var_decl | asg_stmt | if_stmt | for_stmt | break_stmt | con_stmt | rt_stmt | funcall_stmt | blk_stmt ;
asg_stmt: expr SBL index_op SBR  (ASG expr)+ ;
index_op: expr | expr CM index_op;  
if_stmt: IF PRL expr PRR stmt (EIF PRL expr PRR stmt)* (EL stmt)?;
for_stmt: FOR IDENTIFIER UNT expr BY expr stmt;
break_stmt: BRK;
con_stmt: CNT;
funcall_stmt: IDENTIFIER PRL (param param_cmlist)* PRR;
rt_stmt: RT expr*;
blk_stmt: BG stmt* END ;

//Lexer
NUMLIT: Digit+ ((DOT? Digit+ (EXPO)?) | EXPO);
BOOLIT: TRUE | FALSE; 
STRLIT: DQUOTE ( (ESCCHAR | STRCHAR)*) DQUOTE {self.text=self.text[1:-1]}; // [1:-1]
fragment DQUOTE  : '"';
fragment STRCHAR : ~[\\'"];
fragment ESCCHAR : (('\\b')|('\\f')|('\\r')|('\\n')|('\\t')|('\\\'')|('\\\\')|('\'"')); // \b \f \r \n \t ' \\ '"
fragment ILLESC  : ('\\' ~[bfrnt\\']) | ('\'' ~["]);
fragment SIGN: ADD | SUB;
fragment EXPO: Digit? [eE] SIGN? Digit+;

COMMENT_TEXT: '##' .*? -> skip ;

	// 3.4
TRUE: 'true';
FALSE: 'false';
NUM: 'number';
BOOL: 'bool';
STR: 'string';
RT: 'return';
VAR: 'var';
DYN: 'dynamic';
FUN: 'func';
FOR: 'for';
UNT: 'until';
BY: 'by';
BRK: 'break';
CNT: 'continue';
IF: 'if';
EL: 'else';
EIF: 'elif';
BG: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

	// 3.5
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQ: '=';
SEQ: '<=';
SDIV: '<-';
NEQ: '!=';
SL: '<';
GT: '>';
GEQ: '>=';
MOR: '...';
ASG: '==';

	// 3.6
PRL: '(';
PRR: ')';
SBL: '[';
SBR: ']';
CBL: '{';
CBR: '}';
DOT: '.';
CM: ',';
SM: ';';
CL: ':';

Digit: [0-9];
Letter: [A-Za-z];
Newline: '\n'+;
	// 3.3
IDENTIFIER: [_a-zA-Z][_a-zA-Z0-9]* ;
	
// 3.1
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
UNCLOSE_STRING	: DQUOTE (ESCCHAR | STRCHAR)* EOF {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE	: DQUOTE ((ESCCHAR | STRCHAR)*? ILLESC ) {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: .{raise ErrorToken(self.text)};