def triple_step(n):
    return triple_step_dp(n, [-1] * (n + 1))


def triple_step_dp(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    if memo[n] == -1:
        memo[n] = triple_step_dp(n - 1, memo) \
                  + triple_step_dp(n - 2, memo) \
                  + triple_step_dp(n - 3, memo)
    return memo[n]


print(triple_step(eval(input())))
