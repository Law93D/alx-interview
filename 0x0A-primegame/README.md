0x0A. Prime Game
Algorithm
Python

Step 1: Understand the Game Mechanics
Players: Maria and Ben.
Game Rounds: There are x rounds, and each round is played with a set of consecutive integers starting from 1 to n.
Objective: Players take turns picking a prime number from the set and removing that prime number along with its multiples. The player who cannot make a move loses the round.
Step 2: Identify Prime Numbers Efficiently
Since the maximum value of n can be up to 10,000, and the game might involve multiple rounds, you'll need an efficient way to identify prime numbers within this range. The Sieve of Eratosthenes algorithm is well-suited for this task.

Step 3: Implement the Game Logic
Precompute Prime Numbers: Use the Sieve of Eratosthenes to generate a list of prime numbers up to the maximum n in nums.
Simulate Each Round: For each round, simulate the game by iteratively removing primes and their multiples until no more moves are possible. Track the winner for each round.
Determine the Overall Winner: Count the number of rounds won by Maria and Ben. The player with the most wins is the overall winner.
Step 4: Code Implementation

Step 5: Test the Implementation
Use the provided example to test the function and ensure it returns the correct results.
Also, consider edge cases such as when n = 1 or when all n values in nums are small or equal.
