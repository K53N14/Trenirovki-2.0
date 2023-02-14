def add(root, num):
    if num < root[0]:
        if root[1] == None:
            root[1] = [num, None, None]
        else:
            add(root[1], num)
    if num > root[0]:
        if root[2] == None:
            root[2] = [num, None, None]
        else:
            add(root[2], num)

def find(root, num):
    if num == root[0]:
        return True
    elif num > root[0]:
        if root[2] == None:
            return False
        else:
            find(root[2], num)
    else:
        if root[1] == None:
            return False
        else:
            find(root[1], num)

def printleft(root, lvl):
    if root[1] != None:
        lvl += '.'
        print(lvl + str(root[1][0]))
        printleft(root[1], lvl)
    else:
        print(lvl)
def printkeyright(root, lvl):
    print(lvl + str(root[0]))
    if root[2] != None:
        lvl += '.'
        printkeyright(root[2], lvl)


with open('input.txt', 'r') as fin:
    rootflag = True
    for line in fin:
        request = line.split()
        if len(request) == 1:
            if root[1] != None:
                lvl = printleft(root, lvl = '')
            printkeyright(root, lvl = '')
        else:
            operation = request[0]
            num = int(request[1])
            if operation == 'ADD' and rootflag:
                rootflag = False
                root = [num,None,None]
                print('DONE')
            elif operation == 'ADD':
                if find(root,num):
                    print('ALREADY')
                else:
                    add(root, num)
                    print('DONE')
            if operation == 'SEARCH':
                if find(root,num):
                    print('YES')
                else:
                    print('NO')