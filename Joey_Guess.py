# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:19:36 2021

@author: John Beraducci
"""
import numpy as np

def Run_type2(answer):
    score = 0
    current_guess = 0
    while current_guess != answer:
        score += 1
        current_guess = int(input("Pick a number between 1 and 100: "))
        if current_guess < answer:
            print("Too Low")
        if current_guess>answer:
            print("Too High")
    print("You did it!  The answer was " + str(answer) + ". It took you " + str(score) + " tries.")

def Run_type1(answer):
    score = 0
    current_guess = 0
    current_distance = 0
    while current_guess != answer:
        score += 1
        last_distance = current_distance
        current_guess = int(input("Pick a number between 1 and 100: "))
        current_distance = abs(current_guess - answer)
        if current_distance == 0:
            print("You Got it!!!")
        if (score > 1) and (current_distance < last_distance) and (current_distance !=0):
            print("Getting hotter")
        if (score > 1) and (current_distance > last_distance):
            print("Getting colder")
        if current_distance == 1:
            print("You are standing on the Sun its so hot!!!")
        if current_distance == 2:
            print("You are so hot you are standing in lava!!!")
        if 3 <= current_distance <= 5:
            print("You are burning up!!!")
        if 6 <= current_distance <= 10:
            print("You are pretty Hot right now...")
        if current_distance > 80:
            print("You are the coldest person on Earth, standing at the North Pole")
        if 60 < current_distance <= 80:
            print("You are so cold you must be in Antarctica")
        if 50 < current_distance <= 60:
            print("You are so cold your teeth are chattering!")
        if 40 <= current_distance <= 50:
            print("Its pretty cold around this number")
        if (score == 1) and (10 < current_distance < 40):
            print("Thats a decent start, you are a little warm")        
    print("The answer was " + str(answer) + ". It took you " + str(score) + " tries.")

######### Start Program here #############
play_again = 1
name = input("Enter your name: ")

print("Hello " + name +".") 

while play_again == 1:
    game_type = int(input("What type of game do you want to play?  Enter '1' for Hot / Cold;   Enter '2' for High / Low: "))
    
    answer = round(np.random.rand()*100)
    
    if game_type == 1:
        Run_type1(answer)
    
    if game_type == 2:
        Run_type2(answer)
    
    play_again = int(input("Would you like to play again? 1 for Yes, 0 for No: "))
    
print("Thanks for playing " + name + ". Come back soon!")
    

