from sys import argv
from lox.lox import Lox
from lox  import expr, astprinter
from lox import tokens
def main(argv):
    if len(argv)>2:
        print("Usage: lox [script]")
        exit(64)
    if len(argv)==1:
        Lox.runFile(argv[0])
    if len(argv)==2:
        if argv[0]!="tokenize":
            print("Unrecognized Command")
            exit(64)
        else:
            with open(argv[1]) as file:
                source = file.read()
                Lox.printTokens(source)
    else:
        Lox.runPrompt()



if __name__=="__main__":
    # main(argv[1:])
    expression = expr.Binary(
        expr.Unary(
            tokens.Token(tokens.TokenType.MINUS, "-", None, 1),
            expr.Literal(123)
        ),
        tokens.Token(tokens.TokenType.STAR, "*", None, 1),
        expr.Grouping(expr.Literal(45.67))
    )

    printer = astprinter.AstPrinter()
    print(printer.print(expression))

    printer = astprinter.RPNprint()
    print(printer.print(expression))
    minus_token = tokens.Token(tokens.TokenType.MINUS, "-", None, 1)
    plus_token = tokens.Token(tokens.TokenType.PLUS, "+", None, 1)
    bang_token = tokens.Token(tokens.TokenType.BANG, "!", None, 1)

    # Step 2: Create the inner expression (3 + 2)
    expr1 = expr.Binary(expr.Literal(3), plus_token, expr.Literal(2))  # (3 + 2)

    # Step 3: Create the expression for 5 - (3 + 2)
    expr2 = expr.Binary(expr.Literal(5), minus_token, expr1)      # 5 - (3 + 2)

    # Step 4: Apply the unary "!" operator to the whole expression
    final_expr = expr.Unary(bang_token, expr2)               # !(5 - (3 + 2))
    printer = astprinter.AstPrinter()
    print(printer.print(final_expr))

    printer = astprinter.RPNprint()
    print(printer.print(final_expr))