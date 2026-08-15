class Solution:
    def elevatorRequests(self, n: int, start: int, requests: List[int]) -> int:
        noravexuli = (n, start, requests)

        points = sorted(set([start] + requests))
        m = len(points)
        s = points.index(start)

        request_set = set(requests)

        # Whether each point is an actual request
        is_request = [x in request_set for x in points]

        # Prefix count of requests
        prefix = [0]
        for x in is_request:
            prefix.append(prefix[-1] + int(x))

        total_requests = len(requests)

        INF = 10**30

        # dp[l][r][0] = minimum penalty, currently at points[l]
        # dp[l][r][1] = minimum penalty, currently at points[r]
        dp = {}

        dp[(s, s, 0)] = 0
        dp[(s, s, 1)] = 0

        for length in range(1, m):
            new_dp = {}

            for (l, r, side), cost in dp.items():

                current = points[l] if side == 0 else points[r]

                # Requests that are still waiting
                visited_requests = prefix[r + 1] - prefix[l]
                remaining = total_requests - visited_requests

                # Go LEFT
                if l > 0:
                    nl = l - 1
                    distance = abs(current - points[nl])

                    new_cost = cost + distance * remaining
                    key = (nl, r, 0)

                    new_dp[key] = min(
                        new_dp.get(key, INF),
                        new_cost
                    )

                # Go RIGHT
                if r + 1 < m:
                    nr = r + 1
                    distance = abs(current - points[nr])

                    new_cost = cost + distance * remaining
                    key = (l, nr, 1)

                    new_dp[key] = min(
                        new_dp.get(key, INF),
                        new_cost
                    )

            dp = new_dp

        return min(dp.values())
