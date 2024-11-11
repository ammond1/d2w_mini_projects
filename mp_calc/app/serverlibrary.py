

def merge(array: list, p: int, q: int, r: int) -> None:
    nleft = q - p+1
    nright = r-q
    left = 0
    right = 0
    dest = p
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    while left<nleft and right<nright:
        if left_array[left] <= right_array[right]:
            array[dest] = left_array[left]
            left+=1
        else:
            array[dest] = right_array[right]
            right+=1
        dest +=1
    while left<nleft:
        array[dest] = left_array[left]
        left+=1
        dest+= 1
    while right<nright:
        array[dest] = right_array[right]
        right+=1
        dest+=1
    return array
        

def mergesort_recursive(array: list, p: int, r: int) -> None:
    if r-p ==0:
        return array
    elif r-p > 0:
        q = int((p+r)/2)
        mergesort_recursive(array,p,q)
        mergesort_recursive(array,q+1,r)
        merge(array, p,q,r)
        return array
        

def mergesort(array: list , byfunc = None) -> None:
    p = 0 
    r = len(array)-1
    if byfunc == None:
        mergesort_recursive(array,p,r)
        return array
    else:
        ls = []
        n_array = []
        for i in range(len(array)):
            ls.append(byfunc(array[i]))
        mergesort_recursive(ls,p,r)
        for i in range(len(ls)):
            n_array += [n for n in array if byfunc(n) == ls[i]]
        array[:] = n_array
        return array
    




class Stack:
    def __init__(self):
        self.__items= []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            item = self.__items.pop(-1)
            return item
        except:
            return None

    def peek(self) :
        try:
            item = self.__items[-1]
            return item
        except:
            return None

    @property
    def is_empty(self) :
        if len(self.__items) == 0:
            return True
        else:
            return False

    @property
    def size(self):
        return len(self.__items)

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  operators = '+-*/()'
  op_map = {
    '+' : lambda a,b : a+b,
    '-' : lambda a,b : a-b,
    '/' : lambda a,b : a//b,
    '*' : lambda a,b : a*b,
  }

  def __init__(self, string=""):
    self._expr = ""
    if self._valid_string(string): # checks if input contains non valid
       self._expr = string

  def _valid_string(self, string: str) -> bool: # makes sure that the input only contains the operators and operands
    valid = False
    for char in string:
      valid = char in EvaluateExpression.valid_char
      if not valid:
        break
    return valid

  @property
  def expr(self):
    return self._expr

  @expr.setter
  def expr(self, new_expr):
    if self._valid_string(new_expr):
        self._expr = new_expr
    else:
       self._expr = ""
  
  def insert_space(self):
    new_string =""
    for i in range(len(self.expr)):
      if self.expr[i] in self.operators:
        new_string += " " + self.expr[i] + " "
      else:
        new_string += self.expr[i]
    return new_string


  def division(self, a: int, b: int): # account for division by zero
      if b == 0:
        return None
      else:
        return a // b

  def process_operator(self, operand_stack, operator_stack):
    b = int(operand_stack.pop())
    a = int(operand_stack.pop())
    op = operator_stack.pop()
    if b == 0 and op == "/":
      evaluate = self.division(a, b) # for divide by 0 exception ** returns None if divided by zero
    else:
      evaluate = self.op_map[op](a,b)
    if operator_stack.peek() == '(':
      operator_stack.pop()
    operand_stack.push(evaluate)

  def invalid_next(self, operand_stack): #make sure nonetype is not processed
    error_msg = "ZeroDivisionError"
    if not operand_stack.is_empty:
      if operand_stack.peek() == None: # added condition if a None object is pushed by process_operator
        print("ran")
        return True, error_msg #set as error message first
      else:
        return False, None
    else:
      return False, None
    
  def evaluate(self): ## added a check condition for every case where a while loop is needed, man its hella ugly but i covered all cases
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split() # makes a list of strings
    for char in tokens:
      if self.invalid_next(operand_stack)[0]: #
        return self.invalid_next(operand_stack)[1] #
      if char == '+' or char =="-":
        while operator_stack.is_empty is False and operator_stack.peek() not in "()":
          if self.invalid_next(operand_stack)[0]: #
            return self.invalid_next(operand_stack)[1] #
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char == "*" or char == "/":
        while operator_stack.is_empty is False and operator_stack.peek() in "*/":
          if self.invalid_next(operand_stack)[0]:
            return self.invalid_next(operand_stack)[1]
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char == ")":
        while operator_stack.is_empty is False and operator_stack.peek() != "(":
          if self.invalid_next(operand_stack)[0]:
            return self.invalid_next(operand_stack)[1] 
          self.process_operator(operand_stack, operator_stack)
      elif char == "(":
        operator_stack.push(char)
      else:
        operand_stack.push(char)
    while operator_stack.is_empty is False:
      if self.invalid_next(operand_stack)[0]:
            return self.invalid_next(operand_stack)[1]
      self.process_operator(operand_stack, operator_stack)
    if self.invalid_next(operand_stack)[0]:
      return self.invalid_next(operand_stack)[1]
    else:
      return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





