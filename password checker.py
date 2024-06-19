import re

def check_password_strength(password):
    # Criteria for password complexity
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Check if all criteria are met
    all_criteria_met = all([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Determine strength based on the number of criteria met
    if all_criteria_met:
        strength = 'Strong'
    else:
        strength = 'Weak'
    
    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")
    
    return strength, feedback

# Example usage:
password = input("Enter a password to check its strength: ")
strength, feedback = check_password_strength(password)
print(f"Password Strength: {strength}")
if feedback:
    print("Feedback:")
    for tip in feedback:
        print(f"- {tip}")
