class CodeGenerator:
    def __init__(self):
        # Define grid flag
        self.is_grid = 0
        
        # Define standard dimensions
        self.standard_width = 15
        self.standard_height = 6
        
        # Templates for images (dog, cat, etc.) generated using chatGPT.
        self.templates = {
            'dog': [
                "^..^      /",
                "/_/\\_____/",
                "   /\\   /\\ "
            ],
            'cat': [
                " /\\_/\\ ",
                "( o.o )",
                " > ^ < "
            ],
            'bird': [
                "  /\\_/\\  ",
                "(  • •  )",
                "  =_Y_=  ",
                "   `-`   "
            ],
            'sun': [
                "   \\ | /   ",
                " --   *   -- ",
                "   / | \\   "
            ],
            'tree': [
                "   *   ",
                "  ***  ",
                " ***** ",
                "   |   ",
                "   |   "
            ],
            'house': [
                "   /\\   ",
                "  /  \\  ",
                " /____\\ ",
                "|      |",
                "|______|"
            ]
        }   


        # ASCII font for WRITE statements, A-Z, 0-9, [?.!, ]. 
        # What to do with punctuation?
        # font adapted from https://fsymbols.com/generators/carty/
        self.char_templates = {
            'A': [
                "╭━━━╮",
                "┃╭━╮┃",
                "┃┃ ┃┃",
                "┃╰━╯┃",
                "┃╭━╮┃",
                "╰╯ ╰╯"
            ],
            'B': [
                "╭━━╮ ",
                "┃╭╮┃ ",
                "┃╰╯╰╮",
                "┃╭━╮┃",
                "┃╰━╯┃",
                "╰━━━╯"
            ],
            'C': [
                "╭━━━╮",
                "┃╭━╮┃",
                "┃┃ ╰╯",
                "┃┃ ╭╮",
                "┃╰━╯┃",
                "╰━━━╯"
            ],
            'D': [
                "╭━━━╮",
                "╰╮╭╮┃",
                " ┃┃┃┃",
                " ┃┃┃┃",
                "╭╯╰╯┃",
                "╰━━━╯"
            ],  
            'E': [
                "╭━━━╮",
                "┃╭━━╯",
                "┃╰━━╮",
                "┃╭━━╯",
                "┃╰━━╮",
                "╰━━━╯",
            ],
            'F': [
                "╭━━━╮",
                "┃╭━━╯",
                "┃╰━━╮",
                "┃╭━━╯",
                "┃┃   ",
                "╰╯   "
            ],
            'G': [
                "╭━━━╮",
                "┃╭━╮┃",
                "┃┃ ╰╯",
                "┃┃╭━╮",
                "┃╰┻ ┃",
                "╰━━━╯"
            ],
            'H': [               
                "╭╮ ╭╮",
                "┃┃ ┃┃",
                "┃╰━╯┃",
                "┃╭━╮┃",
                "┃┃ ┃┃",
                "╰╯ ╰╯"
            ],
            'I': [
                '╭━━╮',
                '╰┫┣╯',
                ' ┃┃ ',
                ' ┃┃ ',
                '╭┫┣╮',
                '╰━━╯'
            ],
            'J': [
                '  ╭╮',
                '  ┃┃',
                '  ┃┃',
                '╭╮┃┃',
                '┃╰╯┃',
                '╰━━╯'
            ],
            'K': [
                '╭╮╭━╮',
                '┃┃┃╭╯',
                '┃╰╯╯ ',
                '┃╭╮┃ ',
                '┃┃┃╰╮',
                '╰╯╰━╯'
            ],
            'L': [
                '╭╮   ',
                '┃┃   ',
                '┃┃   ',
                '┃┃ ╭╮',
                '┃╰━╯┃',
                '╰━━━╯'
            ],
            'M': [
                '╭━╮╭━╮',
                '┃┃╰╯┃┃',
                '┃╭╮╭╮┃',
                '┃┃┃┃┃┃',
                '┃┃┃┃┃┃',
                '╰╯╰╯╰╯'
            ],
            'N': [
                '╭━╮ ╭╮',
                '┃┃╰╮┃┃',
                '┃╭╮╰╯┃',
                '┃┃╰╮┃┃',
                '┃┃ ┃┃┃',
                '╰╯ ╰━╯'
            ],
            'O': [
                '╭━━━╮',
                '┃╭━╮┃',
                '┃┃ ┃┃',
                '┃┃ ┃┃',
                '┃╰━╯┃',
                '╰━━━╯'
            ],
            'P': [
                '╭━━━╮',
                '┃╭━╮┃',
                '┃╰━╯┃',
                '┃╭━━╯',
                '┃┃   ',
                '╰╯   '
            ],
            'Q': [
                '╭━━━╮',
                '┃╭━╮┃',
                '┃┃ ┃┃',
                '┃┃ ┃┃',
                '┃╰━╯┃',
                '╰━━╮┃',
                '   ╰╯'
            ],
            'R': [
                '╭━━━╮',
                '┃╭━╮┃',
                '┃╰━╯┃',
                '┃╭╮╭╯',
                '┃┃┃╰╮',
                '╰╯╰━╯'
            ],
            'S': [
                '╭━━━╮',
                '┃╭━╮┃',
                '┃╰━━╮',
                '╰━━╮┃',
                '┃╰━╯┃',
                '╰━━━╯'
            ],
            'T': [
                '╭━━━━╮',
                '┃╭╮╭╮┃',
                '╰╯┃┃╰╯',
                '  ┃┃  ',
                '  ┃┃  ',
                '  ╰╯  '
            ],
            'U': [
                '╭╮ ╭╮',
                '┃┃ ┃┃',
                '┃┃ ┃┃',
                '┃┃ ┃┃',
                '┃╰━╯┃',
                '╰━━━╯'
            ],
            'V': [
                '╭╮  ╭╮',
                '┃╰╮╭╯┃',
                '╰╮┃┃╭╯',
                ' ┃╰╯┃ ',
                ' ╰╮╭╯ ',
                '  ╰╯  '
            ],
            'W': [
                '╭╮╭╮╭╮',
                '┃┃┃┃┃┃',
                '┃┃┃┃┃┃',
                '┃╰╯╰╯┃',
                '╰╮╭╮╭╯',
                ' ╰╯╰╯ '
            ],
            'X': [
                '╭━╮╭━╮',
                '╰╮╰╯╭╯',
                ' ╰╮╭╯ ',
                ' ╭╯╰╮ ',
                '╭╯╭╮╰╮',
                '╰━╯╰━╯'
            ],
            'Y': [
                '╭╮  ╭╮',
                '┃╰╮╭╯┃',
                '╰╮╰╯╭╯',
                ' ╰╮╭╯ ',
                '  ┃┃  ',
                '  ╰╯  '
            ],
            'Z': [
                '╭━━━━╮',
                '╰━━╮━┃',
                '  ╭╯╭╯',
                ' ╭╯╭╯',
                '╭╯━╰━╮',
                '╰━━━━╯'
            ],
            '0': [
                "╭━━━╮",
                "┃╭━╮┃",
                "┃┃\┃┃",
                "┃┃\┃┃",
                "┃╰━╯┃",
                "╰━━━╯"
            ],
            '1': [
                "  ╭╮ ",
                " ╭╯┃ ",
                " ╰╮┃ ",
                "  ┃┃ ",
                " ╭╯╰╮",
                " ╰━━╯"
            ],
            '2': [        
                "╭━━━╮",
                "┃╭━╮┃",
                "╰╯╭╯┃",
                "╭━╯╭╯",
                "┃ ╰━╮",
                "╰━━━╯"
            ],
            '3': [
                "╭━━━╮",
                "┃╭━╮┃",
                "╰╯╭╯┃",
                "╭╮╰╮┃",
                "┃╰━╯┃",
                "╰━━━╯"
            ],
            '4': [
                "╭╮ ╭╮",
                "┃┃ ┃┃",
                "┃╰━╯┃",
                "╰━━╮┃",
                "   ┃┃",
                "   ╰╯"
            ],
            '5': [
                "╭━━━╮",
                "┃╭━━╯",
                "┃╰━━╮",
                "╰━━╮┃",
                "╭━━╯┃",
                "╰━━━╯"
            ],
            '6': [
                "╭━━━╮",
                "┃╭━━╯",
                "┃╰━━╮",
                "┃╭━╮┃",
                "┃╰━╯┃",
                "╰━━━╯"
            ],
            '7': [
                "╭━━━╮",
                "┃╭━╮┃",
                "╰╯╭╯┃",
                "  ┃╭╯",
                "  ┃┃",
                "  ╰╯"
            ],
            '8': [
                "╭━━━╮",
                "┃╭━╮┃",
                "┃╰━╯┃",
                "┃╭━╮┃",
                "┃╰━╯┃",
                "╰━━━╯"
            ],
            '9': [
                "╭━━━╮",
                "┃╭━╮┃",
                "┃╰━╯┃",
                "╰━━╮┃",
                "╭━━╯┃",
                "╰━━━╯"
            ],
            '?': [            
                "╭━━━╮",
                "┃╭━╮┃",
                "╰╯╭╯┃",
                "  ┃╭╯",
                "  ╭╮ ",
                "  ╰╯ "
            ],
            '!': [
                " ╭╮  ",
                " ┃┃  ",
                " ┃┃  ",
                " ╰╯  ",
                " ╭╮  ",
                " ╰╯  "
            ],
            '.': [            
                "     ",
                "     ",
                "     ",
                "     ",
                "  ╭╮ ",
                "  ╰╯ "
            ],
            ' ': [           
                "     ",
                "     ",
                "     ",
                "     ",
                "     ",
                "     "
            ],
            ',': [            
                "     ",
                "     ",
                "     ",
                "  ╭╮ ",
                "  ╰┫ ",
                "   ╯ "
            ]
        }

        # Normalize all templates
        self.templates = {k: self.normalize_template(v) for k, v in self.templates.items()}
        self.char_templates = {k: self.normalize_template(v) for k, v in self.char_templates.items()}

    def normalize_template(self, template):
        """Normalize a template to the standard width and height."""
        # Ensure each row has the standard width by centering it
        padded_rows = [row.center(self.standard_width) for row in template]

        # Add empty rows to reach the standard height
        while len(padded_rows) < self.standard_height:
            padded_rows.append(" " * self.standard_width)

        # Truncate rows if they exceed the standard height
        return padded_rows[:self.standard_height]

    def generate_program(self, ast):
        """Generates the Python program based on the AST."""
        program_lines = [
            "import warnings",
            "from warnings import filterwarnings",
            "filterwarnings(\"ignore\", category=SyntaxWarning)",
            "",
            "def draw_ascii_art(template):",
            "    for line in template:",
            "        print(line)",
            "",
            "def combine_top_bottom(top, bottom):",
            "    max_width = max(len(top[0]), len(bottom[0]))",
            "    top = [line.ljust(max_width) for line in top]",
            "    bottom = [line.ljust(max_width) for line in bottom]",
            "    return top + bottom",
            "",
            "def repeat_horizontal(template, times):",
            "    try:",
            "        times = int(times)",
            "        return [line * times for line in template]",
            "    except ValueError:",
            "        return ['[INVALID REPEAT COUNT]']",
            "",
            "def combine_horizontal(left, right):",
            "    max_height = max(len(left), len(right))",
            "    left = left + [''] * (max_height - len(left))  # Pad shorter template",
            "    right = right + [''] * (max_height - len(right))  # Pad shorter template",
            "    return [l + ' ' + r for l, r in zip(left, right)]",
            "",
            "def grid(x, y, *elements):",
            "    if len(elements) != x * y:",
            "        raise ValueError(\"Grid dimensions do not match the number of elements.\")",
            "",
            "    max_lines = max(len(element) for element in elements)",
            "    for i in range(y):",
            "        row_elements = elements[i * x:(i + 1) * x]",
            "        for line_idx in range(max_lines):",
            "            for element in row_elements:",
            "                if line_idx < len(element):",
            "                    print(element[line_idx], end='  ')",
            "                else:",
            "                    print(' ' * len(element[0]), end='  ')",
            "            print()",
            "",
            "# ASCII templates",
            "templates = {"
        ]

        # Add templates to the code
        for name, template in self.templates.items():
            template_lines = ",\n            ".join(f'"{line}"' for line in template)
            program_lines.append(f'    "{name}": [\n            {template_lines}\n        ],')
        program_lines.append("    }")

        # Generate statements from the AST
        for stmt in ast.children:
            stmt_code = self.generate_statement(stmt)
            if stmt_code:
                program_lines.append(stmt_code)

        return "\n".join(program_lines)

    def generate_statement(self, stmt_node):
        """Generates Python code for a single statement."""
        if stmt_node.type == 'DrawStatement':
            return self.generate_draw(stmt_node)
        elif stmt_node.type == 'WriteStatement':
            return self.generate_write(stmt_node)
        elif stmt_node.type == 'GridStatement':
            self.is_grid = 1
            return self.generate_grid(stmt_node)
        return None

    def generate_draw(self, draw_node):
        """Generates Python code to draw ASCII art."""
        expr = self.generate_expression(draw_node.children[0])  
        if self.is_grid:
            return f"{expr}"
        return f"draw_ascii_art({expr})"

    def generate_write(self, write_node):
        """Generates Python code to write ASCII text."""
        text = write_node.children[0].value.upper()
        return self.generate_text_output(text)
        
    def generate_grid(self, grid_node):
        """Generates Python code for a grid statement."""
        x = grid_node.children[0].value
        y = grid_node.children[1].value

        # Ensure GridContent is processed properly
        elements = []
        for child in grid_node.children[2].children:
            elem_code = self.generate_statement(child)
            elements.append(elem_code)
        self.is_grid = 0
        return f"grid({x}, {y}, {', '.join(elements)})"

    def generate_text_output(self, text):
        """Generates Python code to output ASCII text."""
        output = [""] * self.standard_height
        for char in text:
            # Get the ASCII art for the character, or use blank rows if undefined
            char_template = self.char_templates.get(char, [" " * self.standard_width] * self.standard_height)
            for i in range(self.standard_height):
                output[i] += char_template[i] + " "
        return "\n".join(f"print('{line}')" for line in output)

    def generate_expression(self, expr_node):
        """Generates Python code for an expression."""
        if expr_node.type == 'Identifier':
            return f'templates.get("{expr_node.value}", ["[Unknown Image]"])'
        elif expr_node.type == 'Expression':
            op = expr_node.value
            left = self.generate_expression(expr_node.children[0])
            if op == '*':
                # Set right to the number following Number( in the AST
                right = expr_node.children[1].value  # Extract the number directly
                return f'repeat_horizontal({left}, {right})'
            elif op == '/':
                right = self.generate_expression(expr_node.children[1])
                return f'combine_top_bottom({left}, {right})'
            elif op == '+':
                right = self.generate_expression(expr_node.children[1])
                return f'combine_horizontal({left}, {right})'
            else:
                return '"[INVALID OPERATOR]"'
        return '"[INVALID EXPRESSION]"'
