# https://www.geeksforgeeks.org/minimum-cost-path-left-right-bottom-moves-allowed/

from typing import List

def dfs(n: int, adj_list: List):
    pass

if __name__ == "__main__":
    a = [4]
    e = [{0:[1,2], 1:[2], 2:[0,3], 3:[3]}]

    for a_, e_ in zip(a, e):
        print(dfs(a_, e_))