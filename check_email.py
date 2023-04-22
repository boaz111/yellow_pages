import os

# Read the email addresses from a text file
with open('list.txt', 'r') as f:
    emails = f.read().splitlines()

# Define the ping function
def ping_check(email):
    response = os.system("ping -c 1 " + email)
    if response == 0:
        print(email + " is alive")
        return "Alive"
    else:
        print(email + " is not responding")
        return "Not Responding"

# Create a dictionary to store the ping results for each email
ping_results = {}

# Iterate over the email list and perform the ping check
for email in emails:
    ping_result = ping_check(email)
    ping_results[email] = ping_result

# Generate a report of the ping results
report = "Ping Results:\n"
for email, result in ping_results.items():
    report += "{}: {}\n".format(email, result)

# Write the report to a text file
with open('ping_report.txt', 'w') as f:
    f.write(report)

print("Ping check complete. Report saved to 'ping_report.txt'")
