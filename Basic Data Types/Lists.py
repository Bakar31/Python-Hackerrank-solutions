if __name__ == '__main__':
    N = int(input())
    List = []
    for i in range(N):
        args = input().strip().split(" ")
        if args[0] == "append":
            List.append(int(args[1]))
        elif args[0] == "insert":
            List.insert(int(args[1]), int(args[2]))
        elif args[0] == "remove":
            List.remove(int(args[1]))
        elif args[0] == "pop":
            List.pop()
        elif args[0] == "sort":
            List.sort()
        elif args[0] == "reverse":
            List.reverse()
        elif args[0] == "print":
            print (List)
