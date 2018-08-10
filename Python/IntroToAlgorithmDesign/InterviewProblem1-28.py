import time


def divide_naive(numerator, denominator):
    quotient = 0

    while numerator >= denominator:
        numerator -= denominator
        quotient += 1

    return quotient


def divide_fast(numerator, denominator):
    quotient = 0
    quot_accumulator = 1
    den_accumulator = denominator

    while numerator >= denominator:
        if numerator < den_accumulator:
            den_accumulator = denominator
            quot_accumulator = 1

        numerator = numerator - den_accumulator
        quotient = quotient + quot_accumulator
        quot_accumulator = quot_accumulator + quot_accumulator
        den_accumulator = den_accumulator + den_accumulator

    return quotient


if __name__ == '__main__':
    naive_time = time.time()
    print(divide_naive(32142153, 2))
    print("Divide Naive: %s seconds" % (time.time() - naive_time))

    fast_time = time.time()
    print(divide_fast(32142153, 2))
    print("Divide Fast: %s seconds" % (time.time() - fast_time))