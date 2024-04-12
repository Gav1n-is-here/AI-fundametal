#include <iostream>
#include <algorithm>
#include <queue> 
#include <map>
using namespace std;
const int end = 123456780;

map <int, int> state;
map <int, int> ans;
queue <int> q1, q2; 
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int cnt=0, mat[3][3], zx, zy;

inline int toInt() { 
	int now = 0;
	for(int i = 0; i < 3; i++) 
		for(int j = 0; j < 3; j++)
			now = now * 10 + mat[i][j];
	return now;
}
inline void toMatrix(int s) { 
	int div = 100000000;
	for(int i = 0; i < 3; i++)
		for(int j = 0; j < 3; j++) {
			mat[i][j] = (s / div) % 10;
			if(!mat[i][j]) zx = i, zy = j;
			div /= 10;
		}
}

void dbfs(int s) {
	if(s == ::end) return; 
	bool flag;
	state[s] = 1, state[::end] = 2;
	ans[s] = 0, ans[::end] = 1; 
	q1.push(s), q2.push(::end);
	while(!q1.empty() && !q2.empty()) {
		flag = 0;
		int t;
		if(q1.size() > q2.size()) {
			t = q2.front(), q2.pop();
		}else {
			t = q1.front(), q1.pop();
			flag = 1;
		}
		toMatrix(t);
		for(int i = 0; i < 4; i++) {
			int num;
			int nx = dx[i] + zx;
			int ny = dy[i] + zy;
			if(nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
				swap(mat[zx][zy], mat[nx][ny]);
				num = toInt();
				if(!ans.count(num)) {
					ans[num] = ans[t] + 1;
					state[num] = state[t];
					if(flag) q1.push(num);
					else q2.push(num);
				}else if(state[t] + state[num] == 3){
					cnt = ans[t] + ans[num];
					return;
				}
				swap(mat[zx][zy], mat[nx][ny]);
			} 
		}
	}
}

int inversionCount(const std::string& str) {
    int count = 0;
    for (size_t i = 0; i < str.size(); ++i) {
        if (str[i] == '0') continue;
        for (size_t j = i + 1; j < str.size(); ++j) {
            if (str[j] != '0' && str[j] < str[i]) {
                ++count;
            }
        }
    }
    return (count % 2 == 0) ? 0 : -1;
}

int main() {
	string input;
    getline(cin, input);
    input.erase(std::remove(input.begin(), input.end(), ' '), input.end());
    std::replace(input.begin(), input.end(), 'x','0'), input.end();
	int ju=inversionCount(input);
	if(ju){
		cout << -1 << "\n";
		return 0;
	}
    int n = std::stoi(input);
	dbfs(n);	
	cout << cnt << "\n";
	return 0;
} 