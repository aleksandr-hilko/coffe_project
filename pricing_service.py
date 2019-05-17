from pathlib import Path

import constants as const
from definitions import project_path_dir
from reporting import create_table
from roles import Salesman, Manager


class PricingService:
    def __init__(self, cafe_db):
        self.cafe_db = cafe_db

    def show_price(self, sale_ifo_dict, role):
        if isinstance(role, Salesman):
            self.cafe_db.create_and_print_bill(sale_ifo_dict)
        elif isinstance(role, Manager):
            raise NotImplementedError

    def create_and_print_bill(self, sale_info_dict):
        columns, rows = [], []
        total_price, quantity, currency_type = self._get_total_price_and_currency_type_for_coffee(
            sale_info_dict)

        for key in sale_info_dict:
            if key == const.BILL:
                continue
            if type(sale_info_dict.get(key)) is list:
                columns.append(key)
                rows.append(f"{', '.join(sale_info_dict[key])}")
            else:
                columns.append(key)
                rows.append(sale_info_dict[key])
        columns.append("Total")
        rows.append(f"{total_price} {currency_type}")
        res = create_table(rows, columns)
        print(res)
        self._save_last_order_in_file(res)
        #     # what about empty additional ingredients(in bill)

    @staticmethod
    def _save_last_order_in_file(table):
        path_to_bill = Path(project_path_dir, "bill.txt")
        with path_to_bill.open(mode="w") as f:
            f.write(table)

    @staticmethod
    def _get_total_price_and_currency_type_for_coffee(sale_info_dict):
        coffee_with_price = sale_info_dict[
            "coffee type"]  # what if dont have ingredients
        quantity = sale_info_dict["quantity"]
        split_coffee_with_price = coffee_with_price.split()
        price_for_coffee = int(split_coffee_with_price[1])
        currency_type = split_coffee_with_price[-1]
        total_value_for_coffee = price_for_coffee * quantity
        return total_value_for_coffee, quantity, currency_type  # think about summ of diff currency

    def get_el_from_summary_table_by_username(self, column_name, name):
        res = self.cafe_db.get_element_from_total_table_for_salesman(
            column_name, name)
        return 0 if not res else res

    def update_summary_table_by_name(self, column_name, name, sale_info_dict):
        curr_total, quantity, *rest = self._get_total_price_and_currency_type_for_coffee(
            sale_info_dict)
        if column_name == "total":
            new_total_value = self.get_el_from_summary_table_by_username(
                column_name, name) + curr_total
            self.cafe_db.update_data_in_summary_table(column_name, name,
                                                      new_total_value)
        elif column_name == "number_of_sales":
            new_number_of_sales_value = self.get_el_from_summary_table_by_username(
                column_name, name) + quantity
            self.cafe_db.update_data_in_summary_table(column_name, name,
                                                      new_number_of_sales_value)
