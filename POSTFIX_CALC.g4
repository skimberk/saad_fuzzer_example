grammar POSTFIX_CALC;

expr
   : NUMBER
   | expr ' ' expr ' ' OPERATOR;

OPERATOR : '+' | '-' | '*';
// OPERATOR : '+' | '-' | '*' | '/'; // This allows division by zero!


// Borrowed from JSON.g4 from antlr4-grammars/

NUMBER
   : '-'? INT ('.' [0-9] +)? EXP?
   ;


fragment INT
   : '0' | [1-9] [0-9]*
   ;

// no leading zeros

fragment EXP
   : [Ee] [+\-]? INT
   ;