class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def current_token(self):
        return self.tokens[self.position] if self.position < len(self.tokens) else None

    def eat(self, token_type):
        """Consumes the current token if it matches the expected type."""
        if self.current_token() and self.current_token()[0] == token_type:
            self.position += 1
        else:
            raise SyntaxError(f"Expected {token_type}, found {self.current_token()}")

    def parse_program(self):
        root = ASTNode("Program")
        while self.position < len(self.tokens):
            statement = self.parse_statement()
            if statement:
                root.add_child(statement)  # Ensure statement is added to root
        return root

    def parse_statement(self):
        current = self.current_token()
        if current is None:
            return None  # Handle the end of the program gracefully

        if current[0] == 'Keyword':
            keyword = current[1]
            if keyword == 'draw':
                print("Parsing draw statement...")  # Debugging print statement
                return self.parse_draw_statement()
            elif keyword == 'grid':
                print("Parsing grid statement...")  # Debugging print statement
                return self.parse_grid_statement()
            else:
                raise SyntaxError(f"Unknown statement {keyword}")
        elif current[0] == 'SpecialSymbol' and current[1] == ';':
            # Skip over semicolons as statement terminators
            self.eat('SpecialSymbol')  # eat ';'
            return None  # No statement to parse

        else:
            raise SyntaxError(f"Unexpected token {current}")

def parse_draw_statement(self):
    print("Inside parse_draw_statement()")  # Debugging print statement
    self.eat('Keyword')  # eat 'draw'
    self.eat('SpecialSymbol')  # eat '('
    expression = self.parse_expression()  # Parse the expression
    self.eat('SpecialSymbol')  # eat ')'
    
    node = ASTNode('DrawStatement')
    node.add_child(expression)  # Add the parsed expression as a child of the DrawStatement node
    
    print(f"Draw statement AST node: {node}")  # Debugging print statement
    return node


    def parse_expression(self):
        left = self.parse_image()
        while self.current_token() and self.current_token()[0] == 'Operator':
            operator = self.current_token()[1]
            self.eat('Operator')
            right = self.parse_image()
            operator_node = ASTNode('Expression', value=operator)
            operator_node.add_child(left)
            operator_node.add_child(right)
            left = operator_node  # Update left to the new operator node
        return left

    def parse_image(self):
        current = self.current_token()
        if current[0] == 'Identifier':
            identifier = self.current_token()[1]
            self.eat('Identifier')
            return ASTNode('Identifier', value=identifier)
        else:
            raise SyntaxError(f"Unexpected token in image: {current}")

class ASTNode:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"ASTNode({self.type}, {self.value})"
