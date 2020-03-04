#the cache hashtable.
import timeit
cache = {}
def fibonacci(n):
    #if we already have precalculated it.
    if n in cache:
        #return the value at the index.
        return cache[n]
    else:
        #otherwise set it to n if 
        # n < 2 otherwise do recursion till we get there and add this value to the cache.
        cache[n] = n if n < 2 else fibonacci(n-2) + fibonacci(n-1)
        #finally we return the value of cache[n]
        return cache[n]
        

#With a JIT this version is way faster.
cache = {}
def fib_jit(n):
    #if we already have precalculated it.
    if n in cache:
        #return the value at the index.
        return cache[n]
    else:
        #otherwise set it to n if 
        # n < 2 otherwise do recursion till we get there and add this value to the cache.
        if n < 2:
        	return n
        else:
        	if cache.get(n-2) is None:
        		cache[n-2] = fib_jit(n-2)
        	if cache.get(n-1) is None:
        		cache[n-1] = fib_jit(n-1)
        	return cache[n-2] + cache[n-1]

