class CodeGenerator:
    def __init__(self):
        # Possibly load predefined ASCII templates for known identifiers
        self.templates = {
            "sun": ["  \\ | /  ",
                     " -- * -- ",
                     "  / | \\  "],
            "dog": ["^..^      /",
                    "/_/\_____/",
                    "   /\   /\ "]
            # etc.
        }

    def generate_program(self, program_node):
        # Program node might have a list of statements
        results = []
        for stmt in program_node.children:
            result = self.generate_statement(stmt)
            results.append(result)
        # Combine all top-level statements output if needed
        return "\n".join("".join(line) for line in results)

    def generate_statement(self, stmt_node):
        if stmt_node.type == 'DrawStatement':
            return self.generate_draw(stmt_node)
        elif stmt_node.type == 'WriteStatement':
            return self.generate_write(stmt_node)
        elif stmt_node.type == 'GridStatement':
            return self.generate_grid(stmt_node)
        # ... handle other statements

    def generate_draw(self, draw_node):
        # draw_node.children[0] would be the expression (Identifier or Expression)
        image_data = self.generate_expression(draw_node.children[0])
        return image_data

    def generate_expression(self, expr_node):
        # If it's a simple Identifier node, return the corresponding ASCII template
        if expr_node.type == 'Identifier':
            return self.templates.get(expr_node.value, ["[Unknown]"])
        elif expr_node.type == 'Expression':
            # Handle operators: +, /, *
            op = expr_node.value
            left = expr_node.children[0]
            right = expr_node.children[1]
            left_img = self.generate_expression(left)
            right_img = self.generate_expression(right)
            if op == '+':
                return self.combine_side_by_side(left_img, right_img)
            elif op == '/':
                return self.combine_top_bottom(left_img, right_img)
            # ... handle '*'
        # ... and so on

