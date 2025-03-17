import time
import math

def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    
    primes = []
    for i in range(2, limit + 1):
        if sieve[i]:
            primes.append(i)
    return primes

def every_1000th_prime():
    # 10000番目の素数は約104729なので、余裕を持って120000まで計算
    primes = sieve_of_eratosthenes(120000)
    return [primes[i] for i in range(999, 10000, 1000)]

if __name__ == "__main__":
    start_time = time.time()
    primes = every_1000th_prime()
    for prime in primes:
        print(prime)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.10f} seconds")