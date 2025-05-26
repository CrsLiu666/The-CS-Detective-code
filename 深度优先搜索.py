# 定义示例图
GRAPH = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': []
}
 
# 定义DFS算法，查找从起始节点到目标节点的路径
def dfs(graph, start, end, path=[]):
    # 将当前节点添加到路径中
    path = path + [start]
    print("当前路径list",str(path))
    # 如果当前节点等于目标节点，返回找到的路径
    if start == end:
        return path
 
    # 如果当前节点不在图中，返回None
    if start not in graph:
        return None
 
    # 遍历当前节点的邻居节点
    for node in graph[start]:
        print("当前点是",node)
        # 如果邻居节点不在已访问的路径中，继续DFS
        if node not in path:
            print(node + ' not in'+ str(path))
            new_path = dfs(graph, node, end, path)
            # 如果找到路径，返回该路径
            if new_path:
                print("new path" + str(new_path))
                return new_path
        print("*"*100)
    # 如果无法找到路径，返回None
    return None
 
# 调用DFS算法查找从A到G的路径
path = dfs(GRAPH, 'A', 'W')
if path:
    print("Path from A to W:", path)
else:
    print("No path found.")
