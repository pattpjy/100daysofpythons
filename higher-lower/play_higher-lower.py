# Game art
from game_data import data
from art import logo, vs
import random

score = 0
game_should_continue = True
account_b = random.choice(data)
# Format the data into printable format name description, country


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name},a {account_description},from {account_country}"


# check Answer
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


while game_should_continue:
    # Get Random Names from Data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # Ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    # Check if user is correct
    # use if statement to check
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score is {score}")
# score keeping
# Make the game repeatable
# move name from position 2 to 1
# clear the screen between rounds
# end the game
# display final score
