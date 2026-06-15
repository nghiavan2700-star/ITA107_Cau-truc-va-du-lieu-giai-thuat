def fib_tab(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def build_combo_dp_table(prices, scores, B):
    n = len(prices)
    dp = [[0] * (B + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(B + 1):
            dp[i][b] = dp[i - 1][b]
            if prices[i - 1] <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - prices[i - 1]] + scores[i - 1])

    return dp

def trace_combo_from_dp(dp, prices, scores, B):
    chosen = []
    i = len(prices)
    b = B

    while i > 0:
        if dp[i][b] != dp[i - 1][b]:
            chosen.append(i - 1)
            b -= prices[i - 1]
        i -= 1

    chosen.reverse()
    return chosen

def combo_knapsack_1d(prices, scores, B):
    dp = [0] * (B + 1)

    for price, score in zip(prices, scores):
        for b in range(B, price - 1, -1):
            dp[b] = max(dp[b], dp[b - price] + score)

    return dp[B]

def demo_dp_basics():
    print("fib(10):", fib_tab(10))
    print("climb_stairs(5):", climb_stairs(5))

def demo_combo_knapsack_2d():
    names = ["Áo", "Giày", "Túi", "Mũ", "Đồng hồ"]
    prices = [3, 4, 5, 2, 6]
    scores = [4, 5, 7, 3, 9]
    B = 10

    dp = build_combo_dp_table(prices, scores, B)
    chosen = trace_combo_from_dp(dp, prices, scores, B)

    print("Max score:", dp[len(prices)][B])
    print("Chọn:")
    for i in chosen:
        print(names[i], prices[i], scores[i])

def demo_combo_knapsack_1d():
    prices = [3, 4, 5, 2, 6]
    scores = [4, 5, 7, 3, 9]
    B = 10

    dp = build_combo_dp_table(prices, scores, B)
    print("2D:", dp[len(prices)][B])
    print("1D:", combo_knapsack_1d(prices, scores, B))
    