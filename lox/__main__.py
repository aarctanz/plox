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
    main(argv[1:])
    # expression = expr.Binary(
    #     expr.Unary(
    #         tokens.Token(tokens.TokenType.MINUS, "-", None, 1),
    #         expr.Literal(123)
    #     ),
    #     tokens.Token(tokens.TokenType.STAR, "*", None, 1),
    #     expr.Grouping(expr.Literal(45.67))
    # )

    # printer = astprinter.AstPrinter()
    # print(printer.print(expression))

    # printer = astprinter.RPNprint()
    # print(printer.print(expression))