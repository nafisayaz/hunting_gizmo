

%{

#include<stdio.h>
#include<string.h>


typedef struct lexer
{
	char* text;
	int len;
}lexer;

typedef struct grammar{} grammar;

int yylex (struct lexer * l);

#define LOG do{ printf("\e[0;33m%s, %d, %s, %d  \e[0m\n", __FILE__, __LINE__, l->text, l->len); }while(0)

#define COPY(x, y)  do{ x = malloc(strlen(y)); strcpy(x,y); }while(0) 


void yyerror(lexer* l, grammar * p, char const *s){ printf("\e[1;31m%s\n\n\n\n", s); } 

%}


%token I
%token HE
%token SHE
%token WE

%token IS
%token AM
%token ARE

%token GOING

%token A
%token AN
%token THE

%token TO
%token FROM
%token ON
%token IN
%token INTO


%token WHITE_SPACE

%token GENERAL_WORD


%lex-param		{ lexer * l }
%parse-param	{ lexer * l }
%parse-param	{ grammar * p }


%union
{
	char* s;
}


%type<s> SUBJECT
%type<s> PRONOUN
%type<s> H_VERB
%type<s> VERB
%type<s> PREPOSITION
%type<s> ARTICLE


%%


grammar 		:	%empty												{}
				|	sentences											{}

sentences		:	sentence											{}
				|	sentences sentence									{}
				
sentence		:	sent '.'											{ LOG; printf("  ---------> %s", l->text ); }

sent			: 	clause												{ LOG; }
				| 	clause WHITE_SPACE PREPOSITION SUBJECT				{ LOG; }
				|	clause WHITE_SPACE PREPOSITION ARTICLE SUBJECT		{ LOG; }

clause			: 	SUBJECT WHITE_SPACE H_VERB WHITE_SPACE VERB			{ LOG; }

SUBJECT			:	GENERAL_WORD										{ LOG; COPY($$, l->text); }
				|	PRONOUN												{ LOG; COPY($$, l->text); }


PRONOUN			:	I													{ COPY($$, l->text); LOG; }
				|	HE													{ LOG; COPY($$, l->text); }
				|	SHE													{ LOG; COPY($$, l->text); }


H_VERB			:	IS													{ LOG; COPY($$, l->text); }
				|	AM													{ COPY($$, l->text); LOG; }
				|	ARE													{ LOG; COPY($$, l->text); }

VERB			:	GOING												{ LOG; COPY($$, l->text);}

PREPOSITION		:	TO													{ LOG; COPY($$, l->text); }
				|	FROM												{ LOG; COPY($$, l->text); }
				|	IN													{ LOG; COPY($$, l->text); }
				|	ON													{ LOG; COPY($$, l->text); }
				|	INTO												{ LOG; COPY($$, l->text); }


ARTICLE			:	A													{ LOG; COPY($$, l->text); }
				|	AN													{ LOG; COPY($$, l->text); }
				|	THE													{ LOG; COPY($$, l->text); }



%%


int main()
{
	lexer l;
	grammar p;

	yyparse(&l, &p);
}


