#Sieve of Eratosthenes

class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        
        primes = [True] * (n)
        primes[0] = primes[1] = False
         
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        return sum(primes)
    
testing = Solution()
print(testing.countPrimes(10))
print(testing.countPrimes(0))
print(testing.countPrimes(1))

#runtime: 1275ms, beats 54.34%
#memory: 57.96MB, beats 69.99%