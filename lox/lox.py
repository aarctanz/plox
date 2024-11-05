import sys

class Lox:
    hadError = False
    
    @staticmethod
    def report(line, where, message):
        print(f"[line {line} ] Error{where}: {message}")
        Lox.hadError = True
    
    @staticmethod
    def error( line, message):
        Lox.report(line, "", message)


    @staticmethod
    def run(code):
        pass

    @staticmethod
    def runFile(filePath):
        with open(filePath, "r") as file:
            Lox.run(file.read())
            if Lox.hadError:
                sys.exit(65)
    
    @staticmethod
    def runPrompt(Lox):
        while True: 
            try:
                text = input('>>> ')
            except EOFError:
                break
            if not text:
                continue
            result = Lox.run(text)
            print(result)
            Lox.hadError = False

