import unittest
from stack import ArrayStack

class TestArrayStack(unittest.TestCase):

    def test_init(self):
        stack = ArrayStack() 
        self.assertEqual(stack.isEmpty(), True, "Should be empty on init")
    
    def test_push(self):
        stack = ArrayStack()
        for num in range(5):
            stack.push(num)
            self.assertEqual(stack.isEmpty(), False, "Should be not be empty after push")

    def test_peek(self):
        stack = ArrayStack()
        self.assertEqual(stack.peek(), None, "No peeking before pushing")
        for num in range(5):
            stack.push(num)
            peekNum = stack.peek()
            self.assertEqual(num, peekNum, "Peek item should be last pushed")

    def test_pop(self):
        stack = ArrayStack()
        self.assertEqual(stack.peek(), None, "No peeking before pushing")
        for num in range(5):
            stack.push(num)
            poppedNum = stack.pop()
            self.assertEqual(num, poppedNum, "Peek item should be last pushed")
            self.assertEqual(stack.isEmpty(), True, "Should be empty after popping all items")

    def test_isEmpty(self):
        stack = ArrayStack()
        self.assertEqual(stack.isEmpty(), True, "Should be empty on init")
        

if __name__ == '__main__':
    unittest.main()