#!/usr/bin/env python3
"""Edmonds' algorithm — minimum spanning arborescence (directed MST)."""

def min_arborescence(n, edges, root):
    """edges=[(u,v,w)], returns min-cost arborescence rooted at root."""
    INF = float('inf'); res = 0
    while True:
        # Find min incoming edge for each non-root node
        min_in = [INF]*n; min_edge = [-1]*n
        for i,(u,v,w) in enumerate(edges):
            if v != root and w < min_in[v]: min_in[v] = w; min_edge[v] = i
        for v in range(n):
            if v != root and min_in[v] == INF: return -1  # no arborescence
        # Add min edges, check for cycles
        res += sum(min_in[v] for v in range(n) if v != root)
        # Find cycles
        visited = [-1]*n; cyc_id = [-1]*n; num_cyc = 0
        for v in range(n):
            u = v; path = []
            while u != root and visited[u] == -1:
                visited[u] = v; path.append(u)
                u = edges[min_edge[u]][0]
            if u != root and visited[u] == v:
                # Found cycle
                while cyc_id[u] == -1:
                    cyc_id[u] = num_cyc; u = edges[min_edge[u]][0]
                num_cyc += 1
        if num_cyc == 0: return res
        for v in range(n):
            if cyc_id[v] == -1: cyc_id[v] = num_cyc; num_cyc += 1
        # Contract cycles
        new_edges = []
        for u,v,w in edges:
            nu, nv = cyc_id[u], cyc_id[v]
            if nu != nv: new_edges.append((nu, nv, w - min_in[v]))
        edges = new_edges; n = num_cyc; root = cyc_id[root]

def main():
    edges = [(0,1,2),(0,2,5),(1,2,2),(2,0,3),(2,1,4)]
    print(f"Min arborescence cost: {min_arborescence(3, edges, 0)}")

if __name__ == "__main__": main()
