'''

'''
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iter(iterator)
        self._follow = iter(iterator)
        try:
            self._peek = self._follow.__next__()
        except StopIteration:
            self._peek = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._peek

    def next(self):
        """
        :rtype: int
        """
        try:
            self._peek = next(self._follow)
        except StopIteration:
            self._peek = None
        return self._iterator.__next__()

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self._peek else False

mt = [1,2,3,]
a = PeekingIterator(mt)
print(type(a))
print(a.peek())
print(a.hasNext())
print(a.next())
print(a.next())
print(a.peek())
print(a.next())
print(a.hasNext())
