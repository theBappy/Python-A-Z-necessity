import logging

logging.basicConfig(filename='test.log' ,level= logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y

num_1 = 50
num_2 = 10

add_result = add(num_1, num_1)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result)) 

sub_result = substract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result)) 

multiply_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, multiply_result))

div_result =divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result)) 