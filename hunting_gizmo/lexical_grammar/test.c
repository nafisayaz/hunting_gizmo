


#include <test.h>
#include <stdio.h>

extern int yylex();
extern char*  yytext;

int main()
{
	int token = yylex();
		
	printf("%s ->  %d \n", yytext, token );

	while(token)
	{
		int token = yylex();
		
		printf("%s ->  %d \n", yytext, token );
	
	}
}

