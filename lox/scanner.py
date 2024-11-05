from lox.tokens import (TokenType, Token, KEYWORDS)
from lox.lox import Lox

class Scanner:
    
    def __init__(self, source: str) -> None:
        self.source = source

        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []

    def isAtEnd(self)->bool:
        return self.current >= len(self.source)
    
    def peek(self)->str:
        if(self.isAtEnd()):
            return "\0"
        return self.source[self.current]
    
    def peekNext(self)->str:
        if(self.current+1 >= len(self.source)):
            return "\0"
        return self.source[self.current+1]

    def advance(self):
        res = self.source[self.current]
        self.current+=1
        return res
    
    def match(self, expected: str):
        if self.isAtEnd():
            return False
        if (self.source[self.current]) != expected:
            return False

        self.current+=1
        return True


    def addToken(self, typ: TokenType, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(typ,text, literal, self.line))
    
    def string(self) -> None:
        while(self.peek()!='"' and not self.isAtEnd()):
            if(self.peek()=="\n"):
                self.line+=1
            self.advance()
        
        if(self.isAtEnd()):
            Lox.error(self.line, "Unterminated string")
        
        value = self.source[self.start+1:self.current-1]
        self.addToken(TokenType.STRING, value)
    
    def number(self) -> None:
        while(self.peek().isdigit()):
            self.advance()
        
        if(self.peek()=="." and self.peekNext().isdigit()):
            while(self.peek().isdigit()):
                self.advance()
        
        value = float(self.source[self.start:self.current+1])
        self.addToken(TokenType.NUMBER, value)

    def identifier(self) -> None:
        while(self.peekNext().isalnum()):
            self.advance()
        text = self.source[self.start:self.current]
        typ = KEYWORDS.get(text)
        if typ == None:
            self.addToken(TokenType.IDENTIFIER)
        else:
            self.addToken(typ)

    
    def scanToken(self) -> None:
        c = self.advance()
        
        if c == '(': 
            self.addToken(TokenType.LEFT_PAREN)
        elif c == ')': 
            self.addToken(TokenType.RIGHT_PAREN)
        elif c == '{': 
            self.addToken(TokenType.LEFT_BRACE)
        elif c == '}': 
            self.addToken(TokenType.RIGHT_BRACE)
        elif c == ',': 
            self.addToken(TokenType.COMMA)
        elif c == '.': 
            self.addToken(TokenType.DOT)
        elif c == '-': 
            self.addToken(TokenType.MINUS)
        elif c == '+': 
            self.addToken(TokenType.PLUS)
        elif c == ';': 
            self.addToken(TokenType.SEMICOLON)
        elif c == '*': 
            self.addToken(TokenType.STAR) 
        elif c == "!":
            if self.match("="):
                self.addToken(TokenType.BANG_EQUAL)
            else:
                self.addToken(TokenType.BANG)
        elif c == "=":
            if self.match("="):
                self.addToken(TokenType.EQUAL_EQUAL)
            else:
                self.addToken(TokenType.EQUAL)
        elif c == ">":
            if self.match("="):
                self.addToken(TokenType.GREATER_EQUAL)
            else:
                self.addToken(TokenType.GREATER)
        elif c == "<":
            if self.match("="):
                self.addToken(TokenType.LESS_EQUAL)
            else:
                self.addToken(TokenType.LESS)
        elif c == "/":
            if(self.match("/")):
                while(self.peek()!="\n" and not self.isAtEnd()):
                    self.advance()
            else:
                self.addToken(TokenType.SLASH)
        
        elif c==" " or c=="\t" or c=="\r":
            return
        elif c == "\n":
            self.line+=1
        
        elif c == '"':
            self.string()
        
        elif c.isdigit():
            self.number()
        elif c.isalpha():
            self.identifier()

        else:
            Lox.error(self.line, f"Unidentified character {c}.")
    

    
    def scanTokens(self) -> list[Token]:

        while(not self.isAtEnd()):
            self.start = self.current
            self.scanToken()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens