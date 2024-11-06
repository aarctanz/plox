from typing import Any
from enum import Enum

class TokenType(Enum):
    LEFT_PAREN = '('
    RIGHT_PAREN = ')'
    LEFT_BRACKET = '['
    RIGHT_BRACKET = ']'
    LEFT_BRACE = '{'
    RIGHT_BRACE = '}'
    COMMA = ','
    DOT = '.'
    MINUS = '-'
    PLUS = '+'
    COLON = ':'
    SEMICOLON = ';'
    SLASH = '/'
    BACKSLASH = '\\'
    STAR = '*'
    UNDERSCORE = '_'
    QUOTATION_MARK = '?'
    PERCENT = '%'
    AT_SIGN = '@'
    AMPERSAND = '&'
    DOLLAR_SIGN = '$'
    CARET = '^'
    TILDE = '~'
    PIPE = '|'

    # One or two+ character tokens
    BANG = '!'
    BANG_EQUAL = '!='
    EQUAL = '='
    EQUAL_EQUAL = '=='
    GREATER = '>'
    GREATER_EQUAL = '>='
    LESS = '<'
    LESS_EQUAL = '<='
    ARROW = '=>'
    SHEBANG = '#!'
    HASH = '#'
    ELLIPSIS = '...'
    TRIPLE_QUOTE = '"""'

    # Keywords
    GET = 'get'
    SET = 'set'
    DELETE = 'delete'
    AND = 'and'
    OR = 'or'
    NOT = 'not'
    IF = 'if'
    ELSE = 'else'
    SWITCH = 'switch'
    CASE = 'case'
    WHEN = 'when'
    WHILE = 'while'
    UNLESS = 'unless'
    BREAK = 'break'
    FOR = 'for'
    IN = 'in'
    DO = 'do'
    NULL = 'null'
    TRUE = 'true'
    FALSE = 'false'
    TRY = 'try'
    CATCH = 'catch'
    FINALLY = 'finally'
    NEW = 'new'
    CLASS = 'class'
    EXTENDS = 'extends'
    SUPER = 'super'
    SELF = 'self'
    THIS = 'this'
    INTERFACE = 'interface'
    IMPLEMENTS = 'implements'
    FUNCTION = 'function'
    RETURN = 'return'
    GENERATOR = 'generator'
    YIELD = 'yield'
    ASYNC = 'async'
    AWAIT = 'await'
    STATIC = 'static'
    LAMBDA = 'lambda'
    CONST = 'const'
    LET = 'let'
    VAR = 'var'
    PRIVATE = 'private'
    END = 'end'
    PRINT = 'print'

    # String starters
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'

    # New line
    NEW_LINE = '\n'

    # Space
    TAB = '\t'
    SPACE = ' '

    # String terminator
    NULL_CHARACTER = '\0'

    # End-user identifiers
    IDENTIFIER = 'identifier'
    INTEGER = 'int'
    FLOAT = 'float'
    STRING = 'str'
    NUMBER = 'num'

    # end-of-file
    EOF = ''

_keywords = (
    'true', 'false', 'null', 'and', 'or', 'if', 'else', 'function', 'return',
    'for', 'class', 'super', 'this', 'const', 'let', 'while', 'var', 'print'
)

KEYWORDS = {key: TokenType(key) for key in _keywords}

class Token:
    def __init__(self, typ: TokenType, lexeme: str, literal: Any, line: int):
        self.type = typ
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
    
    def __str__(self):
        return f"{self.type.name} {self.lexeme} {self.literal}"

    def __repr__(self):
        return f"TOKEN:{self.__str__()}"