# Predefined list of numbers
numbers <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Calculate the sum of even numbers
sum_even <- sum(numbers[numbers %% 2 == 0])

# Print the result
print(paste("The sum of even numbers is:", sum_even))