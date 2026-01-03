try:
    # Get the numerical score from the user
    score = float(input("Enter the numerical score (0-100): "))

    # Validate the input to ensure it's within the valid range
    if 0 <= score <= 100:
        # Determine the letter grade based on the score
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'

        # Display the calculated grade
        print(f"The corresponding letter grade is: {grade}")
    else:
        print("Invalid score. Please enter a value between 0 and 100.")

except ValueError:
    print("Invalid input. Please enter a numeric value for the score.")
