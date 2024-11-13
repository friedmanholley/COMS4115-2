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
                return self.parse_draw_statement()
            elif keyword == 'grid':
                print("Parsing grid statement...")  # Debugging print statement
                return self.parse_grid_statement()  # This is now correctly defined
            elif keyword == 'write':  # Handle 'write' keyword
                print("Parsing write statement...")  # Debugging print statement
                return self.parse_write_statement()  # Parse the write statement
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

    def parse_write_statement(self):
        print("Inside parse_write_statement()")  # Debugging print statement
        self.eat('Keyword')  # Eat 'write'
        self.eat('SpecialSymbol')  # Eat '('
    
        expression = self.parse_expression()  # Parse the first expression inside the write statement
        
        # Check if there are more tokens (like more identifiers or operators) to handle
        while self.current_token() and self.current_token()[0] == 'Operator' and self.current_token()[1] == '+':
            self.eat('Operator')  # Eat the '+' operator
            right_expression = self.parse_expression()  # Parse the right-hand side expression
            operator_node = ASTNode('Expression', value='+')  # Create a new node for the concatenation operator
            operator_node.add_child(expression)  # Add the left operand
            operator_node.add_child(right_expression)  # Add the right operand
            expression = operator_node  # Update the expression to the new operator node
        
        self.eat('SpecialSymbol')  # Eat ')'
    
        # Create the AST node for the WriteStatement
        node = ASTNode('WriteStatement')
        node.add_child(expression)  # Add the parsed expression as a child of the WriteStatement node
        
        print(f"WriteStatement AST node: {node}")  # Debugging print statement
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
        """Parse grid content which can be a combination of expressions."""
        content_node = ASTNode('GridContent')
        while self.position < len(self.tokens):
            current = self.current_token()
            
            if current and current[0] == 'Keyword':  # Handle 'draw' or 'write' separately
                if current[1] == 'draw':
                    content_node.add_child(self.parse_draw_statement())
                elif current[1] == 'write':
                    content_node.add_child(self.parse_write_statement())
                else:
                    raise SyntaxError(f"Unexpected keyword {current[1]}")
                
                # Check for comma separation and eat if found
                if self.current_token() and self.current_token()[0] == 'SpecialSymbol' and self.current_token()[1] == ',':
                    self.eat('SpecialSymbol')  # Eat ','
                else:
                    break  # Stop if no more commas or invalid tokens
            elif current and current[0] == 'SpecialSymbol' and current[1] == ')':
                break  # Stop if we've encountered the closing parenthesis for the grid
            else:
                break  # Break if any unexpected token is found
    
        return content_node
    
    
    def parse_grid_statement(self):
        """Parse a 'grid' statement."""
        self.eat('Keyword')  # eat 'grid'
        self.eat('SpecialSymbol')  # eat '('
        rows = self.parse_number()  # Parse number of rows
        self.eat('SpecialSymbol')  # eat ','
        cols = self.parse_number()  # Parse number of columns
        self.eat('SpecialSymbol')  # eat ','
        grid_content = self.parse_grid_content()  # Parse the content inside the grid
        self.eat('SpecialSymbol')  # eat ')'
            
        node = ASTNode('GridStatement', value=(rows, cols))
        node.add_child(grid_content)  # Add the parsed grid content as a child node
        return node
