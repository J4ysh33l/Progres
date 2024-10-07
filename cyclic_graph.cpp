#include <iostream>
#include <vector>
#include <list>

using namespace std;

class Graph {
    int V;
    vector<list<int>> adj;

    bool isCyclicUtil(int v, vector<bool>& visited, int parent) {
        visited[v] = true;
        for (auto i : adj[v]) {
            if (!visited[i]) {
                if (isCyclicUtil(i, visited, v))
                    return true;
            } else if (i != parent) {
                return true;
            }
        }
        return false;
    }

public:
    Graph(int V) {
        this->V = V;
        adj.resize(V);
    }

    void addEdge(int v, int w) {
        adj[v].push_back(w);
        adj[w].push_back(v);
    }

    bool isCyclic() {
        vector<bool> visited(V, false);
        for (int i = 0; i < V; ++i) {
            if (!visited[i]) {
                if (isCyclicUtil(i, visited, -1))
                    return true;
            }
        }
        return false;
    }
};

int main() {
    Graph g(3);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 0);

    if (g.isCyclic())
        cout << "Graph contains cycle\n";
    else
        cout << "Graph does not contain cycle\n";

    return 0;
}
 