# Listas que não podem ser modificadas.
# São utilizadas com parênteses ()

# tupla
nums = (3, 4, 6)

# Unpack nums into num1, num2, and num3
num1, num2, num3 = nums

# Construct even_nums list
even_nums = [2, num2, num3]

print(even_nums)


# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):

    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'

    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'

    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)

    # Return shout_words
    return shout_words


# Unpack and pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
print(yell1)
print(yell2)