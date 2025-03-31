# Prefix Notation Calculator

## Overview
The **Prefix Notation Calculator** is a simple application that evaluates arithmetic expressions in **prefix notation** (also known as Polish notation). This calculator allows users to input expressions with operators placed before their operands, following the rules of prefix notation. The calculator supports basic arithmetic operations such as addition (+) and multiplication (*), and it displays results in both numeric form and infix notation.

## Features
- **Prefix Notation Parsing**: The application supports prefix notation where operators come before operands.
- **Arithmetic Operations**: The calculator handles basic arithmetic operations like addition and multiplication.
- **Operator Precedence**: The calculator evaluates multiplication before addition, respecting operator precedence.
- **Error Handling**: The application provides error messages for incomplete or invalid expressions.
- **Infix Notation**: The calculator also converts the evaluated prefix expression to infix notation and displays it alongside the numeric result.

## Technologies Used
- **Python**: The application is built using Python, leveraging libraries like **Sly** for parsing and **PyQt6** for the graphical user interface (GUI).
- **Sly**: A Python library for writing lexers and parsers. It is used to tokenize the input and parse the prefix notation expressions.
- **PyQt6**: A set of Python bindings for Qt libraries to build the user interface.

## Installation

### 1. Clone the Repository
First, clone the repository to your local machine using the following command:

``git clone https://github.com/HuyNg124724/PLCproject.git``

### 2. Install Dependencies
Make sure you have Python installed on your system. Then, install the required dependencies using `pip`:

``pip install -r requirements.txt``

This will install all the necessary libraries, including **PyQt6** and **Sly**.

## Usage

### 1. Run the Application
To run the Prefix Notation Calculator, simply run the following command:

``python main.py``

### 2. Input Format
- Enter the prefix notation expression in the input field (e.g., `+ 1 * 2 3`).
- Press the `=` button to evaluate the expression.
- The calculator will display the result in numeric format on the LCD screen and the corresponding infix notation on the status bar.

### Example:
- **Input**: `+ 1 * 2 3`
- **Output (Numeric)**: `7`
- **Output (Infix)**: `1 + (2 * 3)`

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your improvements or bug fixes. Any contributions are appreciated!

## License
This project is open-source and available under the **MIT License**.

## Report
https://drive.google.com/file/d/1g8SGCdj2zqoTm5eexIYSQ8nbB9uncATO/view?usp=sharing 
