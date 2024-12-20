### **Authors**
- Gabrielle Holley: `gf2501`
- William Culver: `wrc2120`

### **Video**
[Link to Video in Google Drive](https://drive.google.com/file/d/1AAiS8XdS8ODfVJHQK35T-K_JEjPol4Bd/view?usp=share_link)
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
Statement       -> DrawStatement | WriteStatement | GridStatement
DrawStatement   -> 'draw' '(' Expression ')'
WriteStatement  -> 'write' '(' Expression ')'
GridStatement   -> 'grid' '(' Number ',' Number ',' GridContent ')'
GridContent     -> (Expression (',' Expression)*) | (GridStatement (',' GridStatement)*)
Expression      -> Image | Expression '+' Image | Expression '/' Image | Number '*' Image
Image           -> 'draw' '(' Identifier ')'
                | 'write' '(' Identifier ')'
Identifier      -> 'dog' | 'cat' | 'tree' | 'sun' | 'house' | 'bird'
Number          -> [0-9]+
```

---
### **Explanation of Code**:

`alltogether.py` imports `codegen.py`, `lexer.py` and `parser.py` which contain the three steps we have developed. 
`codegen.sh` accepts a .txt or .py file as input to the executable and will out put ASCII.
`sample3.txt` contains 7 sample lines of code. The last line contains a syntax error which will prevent the first 6 from processing, so it is commented out. 

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
- **Image**: An image is a predefined ASCII image generated by `draw` or `write`
- **Identifier**: Identifiers are predefined names such as `dog`, `cat`, `sun`, etc.
- **Number**: Represents numerical values, used for repeat operations (e.g., `*` operator).

---

# Sample Input Programs (included in `sample3.txt`)

### Sample Input 1
```plaintext
grid(3,2,draw(cat), draw(cat), draw(dog), draw(cat), draw(dog), draw(house));

     /\_/\            /\_/\         ^..^      /    
    ( o.o )          ( o.o )         /_/\_____/    
     > ^ <            > ^ <            /\   /\     
                                                   
                                                   
                                                   
     /\_/\         ^..^      /           /\        
    ( o.o )         /_/\_____/          /  \       
     > ^ <            /\   /\          /____\      
                                      |      |     
                                      |______|    

```
### Sample Input 2
```plaintext
draw(cat/tree);

     /\_/\     
    ( o.o )    
     > ^ <            
               
       *       
      ***      
     *****     
       |       
       |       
```

### Sample Input 3
```plaintext
write(hello);

     ╭╮ ╭╮           ╭━━━╮           ╭╮              ╭╮              ╭━━━╮      
     ┃┃ ┃┃           ┃╭━━╯           ┃┃              ┃┃              ┃╭━╮┃      
     ┃╰━╯┃           ┃╰━━╮           ┃┃              ┃┃              ┃┃ ┃┃      
     ┃╭━╮┃           ┃╭━━╯           ┃┃ ╭╮           ┃┃ ╭╮           ┃┃ ┃┃      
     ┃┃ ┃┃           ┃╰━━╮           ┃╰━╯┃           ┃╰━╯┃           ┃╰━╯┃      
     ╰╯ ╰╯           ╰━━━╯           ╰━━━╯           ╰━━━╯           ╰━━━╯  

```

### Sample Input 4
```plaintext
write(world);

     ╭╮╭╮╭╮          ╭━━━╮           ╭━━━╮           ╭╮              ╭━━━╮      
     ┃┃┃┃┃┃          ┃╭━╮┃           ┃╭━╮┃           ┃┃              ╰╮╭╮┃      
     ┃┃┃┃┃┃          ┃┃ ┃┃           ┃╰━╯┃           ┃┃               ┃┃┃┃      
     ┃╰╯╰╯┃          ┃┃ ┃┃           ┃╭╮╭╯           ┃┃ ╭╮            ┃┃┃┃      
     ╰╮╭╮╭╯          ┃╰━╯┃           ┃┃┃╰╮           ┃╰━╯┃           ╭╯╰╯┃      
      ╰╯╰╯           ╰━━━╯           ╰╯╰━╯           ╰━━━╯           ╰━━━╯  
```

### Sample Input 5
```plaintext
draw(house + bird);

       /\            /\_/\     
      /  \         (  • •  )   
     /____\          =_Y_=     
    |      |          `-`      
    |______|                   
                               
```

### Error Input
```plaintext
draw(horse);

We have set this up unknown identifiers passed to draw to still generate code, as shown below.

[Unknown Image]
```
