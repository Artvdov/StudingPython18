# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 19:36:49 2018

@author: A DOVI
"""
"""
Contains one functions to generate samples for testing hypothesis about n-handshakes
"""

import itertools
import string
import secrets

MAXFRIENDS=4
persons=list()
friends=list()

def getPeople(maxPeople=MAXFRIENDS, maxPairs=MAXFRIENDS*2,density=3):
    persons=list(string.ascii_uppercase[:maxPeople])
    friends=list()
    combinats=itertools.combinations(persons,2)
    selectors=[int(secrets.randbelow(density)>0) for x in range(maxPairs)]
    z=itertools.compress(combinats,selectors)
    for i in range(maxPairs):
        try:
            friends.append(next(z))
        except StopIteration:
            break
    return  persons,friends       




    
