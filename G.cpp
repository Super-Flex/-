#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll dp[1500][1500];

ll gn(ll level, ll idx) {
    return (level * (level - 1)) / 2 + idx + 1;
}

ll dfs(ll l, ll i) {
    if (dp[l][i] != -1) {
        return dp[l][i];
    }
    dp[l][i] = gn(l, i) * gn(l, i);
    pair<ll, ll> left = make_pair(l - 1, i - 1);
    if (l - 1 >= 1 && i - 1 >= 0) {
        dp[l][i] += max(0LL, dfs(left.first, left.second));
    }
    pair<ll, ll> right = make_pair(l - 1, i);
    if (l - 1 >= 1 && right.second < l - 1) {
        dp[l][i] += max(0LL, dfs(right.first, right.second));
    }
    pair<ll, ll> mid = make_pair(l - 2, i - 1);
    if (mid.first >= 1 && 0 <= mid.second && mid.second < l - 2) {
        dp[l][i] -= max(0LL, dfs(mid.first, mid.second));
    }
    return dp[l][i];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll n;
    cin >> n;
    memset(dp, -1, sizeof(dp));
    for (ll ___ = 0; ___ < n; ___++) {
        ll x;
        cin >> x;
        ll level = 1;
        ll p = 1;
        while (p < x) {
            p += level + 1;
            level += 1;
        }
        ll idx = x - (p - level) - 1;
        
        cout << dfs(level, idx) << "\n";
    }

    return 0;
}
