# 백준 4949번 균형잡힌 세상

while True:
    str = input()
    stack = []

    if str == '.':
        break
    else:
        bracket =[]
        
        for s in str:
            if s == '(' or s == ')' or s == '[' or s == ']':
                bracket.append(s)

        for b in bracket:
            if b == '(' or b == '[':
                stack.append(b)
            elif b == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else: stack.append(b)
            elif b == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else: stack.append(b)
        
        if len(stack): print('no')
        else: print('yes')