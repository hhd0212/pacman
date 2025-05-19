# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()
        
        
def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    start_state = problem.getStartState()

    S = Stack()
    visited = set()

    S.push((start_state, []))

    while not S.isEmpty():
        state, path = S.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)

            for next_state, action, _ in problem.getSuccessors(state):
                if next_state not in visited:
                    S.push((next_state, path + [action]))

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue

    Q = Queue()
    Q.push((problem.getStartState(), []))  # (state, path)
    visited = set()

    while not Q.isEmpty():
        state, path = Q.pop()

        if problem.isGoalState(state):
            return path

        if state not in visited:
            visited.add(state)

            for next_state, action, _ in problem.getSuccessors(state):
                if next_state not in visited:
                    Q.push((next_state, path + [action]))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    PQ = PriorityQueue()                       
    PQ.push((problem.getStartState(), [], 0), 0)
    visited = {}                                   

    while not PQ.isEmpty():
        state, path, cost = PQ.pop()

        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost

        if problem.isGoalState(state):
            return path

        for next_state, action, step in problem.getSuccessors(state):
            new_cost = cost + step
            
            if next_state not in visited or new_cost < visited[next_state]:
                PQ.push((next_state, path + [action], new_cost), new_cost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    
    PQ = PriorityQueue()
    start = problem.getStartState()
    startH = heuristic(start, problem)
    PQ.push((start, [], 0), startH)
    best = {}

    while not PQ.isEmpty():
        state, path, g = PQ.pop()
        
        if state in best and best[state] <= g:
            continue
        best[state] = g

        if problem.isGoalState(state):
            return path
        
        for next_state, action, step in problem.getSuccessors(state):
            newG = g + step

            if next_state not in best or newG < best[next_state]:
                f = newG + heuristic(next_state, problem)
                PQ.push((next_state, path + [action], newG), f)
    return []


# Abbreviations
dfs = depthFirstSearch
bfs = breadthFirstSearch
ucs = uniformCostSearch
astar = aStarSearch