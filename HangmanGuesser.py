import numpy as np


# Initialization | Run Before Everything
print("Processing Dictionaries...")
words = []

content = open(r"FreqDict.txt").read()
words.extend(content.split("\n"))

nw = []
for wd in words:
    nw.append(wd.upper().split(" "))

freq, wds = np.array(nw).T[:2]
freq = np.int32(freq)
idx = np.where(np.char.isalpha(wds))
fin_freq, fin_wds = freq[idx], wds[idx]

freqdict = {}
for i in range(len(fin_wds)):
    if fin_wds[i] in freqdict:
        freqdict[fin_wds[i]] += fin_freq[i]
    else:
        freqdict[fin_wds[i]] = fin_freq[i]

fin_wds = list(freqdict.keys())

# Necessary Functions

def letterguess(word_len, startlist, roundno, usedletters, verbose):
    revised_words = [wd for wd in fin_wds if len(wd) == word_len]
    
    def check_word(word):
        for idx in range(len(word)):
            if word[idx] in usedletters: # if letter is in used letters, then could be bad word, or already found good word
                if word[idx] != startlist[idx]:
                    return False
            if startlist[idx] == "*":
                continue
            elif startlist[idx] != word[idx]:
                return False
        return True
    
    revised_words2 = [i for i in revised_words if check_word(i)]
    if verbose:
        print("Some Possible Words:")
        print(np.random.choice(revised_words2, size = 10))
    alpha = np.array(list("abcdefghijklmnopqrstuvwxyz".upper()))
    
    freq = {}
    for wd in revised_words2:
        for i in wd:
            if i in freq:
                freq[i] += (1 * freqdict[wd])
            else:
                freq[i] = (1 * freqdict[wd])
    
    for let in usedletters:
        freq[let] = 0
    
    probs = []
    for i in alpha:
        try:
            probs.append(freq[i])
        except KeyError:
            probs.append(0)
    probs = np.array(probs)
    probs = probs / np.sum(probs)
    let = np.random.choice(alpha, p = probs)
    
    return let

def guess(word, totattempts = 10, verbose = True):
    if verbose:
        print("Word to Guess:", word)
        print("Let the Game Begin!")
        print()
    startlist = ["*" for i in range(len(word))]
    wordlist = list(word.upper())
    attempts = totattempts
    usedletters = set()
    roundno = 1
    while attempts > 0:
        if verbose:
            print("Guess #" + str(roundno), "| Attempts:", attempts)
        letter = letterguess(len(word), startlist, roundno, usedletters, verbose).upper()
        if verbose:
            print("Guess is:", letter)
            
        if letter in usedletters:
            raise Exception("Letter Already Used!")
        
        usedletters.add(letter)
        
        if letter in wordlist:
            for idx in range(len(wordlist)):
                if wordlist[idx] == letter:
                    startlist[idx] = letter
            if verbose:
                print("Correct Guess!")
        else:
            if verbose:
                print("Incorrect Guess!")
            attempts -= 1
            
        if verbose:
            print()
            print("Word:", "".join(startlist))
        roundno += 1
        if startlist == wordlist:
            if verbose:
                print("Guesser Won! It took", totattempts - attempts, "attempts.")
                print()
            return 1
    if verbose:
        print("Guesser Lost! It ran out of attempts.")
        print()
    return 0

# Final Game
print("Done.")

word = str(input("Enter your word: "))
guess(word)

# Calculating Final Winrate for Word
print("Calculating Overall Winrate...")
winrate = 0
for i in range(100):
    winrate += guess(word, verbose = False)
print("Final Winrate for", word.upper() + ":", str(winrate) + "%")