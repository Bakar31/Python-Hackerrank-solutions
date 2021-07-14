if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_arr_sorted = sorted(list(set(arr)), reverse = True)
    print(unique_arr_sorted[1])
