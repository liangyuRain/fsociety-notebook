#include <iostream>
#include <stack>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    auto arr = new unsigned long long[n];
    auto jump = new int[n];
    int max = 0;
    stack<int> st;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        while(!st.empty() && arr[st.top()] > arr[i]) {
            jump[st.top()] = i;
            st.pop();
        }
        st.emplace(i);
    }
    while(!st.empty()) {
        jump[st.top()] = -1;
        st.pop();
    }
    for (int i = 0; i < q; ++i) {
        unsigned long long int v;
        int l, r;
        cin >> v >> l >> r;
        --l;
        --r;
        v %= arr[l];
        while(jump[l] != -1 && jump[l] <= r) {
            l = jump[l];
            v %= arr[l];
        }
        cout << v << endl;
    }
}