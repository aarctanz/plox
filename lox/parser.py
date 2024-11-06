# from lox.tokens import Token, TokenType
# from lox.expr import Expr, Binary, Literal, Grouping
# class Parser:
#     def __init__(self, tokens: list[Token]) -> None:
#         self.tokens = tokens
#         self.current = 0
    
#     def peek(self):
#         return self.tokens[self.current]

#     def isAtEnd(self):
#         return self.peek().type == TokenType.EOF
    
#     def check(self, typ):
#         if(self.isAtEnd()):
#             return False
#         return self.peek().type==typ
#     def previous(self):
#         return self.tokens[self.current-1]
    
#     def advance(self):
#         if(not self.isAtEnd()):
#             self.current+=1
#         return self.previous()
    
#     def match(self, *types):
#         for i in types:
#             if self.check(i):
#                 self.advance()
#                 return True
            
#         return False
    
#     def primary(self):
#         if self.match(TokenType.FALSE):
#             return Literal(False)
#         if self.match(TokenType.TRUE):
#             return Literal(True)
#         if self.match(TokenType.NULL):
#             return Literal(None)
        
#         if self.match(TokenType.NUMBER, TokenType.STRING):
#             return Literal(self.previous().literal)
        
#         if self.match(TokenType.LEFT_PAREN):
#             expr = self.expression()
#             self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
#             return Grouping(expr)

#     def equality(self) -> Expr:
#         expr = self.comparison()

#         while(self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL)):
#             operator = self.previous()
#             right = self.comparison()
#             expr = Binary(expr, operator, right)

#         return expr

#     def expression(self):
#         return self.equality()
    