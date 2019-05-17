from db.connection import DBConnection


class CafeDB(DBConnection):

    def all_salesmans(self):
        return self.select_as_list("SELECT name FROM salesman")

    # def all_coffee(self):
    #     coffee = self.select("SELECT name FROM coffee")
    #     return list(map(",".join, coffee))

    def all_coffee_with_price(self):
        all_coffee_price = self.select("SELECT coffee.name, CAST(coffee.price AS TEXT), currency.name\
                                    FROM coffee\
                                    JOIN currency ON coffee.currency_id=currency.id")
        return list(map(" ".join, all_coffee_price))

    def all_additional_ingredients(self):
        additional_ingredients = self.select("SELECT name FROM ingredients")
        return list(map(",".join, additional_ingredients))

    def get_element_from_total_table_for_salesman(self, column_name, name):
        """
        Try to get result by using salesman name and name of necessary column
        :param column_name: 'total' or 'number_of_sales'
        :param name:
        :return:
        """
        id_by_name = self._get_id_by_name(name)
        return self.select_one(f"SELECT {column_name}\
                                FROM summary\
                                WHERE id={id_by_name}")

    def _get_id_by_name(self, name):
        return self.select_one(f"SELECT seller_name_id\
                                FROM salesman\
                                JOIN summary ON salesman.id=summary.seller_name_id\
                                WHERE name='{name}'")

    def update_data_in_summary_table(self, column_name, name, new_value):
        id_by_name = self._get_id_by_name(name)
        return self.execute_and_commit(f"UPDATE summary\
                                        SET '{column_name}'={new_value}\
                                        WHERE id={id_by_name}")
