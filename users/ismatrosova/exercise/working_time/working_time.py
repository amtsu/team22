def out_priority_task (list_task):
    #list_task = {"a":"breakfast", "b":"lunch", "c":"dinner"}
    list_priority=["a","b","c","d","e","f","g","h","i","j" "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for priority in list_priority:    # priority = a b c d e ...
        if list_task.get(priority):
            return list_task[priority]
    return None