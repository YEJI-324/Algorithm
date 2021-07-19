// 스택
//#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	int N;
	string command;

	stack<int> st;

	cin >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> command;
		//cout << N << " :" << command << endl;
		if (command == "push") {
			// 정수 X를 스택에 추가
			int X = 0;
			cin >> X;
			st.push(X);
		}
		else if (command == "pop") {
			// 가장 위 정수 삭제, 출력 공백이면 -1 출력
			if (st.empty()) {
				cout << "-1" << endl;
			}
			else {
				cout << st.top() << endl;
				st.pop();
			}
		}
		else if (command == "size") {
			// 크기 출력
			cout << st.size() << endl;
		}
		else if (command == "empty") {
			// empty 면 1 아니면 0 출력
			if (st.empty()) {
				cout << "1" << endl;
			}
			else {
				cout << "0" << endl;
			}
		}
		else if (command == "top") {
			// top출력 없으면 -1 출력
			if (st.empty()) {
				cout << "-1" << endl;
			}
			else {
				cout << st.top() << endl;
			}
		}
	}

	return 0;
}