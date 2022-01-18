'''
	Your task is to return the data stored in
	the nth node from end of linked list.
	
	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    itr = head
    c = 0
    while itr:
        c += 1
        itr = itr.next
    c -= n
    if c < 0:
        return -1
    while c > 0:
        c -= 1
        head = head.next
    return head.data
