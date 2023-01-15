# Create calculate_insurance_cost() function below:
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

  output_message = "The estimated insurance cost for "+name+" is "+str(estimated_cost)+" dollars"
  return estimated_cost, output_message

# Initial variables for Maria
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Estimate Maria's insurance cost
insurance_cost, output_message = calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, "Maria")

print(output_message)
# Initial variables for Omar
age = 35
sex = 1
bmi = 22.2
num_of_children = 0
smoker = 1

# Estimate Omar's insurance cost
insurance_cost, output_message = calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, "Omar")
print(output_message)
