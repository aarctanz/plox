from sys import argv
from lox.lox import Lox
def main(argv):
    if len(argv)>1:
        print("Usage: lox [script]")
        exit(64)
    if len(argv)==1:
        Lox.runFile(argv[0])
        
    else:
        Lox.runPrompt()



if __name__=="__main__":
    main(argv[1:])