def is_prime(num):
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def get_primes(nums):
    for num in nums:
        if is_prime(num):
            yield num

