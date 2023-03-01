import config
import environment
import util


class Agent:
    def __init__(self):
        self.env = environment.Environment()
        self.graph = util.Graph(self.env)

    def depth_first_search(self):  # depth first search
        stack = util.Stack()  # initialize a stack

        start_state = (
            self.env.get_start_state()
        )  # get the start state of the environment
        stack.push(start_state)  # add the start state to the stack

        closed_list = util.ClosedList()  # initialize a closed list
        while stack.get_number_of_entries() > 0:
            s = stack.pop()  # get the first element of the stack
            print("Expand node {}".format(s))

            if (
                closed_list.contains(s) is False
            ):  # if the node is not in the closed list
                closed_list.add(s)  # add the node to the closed list

                for child_tuple in self.env.get_successors(
                    s
                ):  # get the successors of the node
                    (
                        child,
                        action,
                        reward,
                    ) = child_tuple  # get the child node, action and reward

                    self.graph.add(
                        child=child, parent=s
                    )  # add the child node to the graph

                    if self.env.is_goal(child):  # if the child node is the goal node
                        return self.graph.get_actual_solution(
                            child
                        )  # return the solution

                    stack.push(child)  # add the child node to the stack
                    print("Add node {} to stack".format(child))

    def breadth_first_search(self):  # breadth first search
        queue = util.Queue()  # initialize a queue
        start_state = (
            self.env.get_start_state()
        )  # get the start state of the environment
        queue.enqueue(start_state)  # add the start state to the queue
        closed_list = util.ClosedList()  # initialize a closed list
        while queue.get_number_of_entries() > 0:  # while the queue is not empty
            s = queue.dequeue()  # get the first element of the queue
            print("Expand node {}".format(s))  # print the node
            if (
                closed_list.contains(s) is False
            ):  # if the node is not in the closed list
                closed_list.add(s)  # add the node to the closed list
                for child_tuple in self.env.get_successors(
                    s
                ):  # get the successors of the node
                    (
                        child,
                        action,
                        reward,
                    ) = child_tuple  # get the child node, action and reward
                    self.graph.add(
                        child=child, parent=s
                    )  # add the child node to the graph
                    if self.env.is_goal(child):  # if the child node is the goal node
                        return self.graph.get_actual_solution(
                            child
                        )  # return the solution
                    queue.enqueue(child)  # add the child node to the queue
                    print("Add node {} to queue".format(child))  # print the node

    def uniform_cost_search(self):  # uniform cost search
        queue = util.Priority_Queue()  # initialize a priority queue
        start_state = (
            self.env.get_start_state()
        )  # get the start state of the environment
        queue.insert(
            state=start_state, cost=0, graph=self.graph
        )  # add the start state to the queue
        closed_list = util.ClosedList()  # initialize a closed list
        while queue.get_number_of_entries() > 0:  # while the queue is not empty
            s = queue.pop()  # get the first element of the queue
            print("Expand node {}".format(s))  # print the node
            if self.env.is_goal(s):  # if the node is the goal node
                return self.graph.get_actual_solution(s)  # return the solution
            closed_list.add(s)  # add the node to the closed list
            for child_tuple in self.env.get_successors(
                s
            ):  # get the successors of the node
                child, action, cost = child_tuple  # get the child node, action and cost
                self.graph.add(
                    child=child, parent=s, cost=cost
                )  # add the child node to the graph
                if not queue.contains(child) and not closed_list.contains(
                    child
                ):  # if the child node is not in the queue and not in the closed list
                    queue.insert(
                        state=child, cost=cost, parent=s, graph=self.graph
                    )  # add the child node to the queue
                    print(
                        "Add node {} to priority queue".format(child)
                    )  # print the node
                elif (
                    queue.contains(child)  # if the child node is in the queue
                    and queue.get_actual_cost(child)
                    > self.graph.get_actual_cost(s)
                    + cost  # and the actual cost of the child node is greater than the actual cost of the parent node + the cost of the action
                ):
                    queue.insert(
                        state=child, cost=cost, parent=s, graph=self.graph
                    )  # add the child node to the queue
                    print(
                        "Replace node {} in priority queue".format(child)
                    )  # print the node

    def run_search_algorithm(self, algorithm):  # run the search algorithm
        """
        Function calls the correct algorithm depending on the command args
        """
        if algorithm == "BFS":
            solution = self.breadth_first_search()
        elif algorithm == "DFS":
            solution = self.depth_first_search()
        elif algorithm == "UCS":
            solution = self.uniform_cost_search()
        else:
            raise Exception("Please choose a valid algorithm")

        return solution


if __name__ == "__main__":
    args = config.parser.parse_args()
    search_algorithm = args.search_algorithm
    agent = Agent()
    solution = agent.run_search_algorithm(search_algorithm)

    print(
        "Your solution when using {} algorithm has the node sequence {}.".format(
            args.search_algorithm, solution
        )
    )
