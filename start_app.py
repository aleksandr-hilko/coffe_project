from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from examples import custom_style_1

import click

from questions import coffee_questions

import constants as const
from cafe import Cafe
from roles import Salesman


@click.group()
def main():
    print("main")


@main.command()
@click.argument("name")
def salesman(name):
    salesman = Salesman(name)
    cafe = Cafe()
    pricing_service = cafe.pricing_service
    if name not in cafe.get_salesman_list():
        raise Exception(f"There is no {name} in list of salesmans")

    answers = prompt(questions=coffee_questions(cafe.menu), style=custom_style_1)#how to add some(2) latte?
    # pprint(answers)
    pricing_service.update_summary_table_by_name("total", name, answers)
    pricing_service.update_summary_table_by_name("number_of_sales", name, answers)

    if answers[const.BILL] == const.YES:
        pricing_service.show_price(answers, salesman)


@main.command()
@click.argument("name")
def manager(name):
    print("manager")
    return name


if __name__ == '__main__':
    main()
