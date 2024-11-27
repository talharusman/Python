# Prompt the user to enter the student's score
score <- 87

if (score >= 90) {
  grade <- "A"
} else if (score >= 80) {
  grade <- "B"
} else if (score >= 70) {
  grade <- "C"
} else {
  grade <- "Fail"
}

print(paste("The student's grade is:", grade))