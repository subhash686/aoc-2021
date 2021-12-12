import os


def paths(steps):
    path = os.getcwd()
    file_path = os.path.join(path, 'caves.txt')
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    graph = {}
    for line in Lines:
        input = line.strip()
        edges = input.split("-")
        if not graph.get(edges[0], None):
            graph[edges[0]] = []
        if not graph.get(edges[1], None):
            graph[edges[1]] = []

        if edges[1] not in graph.get(edges[0]):
            graph[edges[0]].append(edges[1])
        if edges[0] not in graph.get(edges[1]):
            graph[edges[1]].append(edges[0])
    count = [0]
    dfs(graph, "start", {}, count, {})
    print(count)


def dfs(graph, node, visited, count, two):
    if node == "end":
        count[0] += 1
        return
    
    if node != "start" and node.lower() == node and visited.get(node, 0) == 1 and not two.get(0, None):
        two[0] = node

    if two.get(0, None) != node and node.lower() == node and visited.get(node, 0) > 0:
        return
    if two.get(0, None) == node and visited.get(node, 0) > 1:
        return
    if node.lower() == node:
        visited[node] = visited.get(node, 0) + 1
    for edge in graph.get(node, []):
        dfs(graph, edge, visited, count, two)
    if node.lower() == node and visited.get(node,0)> 0:
        visited[node] -= 1
        if visited[node] == 1:
            two[0] = None
    

if __name__ == "__main__":
    paths(True)
