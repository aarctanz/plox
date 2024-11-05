from pathlib import Path
from sys import argv

INDENTATION = "    "

DEFAULT_IMPORT = ["from abc import ABC, abstractmethod"]
EXPRESSION_IMPORT = DEFAULT_IMPORT + ["from lox.lox import Lox"]


def defineVisitors(file, basename: str, types: list[str]):
    file.write(f"class {basename}Visitor(ABC):\n")
    for i in types:

        file.write(f"{INDENTATION}@abstractmethod\n")
        file.write(f"def visit_{i.split(":")[0].strip().lower()}_{basename.lower()}:\n")
        file.write(f"{INDENTATION}{INDENTATION}pass")
        file.write("\n")

'''
class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: ExprVisitor):
        pass
'''

'''
class Assign(Expr):
    def __init__(self, name: Token, value: Expr) -> None:
        self.name = name
        self.value = value

    def accept(self, visitor: ExprVisitor) -> None:
        return visitor.visit_assign_expr(self)
'''
def defineTypes(file, base_name: str, class_name: str, fields) -> None:
    file.write(f'class {class_name}({base_name}):')
    file.write('\n')
    file.write(f'{INDENTATION}')
    file.write(f'def __init__(self, {", ".join(fields)}) -> None:')
    file.write('\n')

    for field in fields:
        attr = field.split(':')[0]
        file.write(f'{INDENTATION * 2}self.{attr} = {attr}')
        file.write('\n')

    file.write('\n')
    file.write(f'{INDENTATION}')
    file.write(f'def accept(self, visitor: {base_name}Visitor) -> None:')
    file.write('\n')
    file.write(f'{INDENTATION * 2}')
    file.write(f'return visitor.visit_{class_name.lower()}_{base_name.lower()}(self)')
    file.write('\n')


def defineAst(filename, basename, types: list[str], importstmt):

    with open(filename, "w") as file:
        for i in importstmt:
            file.write(i)
            file.write("\n")

        defineVisitors(file, basename, types)

        file.write(f"class {basename}(ABC):\n")
        file.write(f"{INDENTATION}@abstractmethod\n")
        file.write(f"{INDENTATION}def accept(self, visitor):\n")
        file.write(f"{INDENTATION}{INDENTATION}pass")
        file.write(f"\n")

        for i in types:
            classname, fields = i.split(":")

        # defineTypes(file, "Expr", classname.strip(), fields)


def main():
    if len(argv) < 2:
        print("Output directory necessary")
        exit(1)

    p = Path(argv[1])
    if not p.is_dir():
        print("Invalid directory")
        exit(1)

    defineAst(
        p / "expr.py",
        "Expr",
        [
            "Binary   : Expr left, Token operator, Expr right",
            "Grouping : Expr expression",
            "Literal  : Object value",
            "Unary    : Token operator, Expr right",
        ],
        EXPRESSION_IMPORT,
    )
