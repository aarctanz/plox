from lox.scanner import Scanner

class Lox:
    hadError = False
    
    @staticmethod
    def report(line, where, message):
        print(f"[line {line} ] Error{where}: {message}")
        Lox.hadError = True
    
    @staticmethod
    def error( line: int, message: str):
        Lox.report(line, "", message)


    @staticmethod
    def run(code):
        pass
        # scanner = Scanner(code)
        # print(scanner.scanTokens())

    @staticmethod
    def runFile(filePath):
        with open(filePath, "r") as file:
            Lox.run(file.read())
            if Lox.hadError:
                exit(65)
    
    @staticmethod
    def runPrompt():
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

    @staticmethod
    def printTokens(code):
        scanner = Scanner(code)
        try:
            print((str(scanner.scanTokens())))
        except Exception as e:
            print("Error ", e.args[0])