def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 < y2: return 0
    elif y1 > y2: return 10000
    else:
        if m1 < m2: return 0
        elif m1 > m2: return 500 * (m1 - m2)
        else:
            if d1 <= d2: return 0
            else: return 15 * (d1 - d2)
        
if __name__ == '__main__':
    d1, m1, y1 = map(int, input().strip().split())
    d2, m2, y2 = map(int, input().strip().split())
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
