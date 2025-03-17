def euler_totient(n):
    # Initialize a list to store phi values for every number from 1 to n
    phi = list(range(n + 1))  # phi[i] will store the value of φ(i)
    
    # Using the sieve method to compute Euler's Totient Function
    for i in range(2, n + 1):
        if phi[i] == i:  # i is a prime number
            for j in range(i, n + 1, i):
                phi[j] *= (i - 1)
                phi[j] //= i
    
    return phi

def count_reduced_proper_fractions(N):
    # Calculate totient function values from 2 to N
    phi_values = euler_totient(N)
    
    # Sum up the phi values from 2 to N to get the total number of reduced proper fractions
    total_fractions = sum(phi_values[2:])  # Exclude phi(1) since it is not needed
    return total_fractions

# Take user input
N = int(input("Enter the value of N: "))

# Calculate and display the result
print("The number of reduced proper fractions for N =", N, "is:", count_reduced_proper_fractions(N))
