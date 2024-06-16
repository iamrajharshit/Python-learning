"""remove adjacent duplicate using stacks"""
#str="azxxzy"
#output=ay



str="azxxzy"
def adj_dup(str):
    stack=[]
    for chr in str:
        if chr not in stack:
            stack.append(chr)
        else:
            stack.remove(chr)
        
    return stack

# print(adj_dup(str))

def adjDup(str):
    stack=[]
    for char in str:
        if len(stack)==0 or stack[-1]!=char:
            stack.append(char)
        else:
            stack.pop()        
    return "".join(stack)

# print(adjDup(str))

'''
Balance brackets 
'''
#input: [()]{}{[()()]()}
#output: Balanced

def bal(str2):
    stack=[]
    for chr in str2:
        if chr in ['{','[','(']:
            pass
            

