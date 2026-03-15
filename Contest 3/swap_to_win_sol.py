import sys

def solve():
    # Use sys.stdin.read for faster input in competitive programming
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    ptr = 0
    num_testcases = int(input_data[ptr])
    ptr += 1

    for _ in range(num_testcases):
        n = int(input_data[ptr])
        m = int(input_data[ptr+1])
        ptr += 2
        
        goal_string = list(input_data[ptr])
        ptr += 1
        
        strings = []
        for i in range(n):
            strings.append(list(input_data[ptr]))
            ptr += 1

        operations = []

        for a in range(m):
            if strings[0][a] == goal_string[a]:
                continue
            
            found = False
            # 1. Search in the rest of the first string (s1)
            for j in range(a + 1, m):
                if strings[0][j] == goal_string[a]:
                    # Operation 1: Swap within s1
                    strings[0][a], strings[0][j] = strings[0][j], strings[0][a]
                    operations.append(f"1 1 {a+1} {j+1}")
                    found = True
                    break
            
            print(strings)
            if found:
                continue

            # 2. Search in other strings (s2 to sN)
            for b in range(1, n):
                for j in range(m):
                    if strings[b][j] == goal_string[a]:
                        # Step A: If char is in the wrong column, move it to column 'a' in strings[b]
                        if j != a:
                            strings[b][a], strings[b][j] = strings[b][j], strings[b][a]
                            operations.append(f"1 {b+1} {a+1} {j+1}")
                        
                        # Step B: Swap the char from strings[b][a] into strings[0][a]
                        strings[0][a], strings[b][a] = strings[b][a], strings[0][a]
                        operations.append(f"2 1 {b+1} {a+1}")
                        
                        found = True
                        break
                if found:
                    break
            
        
        print(len(operations))
        for op in operations:
            print(op)

if __name__ == "__main__":
    solve()