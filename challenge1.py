#!/usr/bin/env python3
import os

dogs = []
fish = []

pets = [{"type": "dog", "name": "mudge", "age": 4}, 
        {"type": "fish", "name": "dorothy", "age": "3 days"},
        {"type": "dog", "name": "bingo", "age": 12},
        {"type": "fish", "name": "nemo", "age": 2},
        {"type": "cat", "name": "fluffy", "age": 1}
        ]

for item in pets:
    if item["type"] == "dog":
        dogs.append(item["name"])
        print(f"{item['name']) is my pet dog")
#        print(dogs)
    elif item["type"] == "fish":
        print(fish)
else:
    print("Not my pet")



