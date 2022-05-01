#Morse code is a code where each letter of the English alphabet, each digit, and various
#punctuation characters are represented by a series of dots and dashes. Table 8-4 shows part of the code.
#Write a program that asks the user to enter a string, and then converts that string to Morse code.

#Character Code Character Code Character Code Character Code
#space space   ***** 6 –.... ****** G ––. ****  Q ––.–
#comma ––..––  ***** 7 ––... ****** H .... ***  R .–.
#period .–.–.– ***** 8 –––.. ****** I .. ****** S ...
#question mark ..––.. *** 9 ––––. * J .––– **** T –
#0 ––––– *** A .– **** K –.– ******* U ..–
#1 .–––– *** B –... ** L .–.. ****** V ...–
#2 ..––– *** C –.–. ** M –– ******** W .––
#3 ...–– *** D –.. *** N –. ******** X –..–
#4 ....– *** E . ***** O ––– ******* Y –.–
#5 ..... *** F ..–. ** P .––. ****** Z ––..


Morse_code = {'space' : 'space','comma' : '––..––', 'period' : '.–.–.–', 'question_mark' : '..––..',
              'zero' : '–––––', 'one' : '.––––', 'two' : '..–––', 'three' : '...––', 'four' : '....–',
              'five' : '.....', 'six' : '–....', 'seven' : '––...', 'eight' : '–––..', 'nine' : '––––.',
              'A' : '.–', 'B' : '–...', 'C' : '–.–.', 'D' : '–..', 'E' : '.', 'F' : '..–.', 'G' : '––.',
              'H' : '....', 'I' : '..', 'J' : '.–––', 'K' : '–.–', 'L' : '.–..', 'M' : '––', 'N' : '–.',
              'O' : '–––', 'P' : '.––.', 'Q' : '––.–', 'R' : '.–.', 'S' : '...', 'T' : '–', 'U' : '..–',
              'V' : '...–', 'W' : '.––', 'X' : '–..–', 'Y' : '–.–', 'Z' : '––..'}

#values = [space, comma, period, question_mark, zero, one, two, three, four, five, six, seven,eight, nine, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]


def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += Morse_code[letter] + ' '
        else:
            cipher += ' '
    return cipher

def main():
    message = str(input("Enter alpha or value : "))
    result =encrypt(message.upper())
    print("Morse code is : ", result)

main()