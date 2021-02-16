def minion_game(string):


    #Set up the variables for their scores and the vowels 
    vowels = ['A','E','I','O','U']
    Kevin = 0
    Stuart = 0

    #Iterate through the length of the string
    for i in range(len(string)):
        #If the word starts with a vowel
        if string[i] in vowels:
            Kevin += len(string)-i
        else:
            Stuart +=len(string)-i

    if Stuart > Kevin:
        print("Stuart"+" "+ "%d" % Stuart)
    elif Kevin > Stuart:
        print("Kevin"+" "+'%d' % Kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)