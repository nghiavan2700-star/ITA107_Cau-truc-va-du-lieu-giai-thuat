from collections import defaultdict

class OrderHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, order_id, order_data):
        idx = self._hash(order_id)
        for i, item in enumerate(self.table[idx]):
            if item[0] == order_id:
                self.table[idx][i] = (order_id, order_data)
                return
        self.table[idx].append((order_id, order_data))

    def get(self, order_id):
        idx = self._hash(order_id)
        for k, v in self.table[idx]:
            if k == order_id:
                return v
        return None

    def remove(self, order_id):
        idx = self._hash(order_id)
        for i, item in enumerate(self.table[idx]):
            if item[0] == order_id:
                self.table[idx].pop(i)
                return True
        return False

def group_coupon_anagrams(codes):
    groups = defaultdict(list)
    for code in codes:
        groups["".join(sorted(code))].append(code)
    return list(groups.values())

def longest_consecutive_days(days):
    s = set(days)
    best = 0
    for x in s:
        if x - 1 not in s:
            y = x
            while y in s:
                y += 1
            best = max(best, y - x)
    return best

def count_revenue_windows(revenues, k):
    count = 0
    prefix = 0
    seen = {0: 1}

    for x in revenues:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count

def rolling_hash_search(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []

    base = 256
    mod = 10 ** 9 + 7
    hpat = 0
    htxt = 0
    power = 1

    for i in range(m):
        hpat = (hpat * base + ord(pattern[i])) % mod
        htxt = (htxt * base + ord(text[i])) % mod
        if i < m - 1:
            power = (power * base) % mod

    res = []
    for i in range(n - m + 1):
        if hpat == htxt and text[i:i + m] == pattern:
            res.append(i)
        if i < n - m:
            htxt = (htxt - ord(text[i]) * power) % mod
            htxt = (htxt * base + ord(text[i + m])) % mod

    return res

def demo_order_hash_table():
    ht = OrderHashTable()
    ht.insert("ORD01", {"name": "An", "total": 120})
    ht.insert("ORD02", {"name": "Binh", "total": 250})
    ht.insert("ORD03", {"name": "Cuong", "total": 180})
    print(ht.get("ORD02"))
    print(ht.remove("ORD02"))
    print(ht.get("ORD02"))

def demo_hashing_all():
    print(group_coupon_anagrams(["SAVE10", "AVES10", "SALE20", "ELAS20"]))
    print("Ngày liên tiếp dài nhất:", longest_consecutive_days([1, 2, 3, 7, 8, 10]))
    print("Số đoạn doanh thu =", count_revenue_windows([2, 3, 1, 4, 2], 5))

def demo_rolling_coupon_search():
    text = "LOG_SAVE10_USED_AVES10_SALE20_SAVE10"
    for p in ["SAVE10", "SALE20", "ABC"]:
        print(p, rolling_hash_search(text, p))
        