import re

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.tokens = []

    def tokenize(self):
        # Define token patterns (for keywords, operators, identifiers, numbers, and symbols)
        token_specification = [
            ('Keyword', r'\b(draw|write|grid)\b'),  # Keywords
            ('Operator', r'[+\-*/]'),              # Operators
            ('Identifier', r'[A-Za-z_][A-Za-z0-9_]*'),  # Identifiers (variable names)
            ('Number', r'\d+'),                    # Numbers
            ('SpecialSymbol', r'[(),;]'),          # Special Symbols (parentheses, commas, semicolons)
            ('Whitespace', r'\s+'),                 # Skip over whitespace
            ('Comment', r'#.*'),                   # Skip over comments
        ]
        
        # Combine the regex patterns into a single regular expression
        token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)

        # Scan through the input and tokenize it
        while self.position < len(self.source_code):
            match = re.match(token_regex, self.source_code[self.position:])
            if match:
                # Process only the matched group
                for token_type in match.groupdict():
                    if match.group(token_type):  # Check if this group has a match
                        if token_type not in ['Whitespace', 'Comment']:  # Skip Whitespace and Comment
                            self.tokens.append((token_type, match.group(token_type)))
                        break  # Break after finding the first match
                # Move the position forward by the length of the matched string
                self.position += len(match.group(0))
            else:
                # If no match is found, raise an error (unexpected character)
                raise SyntaxError(f"Unexpected character: {self.source_code[self.position]}")

        return self.tokens

