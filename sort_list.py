class sorter:
    def from_smallest_to_largest():
        list=[]
        for i in range(5):
            element = int(input())
            list.append(element)
        list.sort()
        print(list)
    def from_largest_to_smallest():
        list1=[]
        for i in range(5):
            element0=int(input())
            list1.append(element0)
        list1.sort()
        list1.sort(reverse=True)
        print(list1)
    from_smallest_to_largest()
    from_largest_to_smallest()
