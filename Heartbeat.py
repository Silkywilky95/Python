"""
I used chat gtp to generate this code so I could get caught up with the class grading 
https://chatgpt.com/share/6704788c-805c-8011-a576-442a90e6e406
"""



# Step 1: Initialize total variable for heart rate
total_heart_rate= 0
 
# Step 2: Define the times of day and create an empty list for heart rate readings
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []

# Step 3: Loop through each time slot and get heart rate input
for time in time_slots:
    # Ask user for heart rate input and convert it to an integer
    rate = int(input(f"Enter your heart rate for {time} (in BPM): "))
    # Append the time and corresponding heart rate to the heart_rates list
    heart_rates.append([time, rate])

# Step 4: Display the entered heart rates
print(heart_rates)

# Step 5: Calculate total heart rate and print each time with the corresponding heart rate
for i in range(len(time_slots)):
    time = heart_rates[i][0]
    rate = heart_rates[i][1]
    total_heart_rate += rate
    print(f"At {time}, your heart rate was: {rate} BPM")

# Step 6: Calculate the average heart rate and display it
average_heart_rate = total_heart_rate / len(time_slots)
print(f"Your average heart rate today was: {average_heart_rate:.0f} BPM")
