// ºÎºÐÇÕ
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

int main() {
	int N, S;
	int low = 0, high = 0, sum = 0, min = 1000000;
	int arr[1000000];

	scanf("%d %d", &N, &S);
	for (int i = 0; i < N; i++) {
		scanf("%d", &arr[i]);
	}

	while (high <= N) {
		if (sum >= S) {
			sum -= arr[low];
			low++;
			int temp = high - low + 1;
			if (temp < min) {
				min = temp;
			}
		}
		else {
			sum += arr[high];
			high++;
		}
	}

	if (min == 1000000) {
		printf("0");
	}
	else printf("%d\n", min);
	return 0;
}