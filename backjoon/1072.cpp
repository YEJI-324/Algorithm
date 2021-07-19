// 게임
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

int main() {
	long long X, Y, Z, ans = 0;

	scanf("%lld %lld", &X, &Y);
	Z = 100 * Y / X;

	long long left=1, right=1000000000, mid;

	if (Z >= 99) { //승률이 99, 100일 때
		printf("-1");
		return 0;
	}

	while (left <= right) {
		mid = (left + right) / 2;
		int temp = 100 * (Y + mid) / (X + mid);

		if (temp < Z + 1) {
			left = mid + 1;
		}
		else {
			right = mid - 1;
		}
	}

	printf("%d", left);
	return 0;
}