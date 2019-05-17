class Menu:
    def __init__(self, cafe_db):
        self.cafe_db = cafe_db

    def get_all_coffee_with_price(self):
        return self.cafe_db.all_coffee_with_price()

    def get_all_additional_ingredients(self):
        return self.cafe_db.all_additional_ingredients()
