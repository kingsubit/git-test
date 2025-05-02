#include<iostream>
#include<vector>
using namespace std;

class Vertex {
public:
    Vertex(int vertex_id);
    int getMatrixIndex();
private:
    friend class Graph;
    int vertex_id;
};
Vertex::Vertex(int vertex_id) {
    this->vertex_id = vertex_id;
}
int Vertex::getMatrixIndex() {
    return vertex_id;
}

class Graph {
public:
    int vertexCount = 0;
    int edgeCount = 0;
    Graph(int N);
    void insertVertex(int vertex_id);
    void eraseVertex(int vertex_id);
    void insertEdge(int src_vertex_id, int dst_vertex_id);
    void eraseEdge(int src_vertex_id, int dst_vertex_id);

private:
    Vertex* findVertex(int vertex_id);
    int N;

    vector<Vertex*> vertices_list;
    vector<vector<bool>> adjacency_matrix;
};

Graph::Graph(int N) {
    this->N = N;
    vertices_list.resize(N + 1, nullptr);
    adjacency_matrix.resize(N + 1, vector<bool>(N + 1, false));
}

void Graph::insertVertex(int vertex_id) {
    if (findVertex(vertex_id) != nullptr) return;

    Vertex* new_vertex = new Vertex(vertex_id);
    vertices_list[vertex_id] = new_vertex;
    vertexCount++;
}

void Graph::eraseVertex(int vertex_id) {
    Vertex* erase = findVertex(vertex_id);
    if (erase == nullptr) return;

    for (int i = 1; i <= N; i++) {
        adjacency_matrix[i][erase->getMatrixIndex()] = false;
        adjacency_matrix[erase->getMatrixIndex()][i] = false;
    }

    delete vertices_list[vertex_id];
    vertices_list[vertex_id] = nullptr;
    vertexCount--;
}

void Graph::insertEdge(int src_vertex_id, int dst_vertex_id) {
    Vertex* src = findVertex(src_vertex_id);
    Vertex* dst = findVertex(dst_vertex_id);

    if (src == nullptr || dst == nullptr) {
        cout << -1 << '\n';
        return;
    }
    if (adjacency_matrix[src_vertex_id][dst_vertex_id] == false &&
        adjacency_matrix[dst_vertex_id][src_vertex_id] == false) {
        adjacency_matrix[src_vertex_id][dst_vertex_id] = true;
        adjacency_matrix[dst_vertex_id][src_vertex_id] = true;
        edgeCount++;
         }
    else {
        cout << -1 << '\n';
    }
}

void Graph::eraseEdge(int src_vertex_id, int dst_vertex_id) {
    Vertex* src = findVertex(src_vertex_id);
    Vertex* dst = findVertex(dst_vertex_id);

    if (src == nullptr || dst == nullptr) return;
    if (adjacency_matrix[src_vertex_id][dst_vertex_id] == false ||
        adjacency_matrix[dst_vertex_id][src_vertex_id] == false) {
        return;
    }

    adjacency_matrix[src_vertex_id][dst_vertex_id] = false;
    adjacency_matrix[dst_vertex_id][src_vertex_id] = false;
    edgeCount--;
}

Vertex* Graph::findVertex(int vertex_id) {
    return vertices_list[vertex_id];
}

int main() {
    int N, M, number, src, dst;
    cin >> N >> M;
    Graph gp(2001);

    for (int i = 0; i < N; i++) {
        cin >> number;
        gp.insertVertex(number);
    }
    for (int i = 0; i < M; i++) {
        cin >> src >> dst;
        gp.insertEdge(src, dst);
    }
    cout << gp.vertexCount << " " << gp.edgeCount;
}
