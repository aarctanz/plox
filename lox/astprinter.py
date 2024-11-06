from lox import expr

class AstPrinter(expr.ExprVisitor):
    def print(self, expr: expr.Expr):
        return expr.accept(self)

    def parenthesize(self, name, *exprs):
        content = ' '.join(expression.accept(self) for expression in exprs)
        return f'({name} {content})'
    
    def visit_binary_expr(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)
    
    def visit_grouping_expr(self, expr) -> str:
        return self.parenthesize(expr.expression.value)
    
    def visit_literal_expr(self, expr) -> str:
        if expr.value==None:
            return "nil"
        return str(expr.value)
    
    def visit_unary_expr(self, expr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)
    

class RPNprint(expr.ExprVisitor):
    def print(self, expr: expr.Expr):
        return expr.accept(self)

    def parenthesize(self, name, *exprs):
        content = ' '.join(expression.accept(self) for expression in exprs)
        return f'({content} {name})'
    
    def visit_binary_expr(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)
    
    def visit_grouping_expr(self, expr) -> str:
        return self.parenthesize(expr.expression.value)
    
    def visit_literal_expr(self, expr) -> str:
        if expr.value==None:
            return "nil"
        return str(expr.value)
    
    def visit_unary_expr(self, expr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)
    