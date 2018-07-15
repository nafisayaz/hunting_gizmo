

%{

//#include "test.h"

#include<stdio.h>	


typedef struct lexer
{
	char* text;
	int len;
}lexer;


typedef struct grammar grammar;

#include "parser.h"

#define YY_DECL int yylex (lexer * l)

#define SAVE do{ l->text = yytext; l->len = yyleng; }while(0)

#define PRINTF(...)  do{}while(0)


%}


WHITE_SPACE					" "

I							"i"
HE							"he"
SHE							"she"
WE							"we"

IS							"is"
AM							"am"
ARE							"are"

A							"a" 
AN							"an"
THE							"the"

FROM						"from" 
TO							"to"
IN							"in"
INTO						"into"
ON							"on"


GENERAL_WORD				[a-zA-Z]+


%%


{WHITE_SPACE}				{ SAVE; PRINTF("string_type: %s\n", yytext); return I; }

{I}							{ SAVE; PRINTF("string_type: %s\n", yytext); return I; }
{HE}						{ SAVE; PRINTF("string_type: %s\n", yytext); return HE; }
{SHE}						{ SAVE; PRINTF("string_type: %s\n", yytext); return SHE; }
{WE}						{ SAVE; PRINTF("string_type: %s\n", yytext); return WE; }

{IS}						{ SAVE; PRINTF("string_type: %s\n", yytext); return IS; }
{AM}						{ SAVE; PRINTF("string_type: %s\n", yytext); return AM; }
{ARE}						{ SAVE; PRINTF("string_type: %s\n", yytext); return ARE; }

{A}							{ SAVE; PRINTF("string_type: %s\n", yytext); return A; }
{AN}						{ SAVE; PRINTF("string_type: %s\n", yytext); return AN; }
{THE}						{ SAVE; PRINTF("string_type: %s\n", yytext); return THE; }

{FROM}						{ SAVE; PRINTF("string_type: %s\n", yytext); return FROM; }
{IN}						{ SAVE; PRINTF("string_type: %s\n", yytext); return IN; }
{INTO}						{ SAVE; PRINTF("string_type: %s\n", yytext); return INTO; }
{ON}						{ SAVE; PRINTF("string_type: %s\n", yytext); return ON; }
{GENERAL_WORD}				{ SAVE; PRINTF("string_type: %s\n", yytext); return GENERAL_WORD; }
.							{}


%%


int yywrap() { return 1; }



