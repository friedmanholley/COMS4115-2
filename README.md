### **Authors**
- Gabrielle Holley: `gf2501`
- William Culver: `wrc2120`

### **Context-Free Grammar (CFG)**

#### **Non-Terminals:**
- `Program`: The entry point of the program, consisting of multiple statements.
- `Statement`: Represents a single line of code in the program.
- `Expression`: A combination of images, words, and operations.
- `Image`: Represents either a pre-defined image (`draw`) or text written in ASCII (`write`).
- `Grid`: Represents a grid layout for images and words.
- `Identifier`: Represents predefined image names or identifiers.
- `Number`: Represents numbers used in repeat operations.

#### **Terminals:**
- **Keywords**: `draw`, `write`, `grid`
- **Operators**: `+`, `/`, `*`
- **Special Symbols**: `(`, `)`, `,`, `;`
- **Identifiers**: Words like `dog`, `cat`, `tree`, `sun`, etc.
- **Numbers**: Digits like `1`, `2`, `3`, etc.

#### **Production Rules:**

```
Program         -> Statement*
Statement       -> DrawStatement | WriteStatement | GridStatement | AssignmentStatement
DrawStatement   -> 'draw' '(' Expression ')'
WriteStatement  -> 'write' '(' Expression ')'
GridStatement   -> 'grid' '(' Number ',' Number ',' GridContent ')'
GridContent     -> (Expression (',' Expression)*) | (GridStatement (',' GridStatement)*)
Expression      -> Image | Expression '+' Image | Expression '/' Image | Number '*' Image
Image           -> 'draw' '(' Identifier ')'
                | 'write' '(' Identifier ')'
                | Identifier
Identifier      -> 'dog' | 'cat' | 'tree' | 'sun' | 'house' | 'bird'
Number          -> [0-9]+
```

---

### **Explanation of the Grammar**:

- **Program**: A program consists of one or more statements (`Statement*`).
- **Statement**: A statement can be a `DrawStatement`, `WriteStatement`, `GridStatement`, or an `AssignmentStatement`. We can later expand this to include more functionality if needed.
- **DrawStatement**: A `draw` statement takes an expression inside parentheses, which can be an image.
- **WriteStatement**: A `write` statement is similar to `draw`, except it creates text-based ASCII art.
- **GridStatement**: A `grid` statement consists of a grid size (rows, columns) followed by `GridContent`, which can be a combination of images or other grid statements. This allows for nested grid layouts.
- **Expression**: An expression can be a single image, or a combination of images using the operators `+`, `/`, or `*`.
  - `+` combines images linearly (side by side).
  - `/` combines images vertically (stacked).
  - `*` duplicates an image a specified number of times.
- **Image**: An image is either a predefined ASCII image generated by `draw` or `write`, or a reference to an identifier (e.g., `dog`, `cat`).
- **Identifier**: Identifiers are predefined image names such as `dog`, `cat`, `sun`, etc.
- **Number**: Represents numerical values, used for repeat operations (e.g., `*` operator).

---

# Sample Input Programs (included in `sample.txt`)

### Sample Input 1
```plaintext
draw(sun + dog);

DRAW_STATEMENT
├── EXPRESSION (+)
│   ├── IDENTIFIER (sun)
│   └── IDENTIFIER (dog)

This would generate an image with side-by-side pictures of sun (left) and dog (right). 
```
#### Sample Input 2
```plaintext
write(cat) * 3;

WRITE_STATEMENT
├── EXPRESSION (*)
│   ├── IDENTIFIER (cat)
│   ├── *
│   └── NUMBER (3)


This would generate 3 word illustrations of the word cat.
```

#### Sample Input 3
```plaintext
grid(2, 2, draw(cat), draw(dog), write(cat), write(dog));

GRID_STATEMENT
├── GRID_CONTENT
│   ├── DRAW_STATEMENT
│   │   ├── IDENTIFIER (cat)
│   └── DRAW_STATEMENT
│       ├── IDENTIFIER (dog)

This would generate a 2x2 grid with images of cat and dog on the first row, and word illustration of cat and dog on the second.
```

#### Sample Input 4
```plaintext
write(cat) * 3 + draw(dog);

WRITE_STATEMENT
├── EXPRESSION (+)
│   ├── EXPRESSION (*)
│   │   ├── IDENTIFIER (cat)
│   │   ├── *
│   │   └── NUMBER (3)
│   └── DRAW_STATEMENT
│       ├── IDENTIFIER (dog)


This would generate 3 word illustration of the text cat, followed by one image of a dog.
```

### Sample Input 5
```plaintext
write(sun) / draw(dog);

WRITE_STATEMENT
├── EXPRESSION (/)
│   ├── IDENTIFIER (sun)
│   ├── /
│   └── DRAW_STATEMENT
│       ├── IDENTIFIER (dog)


This would generate word illustration of sun over top of an image of a dog.
```
