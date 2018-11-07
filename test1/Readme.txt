@Author Inoussa Mouiche, 10/25/2018

- Use in support of the python script calc.py
- To run calc.py in command line:
- Make sure to have the interpreter shebang python line 
#!/usr/bin/env python
- and mark the python scrypt as executable by typing 
chmod +x calc.py 
using macOS or Unix/Linux terminal after you navigate to your python folder


Test cases with maximum depth =2
1- 
Input: ./calc.py "123"
Output: 123
2-
Input: ./calc.py "(add 2 add (2 3))"
Output: (7, 'is the final result')
3- 
Input: ./calc.py "(add 2 2 add (2 3 4))"
Output: (13, 'is the final result')
4-
Input: ./calc.py "(multiply 2 multiply (2 3))"
Output: (12, 'is the final result')
5- 
Input: ./calc.py "(add 2 multiply (2 3))"
Output: (8, 'is the final result')
6-
Input: ./calc.py "(add 1 2 3 4 (multiply 2 3 5))"
Output: (40, 'is the final result')
7-
Input: ./calc.py "(add 2 3 4 2 3 5 6))"
Output: (25, 'is the final result')
8-
Input: ./calc.py "(multiply 2 3 4 2 3 5 6))"
Output: (4320, 'is the final result')
9-
Input: ./calc.py "(add 2 6 2 1 multiply (2 5 9 4 5))"
Output: (1811, 'is the final result')

However, consider using a space between a operator and a number. We still have to improve this code to make it shorter and more efficient 