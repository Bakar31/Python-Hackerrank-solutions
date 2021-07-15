if __name__ == '__main__':
    mark = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mark.append([name, score])
    
    second_highest = sorted(set([score for name, score in mark]))[1]
    print('\n'.join(sorted([name for name, score in mark if score == second_highest])))
