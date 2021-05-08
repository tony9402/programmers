#include <bits/stdc++.h>

using namespace std;

int num_len(int x) {
    int ret = 0;
    while(x) {
        x /= 10;
        ret ++;
    }
    return ret; 
}

int solution(string s) {
    int N = s.size();
    int answer = N;
    for(int i=1;i * 2 <= N; i++) {
        int len = N % i;
        vector<pair<string, int>> zip_slice;
        vector<string> slice;
        for(int j = 0; j < N / i * i; j += i) slice.emplace_back(s.substr(j, i));
        zip_slice.emplace_back(slice[0], 1);
        for(int j = 1; j < (int)slice.size(); j++) {
            if(slice[j] == slice[j - 1]) {
                zip_slice.back().second += 1;
                continue;
            }
            zip_slice.emplace_back(slice[j], 1);
        }
        for(int j = 0; j < (int)zip_slice.size(); j++) {
            auto [ S, cnt ] = zip_slice[j];
            len += (int)S.size();
            if(cnt > 1) len += num_len(cnt);
        }
        answer = min(answer, len);
    }
    return answer;
}
