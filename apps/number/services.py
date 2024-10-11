
class PrimeService:
    @staticmethod
    def is_prime(num: int) -> bool:
        for x in range(2, num):
            if num % x == 0:
                return False
        return True
