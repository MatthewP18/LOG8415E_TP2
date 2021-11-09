#!/usr/bin/env python
"""mapper.py"""

import sys

users_and_friends = {}
potential_friends = {}
mutual_friends = {}
lines = sys.stdin.readlines()
# Generate a friends list for each user in the records
for line in lines:
    tokens = line.split("\t") # The left part of the tab (tokens[0]) contains the user id and the right side (tokens[1]) contains his friends
    list_of_friends = []

    tokens[1] = tokens[1].replace("\n", "")
    
    if (tokens[1] == ""): # In the case in which the user had no friends, we had an empty list
        users_and_friends.update({tokens[0] : list_of_friends})
        continue
    list_of_friends = tokens[1].split(",")
    users_and_friends.update({tokens[0] : list_of_friends})

for userid in users_and_friends.keys():
    blacklisted_ids = [userid] # Add the user himself to the blacklist of ids that can not be a friend recommendation
    list_of_potential_friends = []
    for friend in users_and_friends.get(userid):
        blacklisted_ids.append(friend) # Add all the users current friend to the blacklist as well
    for friend in users_and_friends.get(userid):
        friends_of_friend = users_and_friends.get(friend) # Obtain all the friends of the users current friends
        for friend_of_friend in friends_of_friend:
            if(friend_of_friend not in blacklisted_ids): # If the friends of the users current friends are not in the blacklist, we add them to the list of potential friends
                list_of_potential_friends.append(friend_of_friend)
    print(userid+"\t"+ str(list_of_potential_friends)) # Create a mapper output with the list of potential friends and the user ID
