import random
mystery = ['apple', 'grape', 'runner', 'mathematics', 'finance', 'sports', 'games', 'code', 'school', 'funny', 'track', 'books', 'amazing', 'iowa', 'is']
word = random.randint(0,14)
print(f"Your mystery word is {len(mystery[word])} letters")
guess = 0
i = 0
for i in range(5):
    while True:
        guess = input(f"Guess {i + 1}: ")
        if len(guess) == len(mystery[word]):
            length = len(guess)
            break
    p = 0
    i+=1
    if str(guess.lower()) != str(mystery[word]):
        score = 0
        sim = 0
        guess = guess.lower()
        cword = mystery[word]
        gword = mystery[word]
        cl = []
        sl = []
        for x in range(length):
            if guess[x] == cword[x]:
                cl.append(guess[x])
                score+=1
        if score > 0:
            print(f"Correct Letters: {cl}")
        if score == 0 and p == 0:
            print("No Correct Letters")
            p+=1
        for g in range(length):
            for h in range(length):
                if guess[g] == cword[h]:
                    sl.append(guess[g])
                    sim+=1
                    continue
                else:
                    continue
        if sim > 0:
            print(f"Similar letters: {sl}")
        if sim == 0:
            print("No similar letters")
    if str(guess.lower()) == str(mystery[word]):
        break
print(f"The word was {mystery[word]}")
        
