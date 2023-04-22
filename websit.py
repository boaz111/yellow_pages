import re

def find_websites():
    # Open the input text file
    with open('list.txt', 'r') as file:
        data = file.read()

    # Use regular expressions to find website addresses
    websites = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)

    # Open the output file to write website addresses
    with open('websites.txt', 'w') as file:
        # Write each website address on a new line
        for website in websites:
            file.write(website + '\n')
