from collections import deque


class State:
    def __init__(self, ml, cl, sl, mr, cr, sr):
        self.ml = ml
        self.cl = cl
        self.sl = sl
        self.mr = mr
        self.cr = cr
        self.sr = sr
        self.parent = None

    def goal_test(self):
        return self.mr == self.cr == 3 and self.ml == self.sl == 0

    def __str__(self):
        return ("On the {} side there are {} missionaries and {} cannibals.\n"
                "On the {} side there are {} missionaries and {} cannibals.\n").format(
            self.sr, self.mr, self.cr, self.sl, self.ml, self.cl)

    def __repr__(self):
        return f"({self.ml}, {self.cl}, {self.sl}, {self.mr}, {self.cr}, {self.sr})"


class Solver:
    def __init__(self):
        self.start_state = State(3, 3, True, 0, 0, False)
        self.end_state = State(0, 0, False, 3, 3, True)
        self.frontier = deque()
        self.frontier.append(self.start_state)
        self.visited = []
        self.solution = []

    def check_validity(self, state):
        return ((state.ml == 0 or state.ml >= state.cl) and
                (state.mr == 0 or state.mr >= state.cr) and
                not self.check_visit(state) and state.cl >= 0 and state.cr >= 0)

    def check_visit(self, state):
        for val in self.visited:
            if (val.mr == state.mr and val.sl == state.sl and val.cl == state.cl and val.cr == state.cr
                    and val.ml == state.ml):
                return True
        return False

    def get_next_states(self, cur_state):
        self.visited.append(cur_state)
        successors = []
        if cur_state.sl:
            for m, c in [(1, 1), (1, 0), (2, 0), (0, 1), (0, 2)]:
                state = State((cur_state.ml - m), (cur_state.cl - c), False,
                              (cur_state.mr + m), (cur_state.cr + c), True)

                if self.check_validity(state):
                    successors.append(state)
                    print(state)
        elif cur_state.sr:
            for m, c in [(1, 1), (1, 0), (2, 0), (0, 1), (0, 2)]:
                state = State((cur_state.ml + m), (cur_state.cl + c), True,
                              (cur_state.mr - m), (cur_state.cr - c), False)

                if self.check_validity(state):
                    successors.append(state)
                    print(state)

        return successors

    def solve(self):
        while self.frontier:
            current_state = self.frontier.popleft()
            if current_state.goal_test():
                temp = current_state
                while temp is not None:
                    self.solution.append(temp)
                    temp = temp.parent
                self.solution = self.solution[::-1]
                break

            successors = self.get_next_states(current_state)
            for successor in successors:
                successor.parent = current_state
                self.frontier.append(successor)


# def main():
#     solver = Solver()
#     solver.solve()
#     print(solver.solution)
#
#
# if __name__ == '__main__':
#     main()
