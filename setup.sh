#!/bin/bash

# Step 1: Install Robot Framework via Brew
brew install robot-framework

# Step 2: Add Python 3.11 binary directory to PATH
echo 'export PATH=/opt/homebrew/Cellar/python@3.11/3.11.6_1/bin/:$PATH' >> ~/.zshrc
source ~/.zshrc

# Step 3: Start a new shell to apply changes
echo "Please open a new shell to apply the changes made to your PATH."

# Step 4: Install Python dependencies
pip3 install -r requirements.txt

# Step 5: Initialize Robot Framework Browser library
rfbrowser init

echo "Setup completed. You can now start working on your Python project."