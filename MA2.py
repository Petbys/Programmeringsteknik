"""
Solutions to module 2 - A calculator
Student: Petter Byström
Mail: petter.bystrom.8041@student.uu.se
Reviewed by:
Reviewed date:
"""


from tokenize import Pointfloat, TokenError
from MA2tokenizer import TokenizeWrapper
import math


# Globala variabler
vars = {'ans':0}
vars['PI'] = 3.14159365
vars['E'] = 2.718
function_l = ['sin','cos','exp', 'log', 'fib', 'fac']


# hjälpfunktioner

def fib(n):
    a,b = 0,1
    for _ in range(int(n)):
        c = a+b
        a = b
        b = c
    return a

def mean(arg):
    if type(arg) == list:
        summa=0
        for i in arg:
            summa+= i
        return summa/int(len(arg))
    else:
        raise SyntaxError('false argument')
def power(arg):
    if len(arg) == 2:
        return arg[0]**arg[1]
    else:
        raise SyntaxError('fel argument')

arg_list = {'min':min ,'max':max,'sum':sum, 'mean':mean, 'power':power}

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
    
class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg

def assignment(wtok):
    result = expression(wtok)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            vars[str(wtok.get_current())]= result
            wtok.next()
        else:
            raise SyntaxError(f"expected name after not '{wtok.get_current}'")
    return  result

def expression(wtok):
    result = term(wtok)
    while wtok.get_current() in ['+','-']:
        op = wtok.get_current()
        wtok.next()
        if op == '+':
            result = result + term(wtok)
        if op == '-':
            result = result - term(wtok)
    return result

def term(wtok):
    result = factor(wtok)
    while wtok.get_current() in ['*','/']:
        op = wtok.get_current()
        wtok.next()
        if op == '*':
            result = result * factor(wtok)
        elif op == '/':
            try:
                result = result / factor(wtok)
            except ZeroDivisionError:
                raise SyntaxError('cannot devide by zero')
        else:
            wtok.next()
    return result

def arglist(wtok):
    result =[]
    if wtok.get_current() == '(':
        wtok.next()
        result.append(assignment(wtok)) 
        while wtok.get_current() == ',':
            wtok.next()
            result.append(assignment(wtok))
    if wtok.get_current() == ')':
        wtok.next()
        return result
    else: 
        SyntaxError(f'expected ) after ')

def factor(wtok):
    if wtok.get_current() in function_l:
        func = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            arg = assignment(wtok)
            if func == 'sin':
                result = math.sin(arg)
            elif func == 'cos':
                result = math.cos(arg) 
            elif func == 'exp':
                result = math.exp(arg)
            elif func == 'fib':
                if float(int(arg)//int(arg)) == float(arg)//arg and arg > 0:
                    result = fib(arg)
                else:
                    raise SyntaxError('illegal argument, argument must be a positive integer smaller than 45')
            elif func == 'fac':
                if float(arg) == float(int(arg)) and arg >= 0 and arg < 45:
                    result = fac(arg)
                    
                else:
                    raise SyntaxError('Argument must be a positive integer smaller than 45')
            elif func == 'log':
                if arg <= 0:
                    raise SyntaxError('Argument for log <= 0')
                else:
                    result= math.log(arg)
        else:
            raise SyntaxError(f"expected ')' not '{wtok.get_current()}'")

    elif wtok.get_current() in arg_list:
        func = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            result = arg_list[func](arglist(wtok))
        elif wtok.get_current() == ')':
            wtok.next()

    elif wtok.get_current () == '-':
        wtok.next()
        return -factor(wtok)

    elif wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok)
        wtok.next()
        
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.is_name():
        if wtok.get_current() in vars:
            result = vars[wtok.get_current()]
            wtok.next()
        else:
            raise SyntaxError(f"variable  not found")
    else:
        raise SyntaxError(f"expected ) not '{wtok.get_current()}' ")
    return result

def is_file(wtok):
    if wtok.is_name():
        wtok.next()
        if wtok.get_current() == '.':
            wtok.next()
            if wtok.is_name():
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def read_file(file):
    lines = []
    try:
        with open(file,'r') as f:
            for line in f:
                line = line.strip()
                lines.append(line)
        return lines
    except FileNotFoundError:
        print('file not found')

def main():
    print("Calculator version 2.0")
    while True:
        line = [input("Input : ")]
        wtok = TokenizeWrapper(line[0])
        if is_file(wtok) == True:
            line = read_file(line[0])
        if line != None:
            for line in line:
                # print(f'Input :  {line}')
                wtok = TokenizeWrapper(line)
                try:
                    if wtok.get_current() == 'quit':
                        break
                    elif wtok.get_current() == 'vars':
                        print(vars)
                    else:    
                        result = assignment(wtok)
                        if wtok.is_at_end():
                            print('Result: ', result)
                            vars['ans'] = result
                        else:
                            raise SyntaxError('Unexpected token')
                except SyntaxError as se:
                    print("*** Syntax: ", se.arg)
                    print(f"Error ocurred at '{wtok.get_current()}'" +
                    f" just after '{wtok.get_previous()}'")
                except TokenError:
                    print('*** Syntax: Unbalanced parentheses')

if __name__ == "__main__":
    main()




