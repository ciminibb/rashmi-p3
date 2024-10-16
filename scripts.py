"""
This program reads from two TXT files: IF.txt and AlwaysRememberUsThisWay.txt,
then doing a few computations over their content. Ultimately, the results are
written to another TXT file.
"""

import socket

# This function counts words in a given file.
def wordCount(filepath):
    # Open the file in read mode and assign it to variable "file." Using the
    # context manager "with" automatically closed the file after the code in
    # its block has executed - preventing resource leaks.
    with open(filepath, "r") as file:
        content = file.read()
        words = content.split()
        return len(words)

# This function returns the three most common words in a given file.
def topThree(filepath):
    with open(filepath, "r") as file:
        content = file.read().lower()
        words = content.split()
        
        # Use a dictionary to store the frequency of each word.
        frequency = {}
        
        for word in words:
            if word not in frequency: frequency[word] = 1
            else: frequency[word] += 1
            
        # Sort the frequencies from greatest to least.
        sorted_frequencies = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        
        # Return the top 3 most frequent words.
        return sorted_frequencies[:3]
    
# This function returns the three most common words in a given file. However,
# all contractions are split into individual words.
def topThreeDelimited(filepath):
    with open(filepath, "r") as file:
        content = file.read().lower()
        
        # Create a mapping for common contractions, so that those encountered
        # in the file can be resolved to individual words. Then, replace all
        # contractions using the mapping.
        contractions = {
            "can't": "can not", "won't": "will not", "don't": "do not",
            "didn't": "did not", "isn't": "is not", "aren't": "are not",
            "wasn't": "was not", "weren't": "were not", "haven't": "have not",
            "hasn't": "has not", "hadn't": "had not", "doesn't": "does not",
            "mustn't": "must not", "wouldn't": "would not", "couldn't": "could not",
            "shouldn't": "should not", "mightn't": "might not", "shan't": "shall not",
            "it's": "it is", "i'm": "i am", "you're": "you are", "he's": "he is",
            "she's": "she is", "we're": "we are", "they're": "they are", "i've": "i have",
            "you've": "you have", "we've": "we have", "they've": "they have", 
            "i'll": "i will", "you'll": "you will", "he'll": "he will", 
            "she'll": "she will", "we'll": "we will", "they'll": "they will", 
            "i'd": "i would", "you'd": "you would", "he'd": "he would", 
            "she'd": "she would", "we'd": "we would", "they'd": "they would"
        }
        
        for contraction, resolution in contractions.items():
            content = content.replace(contraction, resolution)
            
        words = content.split() # We finally split the content into individual
                                # words after the contractions have been
                                # replaced.
        
        # Use a dictionary to store the frequency of each word.
        frequency = {}
        
        for word in words:
            if word not in frequency: frequency[word] = 1
            else: frequency[word] += 1
            
        # Sort the frequencies from greatest to least.
        sorted_frequencies = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        
        # Return the top 3 most frequent words.
        return sorted_frequencies[:3]

# This function gets the IP address of the machine running the container.
def getIp():
    try:
        # Get the hostname of the machine
        hostname = socket.gethostname()
        
        # Get the IP address using the hostname
        ip = socket.gethostbyname(hostname)
        return ip
    
    except Exception as e:
        return f"Error retrieving IP address: {e}"

# Below is the driver code that utilizes functions above to produce the desired
# output file.

# Save the filepaths to corresponding variables. They should be found at the
# given locations in the Docker container.
path_if = "/home/data/IF.txt"
path_always = "/home/data/AlwaysRememberUsThisWay.txt"

# Count the words in both files separately.
count_if = wordCount(path_if)
count_always = wordCount(path_always)

# Find the most common words in both files separately, with and without
# contractions.
top_if = topThree(path_if)
top_always = topThree(path_always)
top_if_star = topThreeDelimited(path_if)
top_always_star = topThreeDelimited(path_always)

# Get the IP address of the machine running the container.
ip_address = getIp()

# Create the desired output.
output = (
    f"'IF.txt' contains {count_if} words.\n"
    f"'AlwaysRememberUsThisWay.txt' contains {count_always} words.\n"
    f"The files contain {count_if + count_always} words in sum.\n"
    f"The 3 most common words in 'IF.txt' are as follows: {top_if}\n"
    f"The 3 most common words in 'AlwaysRememberUsThisWay.txt' are as follows: {top_always}\n"
    f"The 3 most common words in 'IF.txt' WITHOUT CONTRACTIONS are as follows: {top_if_star}\n"
    f"The 3 most common words in 'AlwaysRememberUsThisWay.txt' WITHOUT CONTRACTIONS are as follows: {top_always_star}\n"
    f"IP address of the machine is {ip_address}.\n"
)

# Print results to the console AND write them to a new TXT file at
# /home/data/output/ in the Docker container.
print(output)

with open("/home/data/output/result.txt", "w") as result:
    result.write(output)