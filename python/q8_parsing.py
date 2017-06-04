# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import sys
import os
import csv


def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.

    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
        
    fb_list = []
    with open(filename,'r') as f:
        
        # Skip first line
        reader = csv.reader(f)
        next(reader)
        
        # Loop through all rows and append to fb_list
        for row in reader:
            fb_list.append(row)
            
        # Replace strings with integers
        for ix, val in enumerate(fb_list):
            fb_list[ix][1:] = list(map(lambda x: int(x),fb_list[ix][1:]))
        
        return fb_list
        

def get_index_with_min_abs_score_difference(goals):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    goals_diff = []
    
    for ix, val in enumerate(goals):
        goals_for = val[-3]
        goals_allowed = val[-2]
        goals_diff.append(abs(goals_for - goals_allowed))
        
    min_goals_diff_idx = goals_diff.index(min(goals_diff))
    
    return min_goals_diff_idx

    
def get_team(index_value, parsed_data):
    """Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    return parsed_data[index_value][0]

  

footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))
