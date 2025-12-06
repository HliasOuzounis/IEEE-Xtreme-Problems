#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

const int MAX_A = 30;
const int L = MAX_A + 1;

std::string answer_query(const std::vector<std::vector<int>>& counts_arr, int ql, int qr) {
    long long carry = 0;
    int last_num = -1;

    for (int num = 0; num <= MAX_A; ++num) {
        long long count = (long long)counts_arr[qr][num] - counts_arr[ql - 1][num] + carry;
        if (count % 2 == 1) {
            if (count > 1) {
                return "No";
            }
            if (last_num != -1) {
                return "No";
            }
            last_num = num;
        }
        carry = count / 2;
    }
    while (carry > 1) {
        if (carry % 2 != 0) return "No";
        carry /= 2;
    }
    return (last_num != -1 || carry == 1) ? "Yes" : "No";
}

void solve_case() {
    int n, q;
    if (!(std::cin >> n >> q)) return;

    std::vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }

    std::vector<std::vector<int>> counts_arr(n + 1, std::vector<int>(L, 0));

    for (int i = 0; i < n; ++i) {
        int val = arr[i];
        if (val <= MAX_A) {
            counts_arr[i + 1][val] += 1;
        }
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < L; ++j) {
            counts_arr[i][j] += counts_arr[i - 1][j];
        }
    }
    for (int i = 0; i < q; ++i) {
        int ql, qr;
        std::cin >> ql >> qr;
        std::cout << answer_query(counts_arr, ql, qr) << "\n";
    }
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    solve_case();

    return 0;
}