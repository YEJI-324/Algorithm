// 스도쿠
#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
using namespace std;

int board[9][9]; // 스도쿠 보드
vector<pair<int, int>> points; // 빈칸 저장
int cnt = 0; // 비어있는 칸 수
bool found = false;

bool check_sudoku(pair<int, int> p) {
	// 같은 행, 열
	for (int i = 0; i < 9; i++) {
		if (board[p.first][i] == board[p.first][p.second] && i!=p.second) {
			return false;
		}
		if (board[i][p.second] == board[p.first][p.second] && i!= p.first) {
			return false;
		}
	}

	// 3 * 3에 같은 숫자 있는지
	int square_x = p.first / 3;
	int square_y = p.second / 3;

	for (int i = 3 * square_x; i < 3 * square_x + 3; i++) {
		for (int j = 3 * square_y; j < 3 * square_y + 3; j++) {
			if (board[i][j] == board[p.first][p.second]) {
				if (i != p.first && j != p.second) {
					return false;
				}
			}
		}
	}

	return true;
}

void fill_sudoku(int n) {

	// 빈칸을 다 채웠을 때 종료!
	if (n == cnt) {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				printf("%d ", board[i][j]);
			}
			printf("\n");
		}
		found = true;
		return;
	}

	// 1 ~ 9 까지 채워보기
	for (int i = 1; i <= 9; i++) {
		board[points[n].first][points[n].second] = i;
		// 이 값이 유효한지 체크

		if (check_sudoku(points[n])) {
			// 유효하다면 다음 빈칸 채우기
			fill_sudoku(n + 1);
		}

		if (found) {
			return;
		}
	}
	// 백트래킹!
	board[points[n].first][points[n].second] = 0;
	return;
}

int main() {
	pair<int, int> point;
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &board[i][j]);
			//빈칸이라면!
			if (board[i][j] == 0) {
				cnt++;
				point.first = i;
				point.second = j;
				points.push_back(point);
			}
		}
	}

	fill_sudoku(0);
}
