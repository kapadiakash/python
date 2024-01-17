# def is_armstrong_number(n):
#     # अंकों की संख्या को स्ट्रिंग में परिवर्तित करें
#     num_str = str(n)
    
#     # संख्या की लंबाई (अंकों की संख्या) को जानें
#     num_length = len(num_str)
    
#     # अर्मस्ट्रांग संख्या की संभावित संख्या को जोड़ने के लिए उपयुक्त गणना करें
#     armstrong_sum = sum(int(digit) ** num_length for digit in num_str)
    
#     # वास्तविक संख्या के समान होने की जाँच करें
#     return armstrong_sum == n

# # संख्या की जाँच करें कि क्या वह अर्मस्ट्रांग संख्या है या नहीं
# number = 153
# if is_armstrong_number(number):
#     print(number, "is an Armstrong number.")
# else:
#     print(number, "is not an Armstrong number.")


def is_armstrong_number(number):
    # Convert the number to a string to get the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Example: Check if 153 is an Armstrong number
number_to_check = 153
if is_armstrong_number(number_to_check):
    print(f"{number_to_check} is an Armstrong number")
else:
    print(f"{number_to_check} is not an Armstrong number")
