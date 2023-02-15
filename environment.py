
class Environment():
    def __init__(self):
        self.num_rows_y = 3
        self.num_cols_x = 4
        self.win_state = [(3, 2)]
        self.lose_state = [(3, 1)]
        self.start_state = (0, 0)
        self.list_of_blocked_states = [(1,1)]

    def get_start_state(self):
        """
        :return: start state of the environment
        """
        return self.start_state

    def get_successors(self, state):
        """
        transition function
        :param state:  state in the environment
        :return: a list of (next_state, action, reward) tuples that define the transition possibilities from state to next_state
        """
        x, y = state
        successors = []
        for action in ["up", "down", "left", "right"]:
            if action == "up":
                next_state = (x, y+1)
            elif action == "down":
                next_state = (x, y-1)
            elif action == "left":
                next_state = (x-1, y)
            elif action == "right":
                next_state = (x+1, y)

            if next_state[0] > self.num_cols_x - 1 or \
                    next_state[0] < 0 or \
                    next_state[1] > self.num_rows_y - 1 or \
                    next_state[1] < 0 or \
                    next_state in self.list_of_blocked_states:
                continue

            successors.append((next_state, action, 1))

        return successors

    def get_reward(self, state):
        """
        returns the reward of a state
        :param state: actual state in environment
        :return: reward that the agents receives for being in this state
        """
        if state == self.win_state:
            return 1
        if state == self.lose_state:
            return -1
        else:
            return 0

    def is_goal(self, state):
        """
        determines if the state is a goal state
        :param state: actual state in environment
        :return: boolean indicating True or False
        """
        return state in self.win_state