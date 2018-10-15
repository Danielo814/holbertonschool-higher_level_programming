#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """
    my_list class
    """
    def print_sorted(self):
        """
        prints sorted list
        """
        print(sorted(self))
