# bmi_information = []
def number_checker (input_numbers):
  for number in input_numbers:
    if type(number) is int or float:
      return(True)
    return("This input is not valid number")

def input_members_calculator (input_numbers):
  member_number_input_values = 0
  for number in input_numbers:
    member_number_input_values = member_number_input_values + 1 

  if member_number_input_values == 2:
    return (True)
  elif member_number_input_values < 2 : 
    return("Please send one or two number(s)")
  elif member_number_input_values == 0 :
    return("Please enter two inputs")
  elif member_number_input_values > 2 :
    return ("The number od input is more standard calculator. Please enter only two inputs")


def bmi_calculator(input_numbers):
  weight, height = input_numbers

  bmi_estimation = weight / (height**2)

  return bmi_estimation


def reciver_data_for_bmi (input):
  input_numbers = input("Enter elements separated by space: ").split(',')

  transformed_data_to_number = []

  for element in input_numbers:
    if type(element) is str:
      transformed_data_to_number.append(float(element))
  
  input_members_validationv = input_members_calculator(transformed_data_to_number)
  input_type_validation = number_checker(transformed_data_to_number)

  if input_members_validationv is True and input_type_validation is True :
    BMI = bmi_calculator(transformed_data_to_number)

    return BMI



calculated_bmi = reciver_data_for_bmi(input)
print(calculated_bmi)





