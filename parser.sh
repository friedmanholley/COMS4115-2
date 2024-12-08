#!/bin/bash

# Ensure that the script stops execution if any command fails
set -e

# Check if a .py or .txt file was passed as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <file_to_parse.py or file_to_parse.txt>"
    exit 1
fi

# Get the file passed as an argument
INPUT_FILE=$1

# Check the file extension
EXT="${INPUT_FILE##*.}"

# Step 1: Set up a virtual environment (optional but recommended)
echo "Setting up a virtual environment..."
python3 -m venv venv

# Step 2: Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Step 3: Install required dependencies
echo "Installing dependencies..."
pip install --upgrade pip  # Upgrade pip to the latest version
pip install -r requirements.txt  # Install dependencies from requirements.txt

# Step 4: Run the parser with the provided file
echo "Running the parser on $INPUT_FILE..."

if [ "$EXT" == "py" ] || [ "$EXT" == "txt" ]; then
    # If it's a .py or .txt file, pass the file to the parser
    python parse.py "$INPUT_FILE" > ast.json
else
    echo "Unsupported file type. Please provide a .py or .txt file."
    exit 1
fi

# Step 5: Run Code Generation
echo "Running code generation on ast.json..."
python codegen.py ast.json

# Step 6: Deactivate the virtual environment
echo "Deactivating the virtual environment..."
deactivate
