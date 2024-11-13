#!/bin/bash

# Ensure that the script stops execution if any command fails
set -e

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

# Step 4: Run the parser
echo "Running the parser..."
python test.py  # Assuming 'test.py' is the main parser file

# Step 5: Deactivate the virtual environment
echo "Deactivating the virtual environment..."
deactivate
