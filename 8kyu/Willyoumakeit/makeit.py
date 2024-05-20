#!/usr/bin/env python3

#First take in 3 variables then make sure they are all intigers or floats, then make sure distance is shorter than average mpg * gallons left

def make_it(avrmpg, gal, distance):
    print(avrmpg, gal, distance)
    if isinstance(avrmpg, (int, float)):
        if isinstance(gal, (int, float)):
            if isinstance(distance,(int, float)):
                if (avrmpg * gal) >= distance:
                    return True
                else:
                    return False
            else:
                return "Enter distance as a number."
        else:
            return "Enter gallons as a number"
    else:
        return "Enter mpg as a number"
    



