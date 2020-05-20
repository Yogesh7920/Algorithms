def all_pair_sp(g):
    am = g.adjacency_matrix()
    vertices = g.nodes
    for k in vertices:
        for i in vertices:
            for j in vertices:

                am[i][j] = min(am[i][j], am[i][k] + am[k][j])

    return am
