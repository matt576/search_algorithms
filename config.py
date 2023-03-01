import argparse

parser = argparse.ArgumentParser(description="read input parameters")

parser.add_argument(
    "--search_algorithm",
    type=str,
    help="specifies the search algorithm",
    choices=["BFS", "DFS", "UCS"],
    default="DFS",
)
