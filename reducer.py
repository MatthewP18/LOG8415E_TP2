#!/usr/bin/env python
"""reducer.py"""

import sys

for line in sys.stdin:
    line = line.strip()

    # parse the input we got from mapper.py
    userid, friend_recommendation_string = line.split('\t')

    # convert userID (currently a string) to int
    try:
        userid = int(userid)
    except ValueError:
        continue

    # Apply some string parsing 
    friend_recommendation_string = friend_recommendation_string.replace("[", "")
    friend_recommendation_string = friend_recommendation_string.replace("]", "")
    friend_recommendation_string = friend_recommendation_string.replace("'", "")
    friend_recommendation_string = friend_recommendation_string.replace(" ", "")
    friend_recommendation_list = list(friend_recommendation_string.split(","))

    my_dict = {i:friend_recommendation_list.count(i) for i in friend_recommendation_list} # Calculate count of same userID and create a weighted dictionnary with that count
    sorted_list = [v[0] for v in sorted(my_dict.items(), key=lambda kv: (-kv[1], kv[0]))] # Sort the dictionnay in descending value and ascending keys to present the most likely friend recommendation first

    # Print the recommendation to the output according to the laboratory specifications
    sorted_list = sorted_list[0:10]
    sys.stdout.write(str(userid) + "\t")
    first_instance = True
    for friend in sorted_list:
        if first_instance == False:
            sys.stdout.write(",")
        sys.stdout.write(friend)
        first_instance = False
    sys.stdout.write("\n")
  