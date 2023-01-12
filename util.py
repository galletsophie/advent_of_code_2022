import requests
import os
import pandas as pd

aoc_cookie = os.environ.get('aoc_cookie')


def prep_input(input_txt: str):
    with open(input_txt, 'r') as f:
        lines = f.readlines()
        input = [line.strip() for line in lines]
    return input



