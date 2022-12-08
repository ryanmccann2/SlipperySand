#!/usr/bin/env python3
# traceTM_SlipperySand.py

import csv

class TuringMachine:
    def __init__(self):
        self.name = ""
        self.states = []
        self.sigma = []
        self.gamma = []
        self.start = ""
        self.accept = ""
        self.reject = ""
        self.transitions = {}

    def getMachine(self, __file):
        # get machine info from csv file
        with open(__file, "r") as f:
            r = list(csv.reader(f, delimiter=','))
            self.name = r[0][0]
            self.states = [state for state in r[1] if state]
            self.sigma = [c for c in r[2] if c]
            self.gamma = [c for c in r[3] if c]
            self.start = r[4][0]
            self.accept = r[5][0]
            self.reject = r[6][0]

            self.transitions = {x:{} for x in self.states}
            for t in r[7:]:
                if t[1] in self.transitions[t[0]]:
                    self.transitions[t[0]][t[1]].append((t[2], t[3], t[4]))
                else:
                    self.transitions[t[0]][t[1]] = [(t[2], t[3], t[4])]
    
    def printMachine(self):
        # function to print machine metadata
        print(f'Name ---> {self.name}')
        print(f'States ---> {self.states}')
        print(f'Sigma ---> {self.sigma}')
        print(f'Gamma ---> {self.gamma}')
        print(f'Start State ---> {self.start}')
        print(f'Accept ---> {self.accept}')
        print(f'Reject ---> {self.reject}')
        print("Transitions:")
        for state, char in self.transitions.items():
            print(f'{state}:')
            for key in char:
                print(key, ':', char[key])


    def trace(self, string, step_limit):
        Q = []
        Q.append((self.start, 0, "q1", string, None, [self.start + string]))
        k = 0
        max_step = 0
        while Q:

            # step limit flag stop program execution
            k += 1
            if k > step_limit:
                return -1, None, max_step
            print(f'{k}. Q = {Q}')
            # pop tuple from bottom of list
            last = Q.pop(0)
            # tuple(current state, string, index of string, state_history, tape)
            curr_state = last[0]
            index = last[1]
            s = last[3]
            if index < len(string) and index >= 0:
                input_char = s[index]
            else:
                input_char = "_"
            history = last[2]
            max_step = max(len(history.split(",")), max_step)
            configurations = last[5]
            

            # if the current state is in reject, continue
            if curr_state == self.reject:
                continue

            # if in accept state, return the history
            if curr_state == self.accept:
                configurations.append(s[:index]+curr_state+s[index:])
                return history, configurations, max_step
            
            else:
                # find all next poss transitions and add to queue
                if input_char in self.transitions[curr_state]:
                    for tup in self.transitions[curr_state][input_char]:
                        if tup[1]:
                            s = s[:index] + tup[1] + s[index+1:]
                        else:
                            s = s[:index] + input_char + s[index+1:]
                        
                        if tup[2] == 'L':
                            configurations.append(s[:index]+curr_state+s[index:])
                            Q.append((tup[0], index - 1, history + ',' + tup[0], s, self.transitions[curr_state][input_char], configurations))
                        # if tup[2] == 'L':
                        else:
                            configurations.append(s[:index]+curr_state+s[index:])
                            Q.append((tup[0], index + 1, history + ',' + tup[0], s, self.transitions[curr_state][input_char], configurations))
        return None, None, max_step
