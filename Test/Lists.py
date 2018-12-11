create_list = []
inp = ""

while True:
    inp = input("Please enter an element to add to the list [fin = finished]")
    create_list.append(inp)
    l = len(create_list)
    if inp == "fin":
        create_list.remove('fin')
        print ("The list contains " + str(l-1) + " elements, here they are: ")

        for a in create_list:
            print (create_list.index(a)+1, ":", str(a))
        break