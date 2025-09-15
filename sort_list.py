class sorter:
    def sort(list,sort):
            if sort == "1":
                sorted_list = sorted(list)
                print(sorted_list)
            elif sort == "2":
                sorted_list = sorted(list, reverse=True)
                print(sorted_list)
            else:
                print("incorrecn input")
    sort([5,7,3,8,0], str(input("choose number(1,2)  ")))
