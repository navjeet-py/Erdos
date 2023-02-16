"""
used dp with space optimization.
Ran in around 2 minutes in cpp.
"""

"""
int possibles[10][4] = {
            {3, 10, 10, 10},
            {2, 4,  10, 10},
            {1, 3,  5,  10},
            {2, 0,  6,  10},
            {1, 5,  7,  10},
            {2, 4,  6,  8},
            {3, 5,  9,  10},
            {4, 8,  10, 10},
            {5, 7,  9,  10},
            {6, 8,  10, 10}
    };

    int current[10], last[11];
    // current is of length 1
    range(i, 0, 10) {
        last[i] = 1;
    }
    last[10] = 0;

    int N = 1000000000;
    range(i, 0, N - 1) {
        if (i % (N/10) == 0) {
            cout << N  <<' ' << i << '\n';
        }
        range(x, 0, 10) {
            current[x] = 0;
            for (int p: possibles[x]) {
                current[x] += last[p];
            }
            current[x] %= mod;
        }
        range(x, 0, 10) {
            last[x] = current[x];
        }
    }
    int ans = 0;
    range(i, 0, 10) {
        ans += last[i];
    }
    cout << ans << '\n';
    print(last, 10);

"""


# ANSWER is 5398857532.
