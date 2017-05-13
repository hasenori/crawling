#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv

with open('top_cities.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f,['rank','city','population'])
    writer.writeheader()
    writer.writerows([
        {'rank': 1, 'city': '上海', 'population': 2415000},
        {'rank': 2, 'city': 'カラ', 'population': 2414000},
        {'rank': 3, 'city': '北京', 'population': 2413000},
        {'rank': 4, 'city': '天津', 'population': 2412000}
    ])
