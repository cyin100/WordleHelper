class green:
  def __init__(self, letter, pos):
    self.letter = letter
    self.pos = pos

with open('fiveletterwords.txt') as file:
    wordlist = set(file.read().split('\n'))
    file.close()

blacklist = set()
greenlist = set()
tempwordlist = set(wordlist)
yellowlist = dict.fromkeys(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
for letter in yellowlist:
    yellowlist[letter] = []

while True:
    guess = input('GUESS: ')
    results = input('RESULT: ')
    
    for i in range(5):
        if results[i].upper() == 'B':
            blacklist.add(guess[i].lower())
        if results[i].upper() == 'G':
            greenlist.add(green(guess[i].lower(), i))
        if results[i].upper() == 'Y':
            yellowlist[guess[i].lower()].append(i)

    for word in wordlist:
        for char in blacklist:
            if char in word:
                tempwordlist.discard(word)
        for char in greenlist:
            if char.letter != word[char.pos]:
                tempwordlist.discard(word)
        for letter in yellowlist:
            for position in yellowlist[letter]:
                if letter in word:
                    if word.index(letter) == position:
                        tempwordlist.discard(word)
                else:
                    tempwordlist.discard(word) 

    wordlist = set(tempwordlist)

    if len(wordlist) == 0:
        print('ERROR - word not found, try double checking your inputs')
        break
    else:
        print(str(wordlist))