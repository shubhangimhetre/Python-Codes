# Yeh rock paper scissors game ka program hai. Iss game ko aap computer ke against kheloge. 
# Iss game ke 3 rules hai 
# 1.Rock Paper se haar jata hai
# 2.Paper Scissors se haar jaata hai 
# 3.Aur, Scissors Rock se.
# Appko pehle rock,paper ya scissors mei se chose karna hoga. Aur uske baad computer randomly inme se ek option chose karega. 
# Firr, upar diye gaye rules ke hisab se result aayega. Jaise: * Agar aapne "Rock" chose kiya aur computer ne "Scissors"
# To aap jeet jaoge kyunki "Rock" "Scissors" ko hara deta hai. ( Rule 3 )

# Aap iss game ke rules issse seekh sakte hai. Topics covered: * semantic/syntactic problems in if/else
# semantic error in while conditions
# errors in variable naming


print("")
print("Welcome to Rock, Paper,Scissor game🙏")
print("")

from random import randint

def win():
    print ("You win!👏🏼✔️✔️🥳")
def lose():
    print ("You lose!😢")
    print("Try again")


while True:
    player_choice = input("What do you pick? (rock, paper, scissor) : ")
    print("")
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissor']
    computer_choice = moves[random_move]
    if player_choice == computer_choice:
        print ("Draw!")
    elif player_choice == 'rock' and computer_choice == 'scissor':
        win()
    elif player_choice == 'paper' and computer_choice == 'scissor':
        lose()
    elif player_choice == 'scissor' and computer_choice== 'paper':
        win()
    elif player_choice == 'scissor' and computer_choice == 'rock':
        lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    elif player_choice == 'rock' and computer_choice== 'paper':
        lose()
    print("")
    again = input("Do you want to play again? (y or n) : ").strip()
    if again=='y':
       continue
    elif again == 'n':
        print("          THANK YOU🙏")
        break 