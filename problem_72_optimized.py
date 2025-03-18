def sieve_of_euler(n):
    # Initialize the phi array where phi[i] will be set to i
    phi = list(range(n + 1))
    
    # Sieve of Euler to calculate Euler's Totient function for all numbers from 2 to n
    for p in range(2, n + 1):
        if phi[p] == p:  # p is a prime number
            for k in range(p, n + 1, p):
                phi[k] *= (p - 1)
                phi[k] //= p
                
    return phi

def count_reduced_proper_fractions(n):
    # Use the sieve of Euler to compute the totient values
    phi = sieve_of_euler(n)
    
    # Sum up phi(b) for b in range 2 to n
    return sum(phi[2:])

# Main program
n = int(input("Enter the value of n: "))
print(f"The number of reduced proper fractions for n = {n} is: {count_reduced_proper_fractions(n)}")
