#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <sstream>
#include <cstring>

using namespace std;

const int INF = 1e9;

struct State {
    int board[3][3];
    int x, y; // 'x'坐标

    State() {
        x = y = 0;
        memset(board, 0, sizeof(board));
    }

    // hash
    size_t hash() const {
        size_t h = 0;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                h = h * 10 + board[i][j];
            }
        }
        return h;
    }

    bool operator==(const State& other) const {
        return memcmp(board, other.board, sizeof(board)) == 0;
    }
};

struct StateHash {
    size_t operator()(const State& state) const {
        return state.hash();
    }
};

struct HeapNode {
    State state;
    int steps;

    HeapNode(const State& s, int st) : state(s), steps(st) {}

    bool operator>(const HeapNode& other) const {
        return steps > other.steps;
    }
};

int dijkstra(const State& start, const State& target) {
    unordered_map<State, int, StateHash> dist;
    priority_queue<HeapNode, vector<HeapNode>, greater<HeapNode>> pq;

    dist[start] = 0;
    pq.push(HeapNode(start, 0));

    while (!pq.empty()) {
        HeapNode node = pq.top();
        pq.pop();

        if (node.state == target) {
            return node.steps;
        }

        if (node.steps > dist[node.state]) {
            continue;
        }

        int dx[] = {0, 0, -1, 1};
        int dy[] = {-1, 1, 0, 0};

        for (int k = 0; k < 4; ++k) {
            int nx = node.state.x + dx[k];
            int ny = node.state.y + dy[k];

            if (nx < 0 || nx >= 3 || ny < 0 || ny >= 3) {
                continue;
            }

            State next = node.state;
            swap(next.board[node.state.x][node.state.y], next.board[nx][ny]);
            next.x = nx;
            next.y = ny;

            int newDist = node.steps + 1;
            if (!dist.count(next) || newDist < dist[next]) {
                dist[next] = newDist;
                pq.push(HeapNode(next, newDist));
            }
        }
    }

    return -1; 
}

int inversionCount(const std::string& str) {
    int count = 0;
    for (size_t i = 0; i < str.size(); ++i) {
        if (str[i] == '0') continue; // Ignore digit 0
        for (size_t j = i + 1; j < str.size(); ++j) {
            if (str[j] != '0' && str[j] < str[i]) {
                ++count;
            }
        }
    }
    return (count % 2 == 0) ? 0 : -1;
}


int main() {
    State start, target;

    string input;
    getline(cin, input);
    
    stringstream ss(input);
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            string cell;
            ss >> cell;
            if (cell == "x") {
                start.board[i][j] = 0; // 'x'->0
                start.x = i;
                start.y = j;
            } else {
                start.board[i][j] = stoi(cell);
            }
        }
    }
    input.erase(std::remove(input.begin(), input.end(), ' '), input.end());
    std::replace(input.begin(), input.end(), 'x','0'), input.end();
    int ju=inversionCount(input);
	if(ju){
		cout << -1 << "\n";
		return 0;
	}

    target.board[0][0] = 1; target.board[0][1] = 2; target.board[0][2] = 3;
    target.board[1][0] = 4; target.board[1][1] = 5; target.board[1][2] = 6;
    target.board[2][0] = 7; target.board[2][1] = 8; target.board[2][2] = 0;
    target.x = 1; target.y = 0;

    int steps = dijkstra(start, target);
    cout << steps << endl;

    return 0;
}