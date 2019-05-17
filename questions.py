# -*- coding: utf-8 -*-
"""
* Checkbox question example
* run example by typing `python example/checkbox.py` in your console
"""
from PyInquirer import Validator, ValidationError
import re
import constants as const


class NumberValidator(Validator):
    def validate(self, document):
        ok = re.match('^[1-9]$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a number(from 1 to 9)',
                cursor_position=len(document.text))  # Move cursor to end


def coffee_questions(menu):
    coffee_with_price_list = menu.get_all_coffee_with_price()
    additional_ingridients = menu.get_all_additional_ingredients()

    coffee_wit_price_list = list(map(lambda el: {"name": el}, coffee_with_price_list))
    additional_ingridients_list = list(map(lambda el: {"name": el}, additional_ingridients))
    my_coffee_questions = [
        {
            'type': 'list',
            'message': 'What coffee do you need',
            'name': 'coffee type',
            'choices': coffee_wit_price_list
            # 'validate': lambda answer: 'You must choose at least one topping.' if len(answer) == 0 else True
            # check empty answer
        },
        {
            'type': 'input',
            'name': 'quantity',
            'message': 'Count of servings do you need?',
            'validate': NumberValidator,
            # 'validate': lambda answer: 'You must choose at least one topping.' if len(answer) == 0 else True,
            'filter': lambda val: int(val)
        },
        {
            'type': 'checkbox',
            'message': 'Select additional ingredients',
            'name': 'additional ingredients',
            'choices': additional_ingridients_list,
            'filter': lambda val: "without any additions" if len(val) == 0 else val
        },
        {
            'type': 'list',
            'message': 'Do you need a bill',
            'name': 'bill',
            'choices': [const.YES, const.NO]
            # 'validate': lambda answer: 'You must choose at least one topping.' if len(answer) == 0 else True
            # check empty answer
        },
    ] #think about adding ingridients to each of coffee 2. add if no request
    return my_coffee_questions
