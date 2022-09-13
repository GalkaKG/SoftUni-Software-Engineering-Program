def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key, value in kwargs.items():
        text = text.replace(key, value)

    return text
