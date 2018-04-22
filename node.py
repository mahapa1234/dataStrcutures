#encoding: utf-8

class Node(object):
    """ Response a singly linked node.
    """
    def __init__(self, data, next = None):
        """
        Instantiates a Node with default next of None.
        """
        self.data = data
        self.next = next

