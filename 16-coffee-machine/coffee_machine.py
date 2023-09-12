from constant import COFFEE_DETAILS

class Coffee_Machine:
    def __init__(self, ingredients : object, coffee_details: []):
        self.currentIngredients = ingredients
        self.coffee_details = coffee_details

    def check_enough_ingredient(self, coffee_details):
        for key in coffee_details:
            if self.currentIngredients.get(key) < coffee_details.get(key):
                return False
        
        return True

    def make_coffee(self, coffee_type):
        coffee_details = COFFEE_DETAILS.get(coffee_type)
        enough_ingredients = self.check_enough_ingredient(coffee_details)

        if (not enough_ingredients):
            return 'Sorry. We run out of ingredient :(('
        
        for key in coffee_details:
            self.currentIngredients[key] -= coffee_details[key]
        
        return f'here is your {coffee_type}'
        
    def print_report(self):
        for key in self.currentIngredients:
            print(f'{key} => {self.currentIngredients[key]}')