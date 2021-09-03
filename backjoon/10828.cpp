// ����
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
			// ���� X�� ���ÿ� �߰�
			int X = 0;
			cin >> X;
			st.push(X);
		}
		else if (command == "pop") {
			// ���� �� ���� ����, ��� �����̸� -1 ���
			if (st.empty()) {
				cout << "-1" << endl;
			}
			else {
				cout << st.top() << endl;
				st.pop();
			}
		}
		else if (command == "size") {
			// ũ�� ���
			cout << st.size() << endl;
		}
		else if (command == "empty") {
			// empty �� 1 �ƴϸ� 0 ���
			if (st.empty()) {
				cout << "1" << endl;
			}
			else {
				cout << "0" << endl;
			}
		}
		else if (command == "top") {
			// top��� ������ -1 ���
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