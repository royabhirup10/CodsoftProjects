import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def choose(self):
        raise NotImplementedError("Define in subclass.")

class Human(Player):
    def choose(self):
        choice = ""
        while choice not in ["rock", "paper", "scissors"]:
            choice = input("Choose rock, paper, or scissors: ").lower()
        return choice

class RandomBot(Player):
    def choose(self):
        return random.choice(["rock", "paper", "scissors"])

class CopycatBot(Player):
    def __init__(self, name):
        super().__init__(name)
        self.last_user_choice = "rock"
    def choose(self):
        return self.last_user_choice
    def update(self, user_choice):
        self.last_user_choice = user_choice

class PredictiveBot(Player):
    def __init__(self, name):
        super().__init__(name)
        self.user_history = []
    def choose(self):
        if not self.user_history:
            return random.choice(["rock", "paper", "scissors"])
        most_common = max(set(self.user_history), key=self.user_history.count)
        prediction = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
        return prediction[most_common]
    def update(self, user_choice):
        self.user_history.append(user_choice)

def determine_winner(user, computer):
    rules = {
        ("rock", "scissors"): "user",
        ("scissors", "paper"): "user",
        ("paper", "rock"): "user",
        ("scissors", "rock"): "computer",
        ("paper", "scissors"): "computer",
        ("rock", "paper"): "computer"
    }
    if user == computer:
        return "tie"
    return rules.get((user, computer), "tie")

def main():
    print("Welcome to Adaptive Rock-Paper-Scissors!")
    print("Choose opponent: 1) Random Bot 2) Copycat Bot 3) Predictive Bot")
    bot_choice = input("Enter 1, 2, or 3: ")
    if bot_choice == "2":
        bot = CopycatBot("Copycat")
    elif bot_choice == "3":
        bot = PredictiveBot("Predictive Bot")
    else:
        bot = RandomBot("Random Bot")
    human = Human("You")
    rounds = 0
    while True:
        user_choice = human.choose()
        if hasattr(bot, 'update'):
            computer_choice = bot.choose()
            bot.update(user_choice)
        else:
            computer_choice = bot.choose()
        result = determine_winner(user_choice, computer_choice)
        print(f"You: {user_choice.title()} | {bot.name}: {computer_choice.title()}")
        if result == "user":
            print("You win this round!")
            human.score += 1
        elif result == "computer":
            print(f"{bot.name} wins this round!")
            bot.score += 1
        else:
            print("It's a tie!")
        rounds += 1
        print(f"Score: You {human.score} - {bot.name} {bot.score}")
        if input("\nPlay again? (y/n): ").lower() != "y":
            break
    print(f"\nTotal rounds played: {rounds}")
    print(f"Final Score: You {human.score} - {bot.name} {bot.score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
