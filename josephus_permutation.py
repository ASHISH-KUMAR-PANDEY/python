def who_goes_free(total, execute):
    list = []
    for i in range(total):
        list.append(i)
    execute_counter = -1 + execute
    while len(list) > 1:
        item = list[(execute_counter) % len(list)]
        index_current = (execute_counter) % len(list)
        list.pop(index_current)
        execute_counter += execute - 1
        execute_counter = execute_counter % len(list)
    return list[0]
