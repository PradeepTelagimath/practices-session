def display_study_hours():
    # Read hours per day and study days
    hours_per_day = int(input())
    study_days = int(input())
    
    # Calculate total study hours
    total_hours = hours_per_day * study_days
    
    # Print formatted output
    print(f"Total Study Hours: {total_hours}")

# Call the function once
display_study_hours()