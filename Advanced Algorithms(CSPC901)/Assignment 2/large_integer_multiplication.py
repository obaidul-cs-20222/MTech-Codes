import matplotlib.pyplot as plt


def classical_dc(x, y):
    
    if x < 10 or y < 10:
        return x * y, 1  

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    
    P1, ops1 = classical_dc(high_x, high_y)  
    P2, ops2 = classical_dc(high_x, low_y)   
    P3, ops3 = classical_dc(low_x, high_y)   
    P4, ops4 = classical_dc(low_x, low_y)    

    result = P1 * 10**(2*m) + (P2 + P3) * 10**m + P4
    ops = ops1 + ops2 + ops3 + ops4 + n 
    return result, ops


def karatsuba(x, y):
    
    if x < 10 or y < 10:
        return x * y, 1  

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)

    
    C, opsC = karatsuba(high_x, high_y)
    D, opsD = karatsuba(low_x, low_y)
    E, opsE = karatsuba(high_x + low_x, high_y + low_y)

    E = E - C - D
    result = C * 10**(2*m) + E * 10**m + D
    ops = opsC + opsD + opsE + n  
    return result, ops



sizes = [2**i for i in range(1, 10)]  
classical_counts, karatsuba_counts = [], []

for n in sizes:
    a = int("9" * n)
    b = int("8" * n)

    print(f"a: {a}, b: {b}")
    
    ans_classical, ops_classical = classical_dc(a, b)
    ans_karatsuba, ops_karatsuba = karatsuba(a, b)

    print(f"Size {n}: Classical ans = {ans_classical}, Karatsuba ans = {ans_karatsuba}, Equal? {ans_classical == ans_karatsuba}")
    print(f" Classical ops = {ops_classical}, Karatsuba ops = {ops_karatsuba}\n")
    classical_counts.append(ops_classical)
    karatsuba_counts.append(ops_karatsuba)
    if ops_classical > ops_karatsuba:
        print(f"For size {n}, Classical DC is more expensive than Karatsuba.")
    else:
        print(f"For size {n}, Karatsuba is more expensive than Classical DC.")


plt.figure(figsize=(8, 5))
plt.plot(sizes, classical_counts, marker='^', label="Classical DC O(n^2)")
plt.plot(sizes, karatsuba_counts, marker='s', label="Karatsuba O(n^1.585)")
plt.xlabel("Number of digits (n)")
plt.ylabel("Operation count")
plt.title("Operation Count: Classical DC vs Karatsuba")
plt.legend()
plt.grid(True)
plt.show()
