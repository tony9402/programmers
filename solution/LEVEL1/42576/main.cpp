#include <bits/stdc++.h>

using namespace std;
map<string, int> mp;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    for(auto &i : participant) mp[i]++;
    for(auto &i : completion ) mp[i]--;
    for(auto i: mp){
        if(i.second != 0){
            answer = i.first;
            break;
        }
    }
    return answer;
}
