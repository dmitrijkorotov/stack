class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def push(self, item):
        self.items.append(item)
                
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()
                
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]
                
    def size(self):
        return len(self.items)
                

def check_brackets(string):
    stack = Stack()
    oppenning_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    bracket_pairs = dict(zip(oppenning_brackets, closing_brackets))
    for char in string:
        if char in oppenning_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return 'Несбалансированно'
            elif char == bracket_pairs[stack.peek()]:
                stack.pop()
            else:
                return 'Несбалансированно'
            
    return 'Сбалансированно'

if __name__ == '__main__':
    print(check_brackets('(((([{}]))))'))
    print(check_brackets('[([])((([[[]]])))]{()}'))
    print(check_brackets('{{[()]}}'))
    print(check_brackets('}{}'))
    print(check_brackets('[[{())}]'))
    print(check_brackets('{{[(])]}}'))