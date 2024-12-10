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

# Step 4: Run Code Generation
echo "Running code generation on $INPUT_FILE..."
python3 alltogether.py "$INPUT_FILE"

# Step 5: Execute the intermediate code
echo "Executing intermediate_code.py..."
python3 intermediate_code.py

# Step 6: Deactivate the virtual environment
echo "Deactivating the virtual environment..."
deactivate
