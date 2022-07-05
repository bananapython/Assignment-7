#  File: ExpressionTree.py

#  Description: This program creates an expression tree from a given infix expression, evaluates it, and prints it and the prefix/postfix expressions out.

#  Student Name: Emily Wang

#  Student UT EID: ew6985

#  Partner Name: Sean Thomas

#  Partner UT EID: sft372

#  Course Name: CS 313E

#  Unique Number: 86439

#  Date Created: 7/1/2022

#  Date Last Modified: 7/4/2022


import sys
import operator

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = Node()
        self.nodes = Stack()
        self.current = self.root
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        tokens = expr.split()
        for tkn in tokens:
            if tkn == "(":
                self.current.lChild = Node()
                self.nodes.push(self.current)
                self.current = self.current.lChild
            elif tkn == ")":
                if not self.nodes.is_empty():
                    self.current = self.nodes.pop()
            elif tkn in operators:
                self.current.data = tkn
                self.nodes.push(self.current)
                self.current.rChild = Node()
                self.current = self.current.rChild
            else:
                self.current.data = tkn
                self.current = self.nodes.pop()
    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode): 
        prefix=self.pre_order(aNode)
        prefix=prefix.split() #turn from string to mutable type
        stack=[]
        op = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv, \
               "//":operator.floordiv,"%" : operator.mod,"**" : operator.pow,}
                #uses lookup dictionary method instead of eval to avoid eval's problems

        while prefix: #converts from prefix to infix while evaluating
            char=prefix.pop()
            if char in operators:
                operand1=float(stack.pop())
                operand2=float(stack.pop())
                result=op[char](operand1,operand2)
                stack.append(result)
                
            else:
                stack.append(char)
        
        return stack[0]
    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        if aNode != None:
            expr = aNode.data + " " + str(self.pre_order(aNode.lChild)) + " " + str(self.pre_order(aNode.rChild))
            tokens = expr.split()
            spacedExpr = ""
            for tkn in tokens:
                spacedExpr += tkn + " "
        
            return spacedExpr
        return ""
    
    
    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        if aNode != None:
            expr = str(self.post_order(aNode.lChild))  + str(self.post_order(aNode.rChild)) + aNode.data
            tokens = expr.split()
            spacedExpr = ""
            for tkn in tokens:
                spacedExpr += tkn + " "
            return spacedExpr
        return ""

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
    
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))
    
    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())
    
    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())
    
if __name__ == "__main__":
    main()

