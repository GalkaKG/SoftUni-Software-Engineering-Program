def func_executor(*args):
    result = []
    for func_ref, func_params in args:
        func_result = func_ref(*func_params)
        result.append(f'{func_ref.__name__} - {func_result}')
    return '\n'.join(result)
