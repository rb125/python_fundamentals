names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
# Add new data
names.append("Priscilla")
insurance_costs.append(8320.0)

# Combine names and insurance_costs into a single 2D list
medical_records = list(zip(names, insurance_costs))
print(medical_records)

# Find the size of the medical_records_list
num_medical_records = len(medical_records)
print("There are "+str(num_medical_records)+" medical records")

# Select the first medical record
first_medical_record = medical_records[0]
print("Here is the first medical record: "+str(first_medical_record))

# Sort the medical records list
medical_records.sort()
print("Here are the medical records sorted by insurance cost: "+str(medical_records))

# Slice the first three records
cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: "+str(cheapest_three))

# Slice the last three records
priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: "+str(priciest_three))

# Count elements in the list
occurences_paul = names.count("Paul")
print("There are "+str(occurences_paul)+" individuals with the name Paul in our medical records.")



