if __name__ == '__main__':
    N = int(input())
    res = []
    
    for _ in range(N):
        cmd = input().split()
        op = cmd[0]
        args = list(map(int, cmd[1:]))
        
        if op == "insert":
            res.insert(args[0], args[1])
        elif op == "print":
            print(res)
        elif op == "remove":
            res.remove(args[0])
        elif op == "append":
            res.append(args[0])
        elif op == "sort":
            res.sort()
        elif op == "pop":
            res.pop()
        elif op == "reverse":
            res.reverse()