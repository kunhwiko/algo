# Floyd's Cycle Detection can be used to find a start of a cycle in a linked list/array
# time: O(n)   space: O(1)

# how does it work?
# pointer "fast" moves twice as fast as pointer "slow" (often called "hare" and "tortoise")
# once slow and fast converge (if at all), another pointer starts from the head 
# the new pointer and one of slow or fast will move at the same speed
# the point of converge will be the the start of the cycle 

# proof 
# a = distance from head to start of cycle
# b = distance from start of cycle to where slow,fast meet
# c = distance from where slow,fast meet to start of cycle
# fast moved = a + b + c + b, slow moved = a + b
# relation of fast and slow : a+b+c+b = 2 * (a+b) -> c = a

def detect(head):
    slow = fast = head 
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next 
        if slow == fast:
            break
		
    # if a cycle doesn't exist 
    if fast == None or fast.next == None:
        return None
    while head != fast:
        head = head.next
        fast = fast.next
    return head   