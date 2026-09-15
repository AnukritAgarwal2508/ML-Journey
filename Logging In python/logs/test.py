from logger import logging

def add(a , b):

    logging.debug("The addition operartion is taking place")
    return a + b


logging.debug("The addition operartion is called")
add(10 , 15)
