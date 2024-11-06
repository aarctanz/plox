from pathlib import Path
from sys import argv

INDENTATION = "    "

DEFAULT_IMPORT = ["from abc import ABC, abstractmethod"]
EXPRESSION_IMPORT = DEFAULT_IMPORT 


def defineVisitors(file, basename: str, types: list[str]):
    file.write(f"class {basename}Visitor(ABC):\n")
    for i in types:

        file.write(f"{INDENTATION}@abstractmethod\n")
        file.write(f"{INDENTATION}def visit_{i.split(":")[0].strip().lower()}_{basename.lower()}(self,expr):\n")
        file.write(f"{INDENTATION}{INDENTATION}pass")
        file.write("\n\n")


def defineTypes(file, base_name: str, class_name: str, fields: str) -> None:
    file.write(f'class {class_name}({base_name}):\n')
    file.write(f'{INDENTATION}def __init__(self, {fields}) -> None:\n')
    for i in fields.split(","):
        file.write(f"{INDENTATION}{INDENTATION}self.{i}={i}\n")
    file.write('\n')

    file.write(f'{INDENTATION}')
    file.write(f'def accept(self, visitor) -> None:')
    file.write('\n')
    file.write(f'{INDENTATION * 2}')
    file.write(f'return visitor.visit_{class_name.lower()}_{base_name.lower()}(self)')
    file.write('\n\n')


def defineAst(filename, basename, types: list[str], importstmt):

    with open(filename, "w") as file:
        for i in importstmt:
            file.write(i)
            file.write("\n")
        file.write("\n")
        defineVisitors(file, basename, types)

        file.write(f"class {basename}(ABC):\n")
        file.write(f"{INDENTATION}@abstractmethod\n")
        file.write(f"{INDENTATION}def accept(self, visitor):\n")
        file.write(f"{INDENTATION}{INDENTATION}pass")
        file.write(f"\n\n")

        for i in types:
            classname = i.split(":")[0].strip()
            fields = i.split(":")[1].strip()
            defineTypes(file, basename, classname, fields)


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
            "Binary   : left, operator, right",
            "Grouping : expression",
            "Literal  : value",
            "Unary    : operator, right",
        ],
        EXPRESSION_IMPORT,
    )

if __name__=="__main__":
    main()