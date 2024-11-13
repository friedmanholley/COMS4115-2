class ASTNode:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        if self.children:
            return f"{self.type}({self.value}): [{', '.join([repr(child) for child in self.children])}]"
        else:
            return f"{self.type}({self.value})"


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
        if current and current[0] == 'Keyword':
            keyword = current[1]
            if keyword == 'draw':
                print("Parsing draw statement...")  # Debugging print statement
                return self.parse_draw_statement()  # Ensure this method exists
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
        
        # Create the AST node for the DrawStatement
        node = ASTNode('DrawStatement')
        node.add_child(expression)  # Add the parsed expression as a child of the DrawStatement node
        
        # Debugging: Check the children of DrawStatement after adding expression
        print(f"DrawStatement children: {node.children}")  # Debugging: Show the children of DrawStatement
        
        print(f"Draw statement AST node: {node}")  # Debugging print statement
        return node



    def parse_expression(self):
        print("Inside parse_expression()")  # Debugging print statement
        left = self.parse_image()  # Parse the first image (e.g., 'sun')
        while self.current_token() and self.current_token()[0] == 'Operator':
            operator = self.current_token()[1]  # Get the operator ('+')
            self.eat('Operator')  # Eat the operator token
            right = self.parse_image()  # Parse the right-hand side image (e.g., 'dog')
            
            operator_node = ASTNode('Expression', value=operator)  # Create a new expression node for the operator
            operator_node.add_child(left)  # Add the left operand (sun)
            operator_node.add_child(right)  # Add the right operand (dog)
            
            left = operator_node  # Update left to the new operator node (for the next operator, if any)
        
        print(f"Expression parsed as: {left}")  # Debugging print statement
        return left

    def parse_image(self):
        current = self.current_token()
        if current[0] == 'Identifier':
            identifier = self.current_token()[1]
            self.eat('Identifier')  # Eat the identifier (sun, dog)
            return ASTNode('Identifier', value=identifier)
        else:
            raise SyntaxError(f"Unexpected token in image: {current}")

    def parse_number(self):
        number = self.current_token()[1]
        self.eat('Number')
        return number

    def parse_grid_content(self):
        content_node = ASTNode('GridContent')
        while self.position < len(self.tokens):
            current = self.current_token()
            if current and current[0] in ['Keyword', 'Identifier']:
                content_node.add_child(self.parse_expression())
                if self.current_token() and self.current_token()[0] == 'SpecialSymbol' and self.current_token()[1] == ',':
                    self.eat('SpecialSymbol')  # eat ','
                else:
                    break  # Stop if no more commas or invalid tokens
            elif current and current[0] == 'SpecialSymbol' and current[1] == ')':
                break  # Stop if we've encountered the closing parenthesis for the grid
            else:
                break  # Break if any unexpected token is found
        return content_node

    def parse_grid_content(self):
        """Parse grid content which can be a combination of expressions."""
        content_node = ASTNode('GridContent')
        while self.position < len(self.tokens):
            current = self.current_token()
            if current and current[0] in ['Keyword', 'Identifier']:
                content_node.add_child(self.parse_expression())
                if self.current_token() and self.current_token()[0] == 'SpecialSymbol' and self.current_token()[1] == ',':
                    self.eat('SpecialSymbol')  # eat ','
                else:
                    break  # Stop if no more commas or invalid tokens
            elif current and current[0] == 'SpecialSymbol' and current[1] == ')':
                break  # Stop if we've encountered the closing parenthesis for the grid
            else:
                break  # Break if any unexpected token is found
        return content_node
