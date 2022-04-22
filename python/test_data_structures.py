#   test_data_structures.py
#   jake farabee 04/22/2022
import pytest
import data_structures

def test_stack():
	tester = algorithms.Stack()
	assert tester.created == True
	assert tester.push(1) == 1
	assert tester.pop() == 1
	tester.push(1), tester.push(2), tester.push(3)
	assert tester.pop(3) == [3, 2, 1]
	tester.push(1)
	with pytest.raises(ValueError):		# can't pop <1
		tester.pop(0)
	with pytest.raises(ValueError):		# can't pop >height
		tester.pop(2)
	assert tester.empty_stack() == True
	with pytest.raises(RuntimeError):	# can't pop empty stack
		tester.pop()

def test_queue():
	tester = algorithms.Queue()
	assert tester.created == True
	assert tester.enqueue(1) == 1
	assert tester.dequeue() == 1
	with pytest.raises(RuntimeError):
		tester.dequeue()				# can't dequeue empty queue