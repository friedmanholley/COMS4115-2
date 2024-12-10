import sys
from codegen import CodeGenerator
from lexer import Lexer
from parser import Parser

if __name__ == "__main__":
    # Check if an input file is provided
    if len(sys.argv) < 2:
        print("Usage: python3 codegen.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read the source code
    with open(input_file, 'r') as f:
        source_code = f.read()

    # Run the lexer
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()

    # Run the parser
    parser = Parser(tokens)
    ast = parser.parse_program()

    # Run the code generator
    codegen = CodeGenerator()
    output = codegen.generate_program(ast)

    # Print the ASCII art output
    print(output)

    # Write intermediate code
    with open("intermediate_code.py", "w") as file:
        file.write(output)
