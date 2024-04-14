#include <bits/stdc++.h>
using namespace std;

string mp = "urdl";
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};


int Manhattan_Distance(string &s) {
    int ret = 0;
    for(int i = 0; i < 9; i++) 
    {
        if(s[i] != '0') 
            ret += abs(i / 3 - (s[i] - '1') / 3) + abs(i % 3 - (s[i] - '1') % 3);
    }
    return ret;
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

int main() 
{   
    string input;
    getline(cin, input);
    input.erase(std::remove(input.begin(), input.end(), ' '), input.end());
    std::replace(input.begin(), input.end(), 'x','0'), input.end();
    int ju=inversionCount(input);
	if(ju){
		cout << "unsolvable" << "\n";
		return 0;
	}

    priority_queue<pair<int, string>, vector<pair<int, string>>, greater<pair<int, string>>> pq;
    unordered_map<string, int> dist;
    unordered_map<string, pair<int, string>> path;
    string ans;
    string target;
    target = "123456780";
    dist[input] = 0;
    pq.push({Manhattan_Distance(input) , input});
    
    while(!pq.empty()) 
    {
        string s = pq.top().second;
        pq.pop();
        if(s == "123456780") 
            break;
        int k = s.find('0');

        for(int i = 0; i < 4; i++) {
            int x = k / 3 + dx[i], y = k % 3 + dy[i];
            if(x < 0 || x >= 3 || y < 0 || y >= 3) 
                continue;
            string t(s);
            swap(t[k], t[x * 3 + y]);

            if(!dist.count(t) || dist[t] > dist[s] + 1) {
                dist[t] = dist[s] + 1;
                path[t] = {i, s};
                pq.push({dist[t] + Manhattan_Distance(t), t});
            }
        }
    }

    while (!path[target].second.empty()) {
        ans.push_back(mp[path[target].first]);
        target = path[target].second;
    }
    reverse(ans.begin(), ans.end());
    cout << ans;
    
    return 0;
}