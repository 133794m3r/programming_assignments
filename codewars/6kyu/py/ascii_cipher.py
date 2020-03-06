import itertools

def factors(n):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n

def ascii_cipher(message, key):
    mod=1 if key > -1 else -1
    primes=list(factors(key*mod))
    prime=primes[::-1][0]*mod
    conv=lambda x:x % 128
    return ''.join(chr(conv(x+prime)) for x in list(map(lambda x:ord(x),message)))

