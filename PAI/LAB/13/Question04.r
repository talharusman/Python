# Function to calculate income tax
calculate_tax <- function(income) {
  tax <- 0
  
  if (income < 30000) {
    tax <- 0
  } else if (income >= 30000 && income < 70000) {
    tax <- income * 0.10
  } else if (income >= 70000 && income < 100000) {
    tax <- income * 0.15
  } else {
    tax <- income * 0.20
  }
  
  return(tax)
}

# Accept income input from the user using scan()
print("Enter your annual income: ")
income <- scan(what = numeric(), nmax = 1)

if (income < 30000) {
    tax <- 0
} else if (income >= 30000 && income < 70000) {
    tax <- income * 0.10
} else if (income >= 70000 && income < 100000) {
    tax <- income * 0.15
} else {
    tax <- income * 0.20
}

# Print the result using print()
print(paste("The income tax for an income of", income, "is:", tax))
