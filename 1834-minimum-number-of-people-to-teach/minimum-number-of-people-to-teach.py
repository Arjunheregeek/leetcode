class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        learned = list(map(set, languages))

        total = 0
        vis = [False] * len(languages)
        cnt = [0] * (n + 1)

        def add(u: int) -> None:
            if vis[u]:
                return
            vis[u] = True  # 避免重复统计
            nonlocal total
            total += 1
            for x in languages[u]:
                cnt[x] += 1

        for u, v in friendships:
            # 减一，下标从 0 开始
            if learned[u - 1].isdisjoint(learned[v - 1]):  # 无交集
                add(u - 1)
                add(v - 1)

        return total - max(cnt)
