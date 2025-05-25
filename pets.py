import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 100
        self.happiness = 50
        self.age = 1
        self.is_sick = False
        self.foods = {"Apple": {"hunger_reduction": 15, "happiness_boost": 5},
                      "Beef": {"hunger_reduction": 25, "happiness_boost": 10},
                      "Carrot": {"hunger_reduction": 10, "happiness_boost": 3}}
        self.games = {"Hide and Seek": {"energy_cost": 20, "happiness_boost": 15},
                      "Frisbee": {"energy_cost": 30, "happiness_boost": 20},
                      "Roll Over": {"energy_cost": 10, "happiness_boost": 10}}

    def feed(self, food_choice):
        if food_choice not in self.foods:
            return "Please enter a valid food choice!"
        if self.hunger <= 10:
            return f"{self.name} is not hungry and doesn't need to eat!"
        food = self.foods[food_choice]
        self.hunger = max(0, self.hunger - food["hunger_reduction"])
        self.happiness += food["happiness_boost"]
        return f"You fed {self.name} {food_choice}. Its hunger decreased by {food['hunger_reduction']} and happiness increased by {food['happiness_boost']}!"

    def play(self, game_choice):
        if game_choice not in self.games:
            return "Please enter a valid game choice!"
        if self.energy < 20:
            return f"{self.name} is too tired to play games!"
        game = self.games[game_choice]
        self.energy -= game["energy_cost"]
        self.happiness += game["happiness_boost"]
        return f"You played {game_choice} with {self.name}. Its energy decreased by {game['energy_cost']} and happiness increased by {game['happiness_boost']}!"

    def sleep(self):
        if self.energy > 80:
            return f"{self.name} is full of energy and doesn't need to sleep!"
        old_energy = self.energy
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 10)
        self.age += 1
        energy_increase = self.energy - old_energy
        self.is_sick = random.random() < 0.1
        result = f"{self.name} took a nap. Energy increased by {energy_increase}, hunger increased by 10, and age increased by 1 year!"
        if self.is_sick:
            result += f"\nOh no! {self.name} got sick after sleeping!"
        return result

    def heal(self):
        if not self.is_sick:
            return f"{self.name} is healthy and doesn't need treatment!"
        self.is_sick = False
        self.happiness += 10
        self.energy = max(0, self.energy - 15)
        return f"You cured {self.name}'s illness. Its happiness increased by 10 and energy decreased by 15!"

    def check_status(self):
        status = f"{self.name}'s Status:\n"
        status += f"Age: {self.age}\n"
        status += f"Hunger: {self.hunger}/100\n"
        status += f"Energy: {self.energy}/100\n"
        status += f"Happiness: {self.happiness}/100\n"
        status += f"Health: {'Sick' if self.is_sick else 'Healthy'}"
        return status

def main():
    print("Welcome to the Virtual Pet World!")
    pet_name = input("Please name your pet: ")
    pet = Pet(pet_name)
    print(f"Hello, {pet.name}! Let's start taking care of it!")

    while True:
        print("\n=== Action Menu ===")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Heal")
        print("5. Check Status")
        print("6. Exit")
        choice = input("Please select an action (enter 1-6): ")

        if choice == "1":
            print("\nAvailable Foods:")
            for i, food in enumerate(pet.foods.keys(), 1):
                print(f"{i}. {food}")
            food_choice = input("Please select a food: ")
            if food_choice.isdigit() and 1 <= int(food_choice) <= len(pet.foods):
                food_choice = list(pet.foods.keys())[int(food_choice) - 1]
                print(pet.feed(food_choice))
            else:
                print("Invalid choice. Please try again!")

        elif choice == "2":
            print("\nAvailable Games:")
            for i, game in enumerate(pet.games.keys(), 1):
                print(f"{i}. {game}")
            game_choice = input("Please select a game: ")
            if game_choice.isdigit() and 1 <= int(game_choice) <= len(pet.games):
                game_choice = list(pet.games.keys())[int(game_choice) - 1]
                print(pet.play(game_choice))
            else:
                print("Invalid choice. Please try again!")

        elif choice == "3":
            print(pet.sleep())

        elif choice == "4":
            print(pet.heal())

        elif choice == "5":
            print(pet.check_status())

        elif choice == "6":
            print(f"Goodbye! {pet.name} will miss you!")
            break

        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()    