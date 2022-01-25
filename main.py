import socket
import platform
import multiprocessing
import psutil
import timeit
import math
import itertools

def bench_pidigits(ndigits=1000, loops=100):
    def calc_ndigits(n):
        def gen_x():
            return map(lambda k: (k, 4*k + 2, 0, 2*k + 1), itertools.count(1))
        def compose(a, b):
            aq, ar, as_, at = a
            bq, br, bs, bt = b
            return (aq * bq,
                    aq * br + ar * bt,
                    as_ * bq + at * bs,
                    as_ * br + at * bt)

        def extract(z, j):
            q, r, s, t = z
            return (q*j + r) // (s*j + t)

        def pi_digits():
            z = (1, 0, 0, 1)
            x = gen_x()
            while 1:
                y = extract(z, 3)
                while y != extract(z, 4):
                    z = compose(z, next(x))
                    y = extract(z, 3)
                z = compose((10, -10*y, 0, 1), z)
                yield y
        return list(itertools.islice(pi_digits(), n))
    for _ in range(loops):
        calc_ndigits(ndigits)
    return



def main():
    
    print("your computer name is "+socket.gethostname())
    print("your OS is "+platform.uname().system)


    print("your OS version is "+platform.platform())

    print("number of CPUs running:")
    print(multiprocessing.cpu_count())

    print("percentage of RAM")
    print(psutil.cpu_percent())

    print("IP address:")
    print(socket.gethostbyname(socket.gethostname()))


    t_default = 6.388216104
    start_time = timeit.default_timer()
    bench_pidigits(ndigits=1000, loops=100)
    elapsed_time = timeit.default_timer() - start_time
    print("relative elapsed:", elapsed_time/t_default)


if __name__ == '__main__':
    main()