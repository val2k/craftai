import os
import time
from celery import Celery


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.factors')
def factors(n: int) -> list:

    # Returns true if n is a prime number
    def check_prime(n):
        x = 2
        while(x < n):
            if n % x == 0:
                # Factor other then 1 or n, number is composite
                return False
            x = x +1
        # Number is prime, while loop terminated without finding factor
        return True
    
    # Finds the next prime after n
    def next_prime(n):
        val = n + 1
        while(True):
            # Check if val (n + 1) is a prime
            if check_prime(val):
                return val
            else:
                val = val + 1
    
    factor_list = []
    prime = 1
    next_p = next_prime(prime)

    while (next_p <= n):
        while n % next_p == 0:
            n = n / next_p
            factor_list.append(next_p)
        prime = next_p
        next_p = next_prime(prime)

    return factor_list

