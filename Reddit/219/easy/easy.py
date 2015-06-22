import fileinput

todo = []

for line in fileinput.input():
    first_param = line.find('(')
    last_param = line.find(')')
    if first_param == 0:
        raise SystemExit("Invalid input: use function(parameter)")
    command = line[:first_param]
    parameter = line[first_param+1:last_param]
    
    if (command == "addItem"):
        todo.append(parameter)
    elif (command == "deleteItem"):
        if parameter in todo:
            todo.remove(parameter)
        else:
            raise SystemExit("Invalid input: item not in list for delete")
    elif (command == "viewList"):
        for i in range(len(todo)):
            print("%d.\t%s\n" % (i+1, todo[i][1:-1])),
