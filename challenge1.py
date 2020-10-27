#!/usr/bin/env python3
import os

dogs = [" mudge is age:4 and bingo is age 12"]
fish = ["nemo is age 2" ]

pets = [{"type": "dog", "name": "mudge", "age": 4}, 
        {"type": "fish", "name": "dorothy", "age": "3 days"},
        {"type": "dog", "name": "bingo", "age": 12},
        {"type": "fish", "name": "nemo", "age": 2},
        {"type": "cat", "name": "fluffy", "age": 1}
        ]

for item in pets:
    if item["type"] == "dog":
        print(dogs)
    elif item["type"] == "fish":
        print(fish)
else:
    print("Not my pet")



