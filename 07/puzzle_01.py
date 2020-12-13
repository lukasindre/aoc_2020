import fileinput
import re

def contains(rule):
    rules = [r for r in data if rule in data[r]]
    return [rule, *[t for tr in traits for t in contains(tr)]]
