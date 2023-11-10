# CiSTUP_Assignment

Write a Python function to calculate the probability of each alternative in a multinomial choice
setting using the logistic function, given a set of parameters and independent variables. The
function should be generic enough to handle any number of alternatives and independent variables.
In a multinomial logit model, the probability of each alternative is calculated using a logistic
function. For each alternative, a deterministic utility (V) is computed based on a linear
combination of independent variables and their respective coefficients (β). The probability of each
alternative is the exponential of its utility divided by the sum of exponentials of all utilities.
Given Sample Data:

data = {
'X1': [2, 3, 5, 7, 1, 8, 4, 5, 6, 7],
'X2': [1, 5, 3, 8, 2, 7, 5, 9, 4, 2],
'Sero': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

Deterministic Utilities:

V1 = β01 + β1X1 + β2X2
V2 = β02 + β1X1 + β2X2
V3 = β03 + β1Sero + β2Sero

Probabilities to Compute:
P1 =

exp(V1)

exp(V1) + exp(V2) + exp(V3)
P2 =

exp (V2)

exp (V1) + exp (V2) + exp (V3)
P3 =

exp(V3)

exp(V1) + exp(V2) + exp(V3)

Parameters:

β01 = 0.1, β1 = 0.5, β2 = 0.5, β02 = 1, β03 = 0

Tasks

Write a Python function called ‘calculate_probabilities’ that takes the following inputs:
- Parameters: A dictionary containing the β coefficients.
- Data: A dictionary containing the independent variables (X1, X2, Sero, etc.).

Page 3 of 3

- Utilities: A list of functions that define the deterministic utilities for each alternative based on
the given parameters and data.
Your function should output a new dictionary with keys representing each alternative and values
as lists containing the calculated probabilities for each data point. Save this output in .txt file
format.

Ensure your code is well-commented to explain the logic used at each step.
Bonus: Include error handling for possible input errors such as mismatched dimensions between
parameters and data points.

Evaluation Criteria:
  • Correctness of the logistic function implementation.
  • Ability to handle a dynamic number of alternatives and independent variables.
  • Code readability and use of comments.
  • Proper error handling.
