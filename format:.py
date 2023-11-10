import numpy as np

def calculate_probabilities(parameters, data, utilities):
    try:
        num_alternatives = len(utilities)
        num_data_points = len(data['X1'])
        probabilities = {f'P{i+1}': [] for i in range(num_alternatives)}
        
        # Calculate probabilities for each alternative and data point
        for i in range(num_data_points):
            utilities_values = [utility(data['X1'][i], data['X2'][i], data['Sero'][i], parameters) for utility in utilities]
            exp_utilities = np.exp(utilities_values)
            total_exp_utilities = np.sum(exp_utilities)
            alternative_probabilities = exp_utilities / total_exp_utilities
            
            # Store probabilities in the dictionary
            for j in range(num_alternatives):
                probabilities[f'P{j+1}'].append(alternative_probabilities[j])
        
        return probabilities
    
    except Exception as e:
        return f"Error: {str(e)}"


# Sample data
data = {
    'X1': [2, 3, 5, 7, 1, 8, 4, 5, 6, 7],
    'X2': [1, 5, 3, 8, 2, 7, 5, 9, 4, 2],
    'Sero': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Parameters
parameters = {
    'β01': 0.1,
    'β1': 0.5,
    'β2': 0.5,
    'β02': 1,
    'β03': 0
}

# Utilities for each alternative
utilities = [
    lambda x1, x2, sero, params: params['β01'] + params['β1'] * x1 + params['β2'] * x2,
    lambda x1, x2, sero, params: params['β02'] + params['β1'] * x1 + params['β2'] * x2,
    lambda x1, x2, sero, params: params['β03'] + params['β1'] * sero + params['β2'] * sero
]

# Calculate probabilities
probabilities = calculate_probabilities(parameters, data, utilities)

# Print probabilities
print(probabilities)

# Save probabilities to a .txt file
with open('probabilities.txt', 'w') as file:
    file.write(str(probabilities))
