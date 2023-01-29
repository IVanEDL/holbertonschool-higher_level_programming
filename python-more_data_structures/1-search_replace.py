#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda beta: replace if beta == search else beta, my_list))
