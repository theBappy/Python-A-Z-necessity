
def prefix_decorator(prefix):
    def decortor_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed Before', original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, 'Executed After', original_function.__name__, '\n')
            return result
        return wrapper_function
    return decortor_function

@prefix_decorator('LOG:')
def display_info(name, age):
    print('display_info ran with argumets ({} , {})'.format(name, age))

display_info('Maxwell', 24)
display_info('Travis', 22)