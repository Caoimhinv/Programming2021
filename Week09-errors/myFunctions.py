import logging

logging.basicConfig(level=logging.DEBUG)

def factorial(num):
    if num < 0:
        logging.warning("factorial received a number less than 0")
        return -1
    if num == 0:
        return 1
    factorial = 1
    num += 1
    for i in range(1,num):
        logging.debug("before mult %d by %d", factorial, i)
        factorial *= i
        logging.debug("after mult %d", factorial)

    return factorial

if __name__ == "__main__":
    print ("in My Functions ", __name__)
    assert factorial(7) == 5040