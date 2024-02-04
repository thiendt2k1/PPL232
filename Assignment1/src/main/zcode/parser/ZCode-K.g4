// My ID: 1952310

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}


program: many_decl EOF ;

/**** PROGRAM STRUCTURE ****/

many_decl: decl decl_tail;
decl_tail: NEWLINE+ decl decl_tail | ;
decl: var_decl | func_decl ;

var_decl: VAR ID value_init | key_word single_decl | array_decl ;

key_word: DYNAMIC | primitive_type;

single_decl : ID value_init?;

value_init : ASSIGN exp;

array_decl : primitive_type ID LSB dim_list RSB value_init? ;

func_decl : FUNC ID LB nullable_param_list RB NEWLINE* end_stmt?; 
nullable_param_list : param_decl param_list_tail | ;
param_list_tail : CM param_decl param_list_tail | ;
end_stmt : return_stmt | block_stmt ;

param_decl : primitive_type single_decl ;

/**** TYPE AND VALUE ****/
data_type: primitive_type | arr_type;

primitive_type: NUMBER | BOOLEAN | STRING;

arr_type: primitive_type LSB dim_list RSB;
dim_list: dim_size dim_tail | dim_tail;
dim_tail: CM dim_size dim_tail | ;
dim_size: ( '0' | INTLIT);																	// required "The lower bound is always 0"

/**** EXPRESSIONS ****/

exp: LB exp1 RB | exp1;
exp1: exp1 LSB NUMLIT RSB | exp2;	
exp2: exp3 SUB exp2 | exp3;	
exp3: exp4 NOT exp3 | exp4;	
exp4: exp4 ( MUL | DIV | MOD ) exp5 | exp5;
exp5: exp5 ( ADD | SUB ) exp6 | exp6;
exp6: exp6 ( AND | OR ) exp7 | exp7;
exp7: exp8 ( EQUAL | EQUAL_STR | NOT_EQUAL | LT | GT | LTE | GTE ) exp8 | exp8;
exp8: literal ( TRIPDOT ) literal | literal;

literal: NUMLIT | BOOLLIT | STRINGLIT ;

/**** STATEMENTS ****/

stmt : var_decl_stmt NEWLINE+
	 | assign_stmt  NEWLINE+
	 | if_stmt  NEWLINE+
	 | for_stmt  NEWLINE+
	 | break_stmt  NEWLINE+
	 | continue_stmt  NEWLINE+
	 | return_stmt  NEWLINE+
	 | func_call_stmt  NEWLINE+
	 | block_stmt NEWLINE+
	 ;

var_decl_stmt : var_decl ;

assign_stmt : lhs ASSIGN exp ;
lhs : ID | arr_element ;
arr_element: ID id_list;
id_list: LSB NUMLIT RSB id_list?;

if_stmt : IF condition_exp NEWLINE* stmt NEWLINE+ elif_stmt?;
elif_stmt : ELIF condition_exp NEWLINE+ stmt elif_stmt? | else_stmt ;
else_stmt : ELSE stmt NEWLINE+;
condition_exp : LB exp RB ;

for_stmt : FOR ID UNTIL condition_exp BY NUMLIT NEWLINE* stmt;

break_stmt : BREAK;

continue_stmt : CONTINUE;

return_stmt : RETURN exp?;

func_call_stmt : ID LB arg_list RB;
arg_list : ID arg_tail | ;
arg_tail : CM ID arg_tail | ;

block_stmt : BEGIN block_body END;
block_body : stmt* | NEWLINE+;

/**** LEXER ****/

/**** COMMENT ****/
COMMENT: DOUBLE_HASH ~[\n]* -> skip;

/**** KEYWORD ****/

DOUBLE_HASH : '##';

TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOLEAN: 'boolean';
STRING: 'string';

RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';

FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';

IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

/**** OPERATORS ****/
// Calculation
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
//Boolean
NOT: 'not';
AND: 'and';
OR: 'or';
// Assignments
EQUAL: '=';
ASSIGN: '<-';
// Comparation
NOT_EQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
// String
TRIPDOT: '...';
EQUAL_STR: '==';

/**** SEPERATORS ****/
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
CM: ',';
NEWLINE: '\n'+ -> skip;
SING_QUOTE: '\'';

/**** LITERALS ****/
INTLIT: [1-9]DIGIT*;
NUMLIT: ( SUB? ( '0' | NONZERO_DECIMAL) ('.' DIGIT*)?							// 0, 999, 12. OR 12.3
		| SUB? ( '0' | NONZERO_DECIMAL) ('.' DIGIT*)? [eE] [+-]? DIGIT+ 		// 12.3e3 OR 12E3 12.3E-30
		) ;

BOOLLIT: TRUE | FALSE ;

STRINGLIT:  DQUOTE ( (ESCCHAR | STRCHAR)*) DQUOTE {self.text=self.text[1:-1]}; // [1:-1]

/**** IDENTIFIERS ****/



/**** FRAGMENTS ****/
fragment DIGIT: [0-9];
fragment NONZERO_DECIMAL: [1-9]DIGIT*;
// fragment ESC_SEQ: '\\' [btnfr\\'];
// fragment STR_CHAR: ~[\b\f\r\n\t"\\] | '\'' | '\\' | '\'"' ;
// fragment ESC_ILLEGAL: ('\\' ~['btnfr\\]) | ~'\\';

// WS: [ \t\b\f\n]+ -> skip;
// ERROR_TOKEN: . {raise ErrorToken(self.text)};
// UNCLOSE_STRING: '"' (ESC_SEQ | STR_CHAR)* EOF { raise UncloseString(self.text[1:])};
// ILLEGAL_ESCAPE: '"' (ESC_SEQ | STR_CHAR)* ESC_ILLEGAL { raise IllegalEscape(self.text[1:-1] )};

// STRS:
fragment DQUOTE  : '"';
fragment STRCHAR : ~[\\'"];
fragment ESCCHAR : (('\\b')|('\\f')|('\\r')|('\\n')|('\\t')|('\\\'')|('\\\\')|('\'"')); // \b \f \r \n \t ' \\ '"
fragment ILLESC  : ('\\' ~[bfrnt\\']) | ('\'' ~["]);

ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING	: '"' (ESCCHAR | STRCHAR)* EOF {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE	: '"' ((ESCCHAR | STRCHAR)*? ILLESC ) {raise IllegalEscape(self.text[1:])};
ERROR_CHAR: .{raise ErrorToken(self.text)};