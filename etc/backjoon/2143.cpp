// 두 배열의 합
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T, n, m;
	vector<long long> A, B;

	scanf("%d", &T);
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int temp = 0;
		scanf("%d", &temp);
		A.push_back(temp);
	}

	scanf("%d", &m);
	for (int i = 0; i < m; i++) {
		int temp = 0;
		scanf("%d", &temp);
		B.push_back(temp);
	}

	// A의 부집합
	vector<long long> A_sub;
	for (int i = 0; i < n; i++) {
		long long sum = A[i];
		A_sub.push_back(sum);
		for (int j = i + 1; j < n; j++) {
			sum += A[j];
			A_sub.push_back(sum);
		}
	}
	// B의 부집합
	vector<long long> B_sub;
	for (int i = 0; i < m; i++) {
		long long sum = B[i];
		B_sub.push_back(sum);
		for (int j = i + 1; j < m; j++) {
			sum += B[j];
			B_sub.push_back(sum);
		}
	}

	// 정렬하기
	sort(A_sub.begin(), A_sub.end());
	sort(B_sub.begin(), B_sub.end());

	// 투 포인터 사용하기
	long long ans = 0;
	long long cnt = 0;
	int B_idx = B_sub.size() - 1;

	for (int A_idx = 0; A_idx < A_sub.size(); A_idx++) {
		int target = T - A_sub[A_idx];
		if (A_idx > 0 && A_sub[A_idx] == A_sub[A_idx - 1]) {
			ans += cnt;
		}
		else {
			cnt = 0;
			while (0 <= B_idx && target < B_sub[B_idx]) {
				B_idx--;
			}
			while (0 <= B_idx && target == B_sub[B_idx]) {
				cnt++;
				B_idx--;
			}
			ans += cnt;
		}
	}
	printf("%lld", ans);
	return 0;
}
