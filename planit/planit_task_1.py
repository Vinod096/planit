string = "character"

characters = {}

def word():
    for letter in string:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    most_occurring = max(characters, key=characters.get)
    return most_occurring

print("Most occuring character is: ", word())
