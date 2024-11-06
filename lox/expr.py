from abc import ABC, abstractmethod

class ExprVisitor(ABC):
    @abstractmethod
    def visit_binary_expr(self,expr)->str:
        pass

    @abstractmethod
    def visit_grouping_expr(self,expr)->str:
        pass

    @abstractmethod
    def visit_literal_expr(self,expr)->str:
        pass

    @abstractmethod
    def visit_unary_expr(self,expr)->str:
        pass

class Expr(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Binary(Expr):
    def __init__(self, left, operator, right) -> None:
        self.left=left
        self. operator= operator
        self. right= right

    def accept(self, visitor) -> None:
        return visitor.visit_binary_expr(self)

class Grouping(Expr):
    def __init__(self, expression) -> None:
        self.expression=expression

    def accept(self, visitor) -> None:
        return visitor.visit_grouping_expr(self)

class Literal(Expr):
    def __init__(self, value) -> None:
        self.value=value

    def accept(self, visitor) -> None:
        return visitor.visit_literal_expr(self)

class Unary(Expr):
    def __init__(self, operator, right) -> None:
        self.operator=operator
        self. right= right

    def accept(self, visitor) -> None:
        return visitor.visit_unary_expr(self)

