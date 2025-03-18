def estimate_binomial_divisible_by_10(m, n, reference_m, reference_result):
    
    # Calculate the scaling factor based on m
    scaling_factor = m / reference_m
    
    # Estimate the result by scaling the reference result, and make sure it's an integer
    estimated_result = int(reference_result * scaling_factor)  # Ensure the result is an integer
    
    return estimated_result

def general_estimation_program():
   
    # Input for the reference values (provided in the problem)
    reference_m = int(input("Enter the reference value for m (e.g., 10^9): "))
    reference_result = int(input("Enter the reference result for T(reference_m, n) (e.g., 989697000): "))
    
    # Input for the larger m and n values for which we need to estimate the result
    m = int(input("Enter the larger value for m (e.g., 10^18): "))
    n = int(input("Enter the corresponding value for n (e.g., 10^12 - 10): "))
    
    # Estimate T(m, n)
    estimated_result = estimate_binomial_divisible_by_10(m, n, reference_m, reference_result)
    
    # Output the estimated result
    print(f"Estimated T({m}, {n}) = {estimated_result}")

if __name__ == "__main__":
    general_estimation_program()
