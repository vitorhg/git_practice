# load a dataset and develop functionalities to extract simple insights from the data

# iterate over entries in a column to build a dictionary
# in which the keys are the names of languages
# and the values are the number of tweets in the given language

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv("tweets.csv")

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = df["lang"]

# Iterate over lang column in DataFrame
for entry in df["lang"]:

    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

# Print the populated dictionary
print(langs_count)

# {'en': 97, 'et': 1, 'und': 2}


# define a function with the functionality you developed in the previous exercise
# return the resulting dictionary from within the function
# and call the function with the appropriate arguments.
# the 'tweets.csv' file has been imported into the tweets_df variable

tweets_df = 0  # só pra não dar erro

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count


# Call count_entries(): result
result = count_entries(tweets_df, "lang")

# Print the result
print(result)

# {'en': 97, 'et': 1, 'und': 2}
