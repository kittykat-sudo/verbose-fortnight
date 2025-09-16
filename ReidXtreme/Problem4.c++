#include <bits/stdc++.h>
using namespace std;

struct DSU {
    int n;
    vector<int> p, r;
    DSU(int n=0): n(n), p(n+1), r(n+1,0) { iota(p.begin(), p.end(), 0); }
    int find(int x){ return p[x]==x?x:p[x]=find(p[x]); }
    bool unite(int a,int b){
        a=find(a); b=find(b);
        if(a==b) return false;
        if(r[a]<r[b]) swap(a,b);
        p[b]=a;
        if(r[a]==r[b]) r[a]++;
        return true;
    }
};

struct Edge {
    int u, v;
    long long c, p;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if(!(cin >> n >> m)) return 0;
    vector<Edge> e(m);
    for(int i=0;i<m;i++){
        cin >> e[i].u >> e[i].v >> e[i].c >> e[i].p;
    }

    // 1) Find lambda = max bottleneck
    vector<int> idx(m);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(), [&](int a, int b){
        return e[a].p > e[b].p; // descending by capacity
    });
    DSU dsu1(n);
    int merges = 0;
    long long lambda = 0;
    for(int id: idx){
        if(dsu1.unite(e[id].u, e[id].v)){
            merges++;
            lambda = e[id].p; // last edge that helped connect
            if(merges == n-1) break;
        }
    }
    // Assuming the graph can be connected as per problem statement.

    // 2) Min-cost spanning tree on edges with p >= lambda
    vector<int> filt;
    filt.reserve(m);
    for(int i=0;i<m;i++) if(e[i].p >= lambda) filt.push_back(i);
    sort(filt.begin(), filt.end(), [&](int a, int b){
        if(e[a].c != e[b].c) return e[a].c < e[b].c; // ascending cost
        return e[a].p > e[b].p; // tie-break (optional)
    });
    DSU dsu2(n);
    long long totalCost = 0;
    int taken = 0;
    for(int id: filt){
        if(dsu2.unite(e[id].u, e[id].v)){
            totalCost += e[id].c;
            if(++taken == n-1) break;
        }
    }

    cout << lambda << "\n" << totalCost << "\n";
    return 0;
}