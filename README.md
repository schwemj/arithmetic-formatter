# arithmetic_formatter

This is a simple arithmetic formatter written in Python3, which displays arithmetic problems in a vertical format to improve readability. 

To use it, call and print the arithmetic_formatter() function with a list of mathematical problems in string format as the first argument. 
If the inclusion of calculated results is desired, set display_answers = True.

Boundaries:
- mathematical problems must be given as a list of strings (list can be of length 1)
- valid operations are limited to addition and subtraction of two numbers
- maximum number of input problems at once is 5
- numbers cannot be fractions and have to be less than 5 digits in length
- elements of a problem must be separated by a space

Examples for valid strings:

'42 + 2'

'3 - 12'

'-10 + 6513'

Examples for invalid strings:

'1+2' (elements not separated by space)

'15743 - 23' (first number exceeds 4 digit limit)

'32 - 645 + 7321' (more than two operands)

---
REQUIREMENTS:
- Python3
