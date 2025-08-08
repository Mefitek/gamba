# Test by running pytest Test.py in cmd

import pytest
from Main import *

p = Pokie(CYLS, CYL_SLOTS)

def test_pokie_1():
    """
    ['🍉', '🍉', '🍉']
    ['🔔', '🍉', '🍇']
    ['🍊', '🍒', '🍉']
    """
    p.set_pokie([[6,6,6],
                 [5,6,2],
                 [3,0,6]])
    p.count_score()
    assert p.last_score == 40

def test_pokie_1():
    """
    ['🍇', '🍇', '🍇']
    ['🔔', '🧊', '🍇']
    ['🧊', '🔔', '🔔']
    """
    p.set_pokie([[2,2,2],
                 [5,8,2],
                 [8,5,5]])
    p.count_score()
    assert p.last_score == 45
