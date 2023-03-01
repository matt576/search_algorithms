class Queue:
    """
    This class defines a queue fringe
    """

    def __init__(self):
        self.list = []

    def enqueue(self, state):
        """
        adds a state to the queue
        :param state: state to add to the queue
        :return: void
        """
        self.list.append(state)

    def dequeue(self):
        """
        removes the first state from the queue and returns this state (FIFO principle)
        :return: state
        """
        state = self.list.pop(0)
        return state

    def get_number_of_entries(self):
        """
        returns the number of states in the queue
        :return: int number length of queue
        """
        return len(self.list)


class Stack:
    """
    This class defines a stack fringe
    """

    def __init__(self):
        self.list = []

    def pop(self):
        """
        removes the first element of the stack and returns it (LIFO principle)
        :return: state
        """
        state = self.list.pop()
        return state

    def push(self, state):
        """
        adds a state to the stack
        :param state: state to add to the stack
        :return: void
        """
        self.list.append(state)

    def get_number_of_entries(self):
        """
        returns the number of states in the stack
        :return: int number length of stack
        """
        return len(self.list)


class Priority_Queue:
    """
    This class defines a priority queue fringe
    """

    def __init__(self):
        self.dict = {}

    def insert(self, state, cost, graph, parent=None):
        """
        insert a new state to the priority queue
        :param state: state to add to the priority queue
        :param cost: the cost to reach this state from its previous state
        :param graph: the graph stores the path costs to each node
        :param parent: the parent node of the state, if None, the state is the start state
        :return: void
        """
        if parent is None:
            self.dict[state] = cost
        else:
            self.dict[state] = graph.get_actual_cost(parent) + cost

    def pop(self):
        """
        deletes the state with the lowest cost in the priority queue and returns this state
        :return: state
        """
        state = min(self.dict, key=self.dict.get)
        del self.dict[state]
        return state

    def contains(self, state):
        """
        checks if state is already in the priority queue
        :param state: state to check
        :return: boolean indicating if state is in priority queue or not
        """
        return state in self.dict.keys()

    def get_actual_cost(self, state):
        """
        returns the actual path cost of a state in the priority queue
        :param state: state to find actual costs for
        :return: path costs to reach this state with the actual solution
        """
        if not self.contains(state):
            raise Exception("The state does not exist in the priority queue")
        return self.dict[state]

    def get_number_of_entries(self):
        """
        get the number of states in the priority queue
        :return: (int) length of dict
        """
        return len(self.dict.keys())


class ClosedList:
    """
    The closed list keeps all the states that already have been expanded. The closed list only exists in the
    Graph Search algorithms but not in the Search Tree algorithms
    """

    def __init__(self):
        self.list = []

    def contains(self, state):
        """
        checks if the state already has been expanded
        :param state: state to check
        :return: boolean indicating if state already has been expanded or not
        """
        return state in self.list

    def add(self, state):
        """
        adds expanded state to closed list
        :param state: state to add to list
        :return: void
        """
        self.list.append(state)


class Graph:
    """
    The Graph keeps track of the actual graph, the actual solution and path costs to every node on the shortest path
    """

    def __init__(self, environment):
        self.start_state = environment.start_state
        self.dict = {self.start_state: {"parent": None, "cost": 0}}

    def add(self, child, parent, cost=0):
        """
        Add a child to the graph structure. If the child state does already exist in the graph structure, costs
        have to be updated
        :param child: state to add to graph
        :param parent: state that was explored to find the child state
        :param cost: the cost from the parent state to the child state
        :return: void
        """
        if child not in self.dict.keys():
            self.dict[child] = {
                "parent": parent,
                "cost": self.get_actual_cost(parent) + cost,
            }
        else:
            if self.get_actual_cost(child) > self.get_actual_cost(parent) + cost:
                self.dict[child] = {
                    "parent": parent,
                    "cost": self.get_actual_cost(parent) + cost,
                }

    def get_actual_cost(self, state):
        """
        returns the actual costs to reach a state on the so far known shortest path
        :param state: state
        :return: path costs
        """
        return self.dict[state]["cost"]

    def get_actual_solution(self, state):
        """
        returns the solution of the algorithm. The solution is a sequence of actions to apply in order to find a
        goal state
        :param state: goal state that was reached
        :return: list of actions
        """
        solution = [state]
        no_root = True
        while no_root:
            parent = self.dict[state]["parent"]
            state = parent
            if state is self.start_state:
                no_root = False
            solution.append(state)
        solution.reverse()
        return solution
