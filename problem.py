class Problemtwo:
    def coinproblem(self, v, coins): ##value V, coins = list of coin denominations
        coins.sort(reverse=True)
        solution = []
        total = 0
        i = 0
        if v == 0:
            return 'No coins needed'
        if v < coins[len(coins)-1]:
            return 'Invalid - lowest coin denomination must be higher than value'
        while total != v and i < 4:
            total = total + coins[i]
            if total > v:
                total = total - coins[i]
                i += 1
            else:
                solution.append(coins[i])
        return len(solution)



