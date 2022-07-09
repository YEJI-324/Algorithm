// 합이 0인 네 정수
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> a, b, c, d;
vector<int> ab, cd;
long long ans = 0; // 이걸 int로 하면 안된다,,,

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int u, v, w, x;
		scanf("%d %d %d %d", &u, &v, &w, &x);
		a.push_back(u);
		b.push_back(v);
		c.push_back(w);
		d.push_back(x);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			ab.push_back(a[i] + b[j]);
			cd.push_back(c[i] + d[j]);
		}
	}

	sort(ab.begin(), ab.end());
	sort(cd.begin(), cd.end());
	long long cnt = 0;
	int p_cd = cd.size() - 1;
	for (int p_ab = 0; p_ab < ab.size(); p_ab++) {
		int target = -ab[p_ab];
		if (p_ab > 0 && ab[p_ab] == ab[p_ab-1]) {
			ans += cnt;
		}
		else {
			cnt = 0;
			while (0 <= p_cd && target < cd[p_cd]) {
				p_cd--;
			}
			while (0 <= p_cd && target == cd[p_cd]) {
				cnt++;
				p_cd--;
			}
			ans += cnt;
		}
	}
	printf("%lld", ans);
	return 0;
}