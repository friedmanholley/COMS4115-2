class CodeGenerator:
    def __init__(self):
        # Templates for images (dog, cat, etc.) generated using chatGPT.
        self.templates = {
            "dog": [
                "^..^      /",
                "/_/\_____/",
                "   /\   /\ "
            ],
            "cat": [
                " /\_/\ ",
                "( o.o )",
                " > ^ < "
            ],
            "bird": [
                "  /\_/\  ",
                "(  • •  )",
                "  =_Y_=  ",
                "   `-`   "
            ],
            "sun": [
                "   \\ | /   ",
                " --   *   -- ",
                "   / | \\   "
            ],
            "tree": [
                "   *   ",
                "  ***  ",
                " ***** ",
                "   |   ",
                "   |   "
            ],
            "house": [
                "   /\\   ",
                "  /  \\  ",
                " /____\\ ",
                "|      |",
                "|______|"
            ]
        }

        # ASCII font for WRITE statements, A-Z, 0-9. 
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
                ' ┃┃',
                ' ┃┃',
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
                '┃╰╯╯',
                '┃╭╮┃',
                '┃┃┃╰╮',
                '╰╯╰━╯'
            ],
            'L': [
                '╭╮',
                '┃┃',
                '┃┃',
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
                '┃┃',
                '╰╯'
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
                '  ┃┃',
                '  ┃┃',
                '  ╰╯'
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
                ' ┃╰╯┃',
                ' ╰╮╭╯',
                '  ╰╯'
            ],
            'W': [
                '╭╮╭╮╭╮',
                '┃┃┃┃┃┃',
                '┃┃┃┃┃┃',
                '┃╰╯╰╯┃',
                '╰╮╭╮╭╯',
                ' ╰╯╰╯'
            ],
            'X': [
                '╭━╮╭━╮',
                '╰╮╰╯╭╯',
                ' ╰╮╭╯',
                ' ╭╯╰╮',
                '╭╯╭╮╰╮',
                '╰━╯╰━╯'
            ],
            'Y': [
                '╭╮  ╭╮',
                '┃╰╮╭╯┃',
                '╰╮╰╯╭╯',
                ' ╰╮╭╯',
                '  ┃┃',
                '  ╰╯'
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
            ]
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
            ]
        }

    def generate_program(self, program_node):
        results = []
        for stmt in program_node.children:
            result = self.generate_statement(stmt)
            if isinstance(result, list):
                results.extend(result)
            else:
                results.append(str(result))
        return "\n".join(results)

    def generate_statement(self, stmt_node):
        if stmt_node.type == 'DrawStatement':
            return self.generate_draw(stmt_node)
        elif stmt_node.type == 'WriteStatement':
            return self.generate_write(stmt_node)
        elif stmt_node.type == 'GridStatement':
            return self.generate_grid(stmt_node)
        # Handle other statements as needed

    def generate_draw(self, draw_node):
        # Assume draw_node.children[0] is the expression node
        image_data = self.generate_expression(draw_node.children[0])
        return image_data

    def generate_write(self, write_node):
        # write_node.children[0] contains an expression or identifier representing text
        # Assume this expression is just an identifier node with the text to write
        text_node = write_node.children[0]
        if text_node.type == 'Identifier':
            return self.generate_text(text_node.value)
        else:
            return ["[WRITE ERROR: Invalid text]"]

    def generate_text(self, text):
        # For each character in the text, get its ASCII template and then
        # combine them horizontally line-by-line.
        lines = []
        # Convert text to uppercase or handle both cases
        text = text.upper()
        char_images = [self.char_templates.get(ch, ["[?]"]) for ch in text]

        # First, ensure all characters have the same number of lines
        max_lines = max(len(img) for img in char_images if isinstance(img, list))
        # Pad images with blank lines if needed
        for i, img in enumerate(char_images):
            if isinstance(img, list):
                char_images[i] = img + [""] * (max_lines - len(img))
            else:
                # If the character isn't found, represent it as [?]
                char_images[i] = ["[?]"] + [""] * (max_lines - 1)

        # Now combine horizontally
        for line_idx in range(max_lines):
            line_parts = [img[line_idx] for img in char_images]
            lines.append(" ".join(line_parts))
        return lines

    def generate_grid(self, grid_node):
        rows, cols = grid_node.value
        grid_content = grid_node.children[0].children
        output = []
        index = 0
        for r in range(rows):
            row_images = []
            for c in range(cols):
                if index < len(grid_content):
                    img = self.generate_expression(grid_content[index])
                    row_images.append(img)
                    index += 1
            # horizontally combine images for one row
            if row_images:
                combined = row_images[0]
                for img in row_images[1:]:
                    combined = self.combine_side_by_side(combined, img)
                output.extend(combined)
        return output

    def generate_expression(self, expr_node):
        if expr_node.type == 'Identifier':
            return self.templates.get(expr_node.value, ["[Unknown Image]"])
        elif expr_node.type == 'Expression':
            op = expr_node.value
            left = expr_node.children[0]
            right = expr_node.children[1]
            left_img = self.generate_expression(left)
            right_img = self.generate_expression(right)
            if op == '+':
                return self.combine_side_by_side(left_img, right_img)
            elif op == '/':
                return self.combine_top_bottom(left_img, right_img)
            elif op == '*':
                # Implement repetition if needed
                return left_img
        else:
            return ["[Invalid Expression]"]

    def combine_side_by_side(self, left_img, right_img):
        max_height = max(len(left_img), len(right_img))
        left_img = left_img + [""] * (max_height - len(left_img))
        right_img = right_img + [""] * (max_height - len(right_img))
        combined = [l + r for l, r in zip(left_img, right_img)]
        return combined

    def combine_top_bottom(self, top_img, bottom_img):
        return top_img + bottom_img
