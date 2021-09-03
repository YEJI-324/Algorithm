#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

int n, ans;
int chess[14][14];

void recur(int line) {
    if (line == n) {
        ans++;
        return;
    }

    for (int i = 0; i < n; i++) {
        if (chess[line][i] != -1) continue;
        chess[line][i] = line;

        //좌우
        for (int x = 0; x < n; x++) {
            if (chess[line][x] == -1) {
                chess[line][x] = line;
            }
        }

        //하
        for (int y = line; y < n; y++) {
            if (chess[y][i] == -1) {
                chess[y][i] = line;
            }
        }

        //대각선
        for (int y = line, x = i; y < n && 0 <= x; y++, x--) {
            if (chess[y][x] == -1) {
                chess[y][x] = line;
            }
        }
        for (int y = line, x = i; y < n && x < n; y++, x++) {
            if(chess[y][x] == -1) {
                chess[y][x] = line;
            }
        }

        recur(line + 1);
        
        // 좌우 지우기
        for (int x = 0; x < n; x++) {
            if(chess[line][x] == line){
                chess[line][x] = -1;
            }
        }
        // 하 지우기
        for (int y = line; y < n; y++) {
            if (chess[y][i] == line) {
                chess[y][i] = -1;
            }
        }
        //대각선 지우기
        for (int y = line, x = i; y < n && 0 <= x; y++, x--) {
            if (chess[y][x] == line) {
                chess[y][x] = -1;
            }
        }
        for (int y = line, x = i; y < n && x < n; y++, x++) {
            if (chess[y][x] == line) {
                chess[y][x] = -1;
            }
        }
    }
}

int main(){

    for (int i = 0; i < 14; i++) {
        for (int j = 0; j < 14; j++) {
            chess[i][j] = -1;
        }
    }

    scanf("%d", &n);
    recur(0);
    printf("%d", ans);
}