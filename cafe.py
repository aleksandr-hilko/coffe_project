from menu import Menu
from db.db_helper import CafeDB
from pricing_service import PricingService


class Cafe:
    def __init__(self):
        self.cafe_db = CafeDB("db_coffee_for_me.db")
        self.menu = Menu(self.cafe_db)
        self.pricing_service = PricingService(self.cafe_db)

    def get_salesman_list(self):
        return self.cafe_db.all_salesmans()
