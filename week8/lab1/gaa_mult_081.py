#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points
        self.total = (self.goals * 3) + self.points

    def __str__(self):
        return "{} goal(s) and {} point(s)".format(self.goals, self.points)

    def __eq__(self, other):
        return self.total == other.total

    def __gt__(self, other):
        return self.total > other.total

    def __lt__(self, other):
        return self.total < other.total

    def __ge__(self, other):
        return self.total >= other.total

    def __le__(self, other):
        return self.total <= other.total

    def __add__(self, other):
        return Score(self.goals + other.goals, self.points + other.points)

    def __sub__(self, other):
        return Score(self.goals - other.goals, self.points - other.points)

    def __iadd__(self, other):
        self.goals, self.points = self.goals + other.goals, self.points + other.points
        return self

    def __isub__(self, other):
        self.goals, self.points = self.goals - other.goals, self.points - other.points
        return self

    def __mul__(self, other):
        return Score(self.goals * other, self.points * other)

    def __rmul__(self, other):
        return Score(self.goals * other, self.points * other)

    def __imul__(self, other):
        self.goals, self.points = self.goals * other, self.points * other
        return self
