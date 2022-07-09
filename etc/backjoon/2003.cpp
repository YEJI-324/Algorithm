// 수들의 합2
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

int main() {
	int N, M;
	int low = 0, high = 0, cnt = 0, sum = 0;
	int arr[10000];

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}

	while (high <= N) {
		if (sum >= M) {
			sum -= arr[low];
			low++;
		}
		else {
			sum += arr[high];
			high++;
		}

		if (sum == M) {
			cnt++;
		}
	}

	printf("%d\n", cnt);
	return 0;
}