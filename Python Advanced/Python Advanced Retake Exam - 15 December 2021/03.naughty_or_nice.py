def naughty_or_nice_list(*args, **kwargs):
    santa_dict = {'Nice': [], 'Naughty': [], 'Not found': []}
    list_with_tuples = args[0]
    args = list(args)[1:]
    
    for arg in args:
        count = 0
        pair = ()
        num, type_ = arg.split('-')
        
        for t in list_with_tuples:
            if t[0] == int(num):
                count += 1
                pair = t
                name_kid = t[1]
                
        if count == 1:
            santa_dict[type_].append(name_kid)
            list_with_tuples.remove(pair)
            
    for name_, type_ in kwargs.items():
        count = 0
        pair = ()
        
        for t in list_with_tuples:
            if t[1] == name_:
                count += 1
                pair = t
                name_kid = t[1]
                
        if count == 1:
            santa_dict[type_].append(name_kid)
            list_with_tuples.remove(pair)
            
    if len(list_with_tuples) > 0:
        for info in list_with_tuples:
            santa_dict['Not found'].append(info[1])
            
    print_result = ''
    for k, v in santa_dict.items():
        if len(v) > 0:
            print_result += f'{k}: {", ".join(v)}\n'
            
    return print_result


