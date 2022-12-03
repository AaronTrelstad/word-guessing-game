import random
mystery = ['apple', 'grape', 'runner', 'mathematics', 'finance', 'sports', 'games', 'code', 'school', 'funny', 'track', 'books', 'amazing', 'iowa', 'is']
word = random.randint(0,len(mystery))
print(f"Your mystery word is {len(mystery[word])} letters")
guess = 0
i = 0
for i in range(5):
    while True:
        guess = input(f"Guess {i + 1}: ")
        if len(guess) == len(mystery[word]):
            break
    p = 0
    i+=1
    if str(guess.lower()) != str(mystery[word]):
        score = 0
        for x in range(len(mystery[word])):
            guess = guess.lower()
            cword = mystery[word]
            if guess[x] == cword[x]:
                score+=1
            if guess[x] == cword[x]:
                print(guess[x])
        if score == 0 and p == 0:
            print("No Correct Letters")
            p+=1
        if score > 0 and p == 0:
            print(f"You had {score} letter(s) correct")
            p+=1
    if str(guess.lower()) == str(mystery[word]):
        break
print(f"The word was {mystery[word]}")
        
