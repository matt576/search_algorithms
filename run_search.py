import config
import environment
import util


class Agent():
    def __init__(self):
        self.env = environment.Environment()
        self.graph = util.Graph(self.env)

    #implementHere
    def depth_first_search(self):
        # TODO initialize a stack
        stack = util.Stack()
        # TODO get the start state of the environment and push it on the stack
        start_state = self.env.get_start_state()
        stack.push(start_state)
        # TODO initialize a ClosedList called closed_list
        closed_list = util.ClosedList()
        while stack.get_number_of_entries() > 0:
            # TODO get the first element of the stack
            s = stack.pop()
            print("Expand node {}".format(s))
            # TODO if the closed_list does not contain state s already
            if closed_list.contains(s) is False:
                # TODO add state s to the closed_list
                closed_list.add(s)
                # TODO for every child_tuple in the list of successors from s
                for child_tuple in self.env.get_successors(s):
                    # TODO extract the child, action, reward from the variable child_tuple
                    child, action, reward = child_tuple
                    # TODO add the child and parent node s to the graph
                    self.graph.add(child=child, parent=s)
                    # TODO if child node is goal node
                    if self.env.is_goal(child):
                        # TODO return actual solution from the graph with the actual child as input
                        return self.graph.get_actual_solution(child)
                    # TODO push the child on the stack
                    stack.push(child)
                    print("Add node {} to stack".format(child))

    # implementHere
    def breadth_first_search(self):
        # TODO implement breadth first search algorithm
        queue = util.Queue()
        start_state = self.env.get_start_state()
        queue.enqueue(start_state)
        closed_list = util.ClosedList()
        while queue.get_number_of_entries() > 0:
            s = queue.dequeue()
            print("Expand node {}".format(s))
            if closed_list.contains(s) is False:
                closed_list.add(s)
                for child_tuple in self.env.get_successors(s):
                    child, action, reward = child_tuple
                    self.graph.add(child=child, parent=s)
                    if self.env.is_goal(child):
                        return self.graph.get_actual_solution(child)
                    queue.enqueue(child)
                    print("Add node {} to queue".format(child))


    # implementHere
    def uniform_cost_search(self):
        # TODO implement uniform cost search algorithm
        queue = util.Priority_Queue()
        start_state = self.env.get_start_state()
        queue.insert(state=start_state, cost=0, graph=self.graph)
        closed_list = util.ClosedList()
        while queue.get_number_of_entries() > 0:
            s = queue.pop()
            print("Expand node {}".format(s))
            if self.env.is_goal(s):
                return self.graph.get_actual_solution(s)
            closed_list.add(s)
            for child_tuple in self.env.get_successors(s):
                child, action, cost = child_tuple
                self.graph.add(child=child, parent=s, cost=cost)
                if not queue.contains(child) and not closed_list.contains(child):
                    queue.insert(state=child, cost=cost, parent=s, graph=self.graph)
                    print("Add node {} to priority queue".format(child))
                elif queue.contains(child) and queue.get_actual_cost(child) > self.graph.get_actual_cost(s) + cost:
                    queue.insert(state=child, cost=cost, parent=s, graph=self.graph)
                    print("Replace node {} in priority queue".format(child))


    def run_search_algorithm(self, algorithm):
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
            raise Exception("Wrong algorithm determined")

        return solution


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    args = config.parser.parse_args()
    search_algorithm = args.search_algorithm
    agent = Agent()
    solution = agent.run_search_algorithm(search_algorithm)

    print("Your solution when using {} is the action sequence {}.".format(args.search_algorithm, solution))

