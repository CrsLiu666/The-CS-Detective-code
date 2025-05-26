# 导入必要的库
from collections import deque  # 使用双端队列实现高效队列操作（popleft()时间复杂度O(1)）
from typing import Dict, List, Set  # 类型提示模块，用于明确变量类型

def bfs(graph: Dict[str, List[str]], start: str) -> None:
    """
    优化后的广度优先搜索(BFS)实现
    功能：遍历图并打印节点访问顺序
    
    参数：
        graph: 图的邻接表表示，格式为 {节点: [邻居列表]}
        start: 开始遍历的起始节点
    
    返回：
        None (直接打印遍历过程)
    """
    # 初始化数据结构
    visited: Set[str] = {start}  # 使用集合存储已访问节点（查找效率O(1)）
    queue: deque[str] = deque([start])  # 初始化队列，存储待访问节点
    
    # 打印初始信息
    print(f"BFS遍历开始，起始节点: {start}")
    print(f"初始已访问集合: {visited}\n")
    
    # 主循环：当队列不为空时持续处理
    while queue:
        # 取出队列最前端的节点（FIFO原则）
        current_node = queue.popleft()
        print(f"正在处理节点: {current_node}")
        print("-" * 50)  # 可视化分隔线
        
        # 遍历当前节点的所有邻居
        # 使用graph.get(current_node, [])避免KeyError异常
        for neighbor in graph.get(current_node, []):
            print(f"检查邻居: {current_node} -> {neighbor}")
            
            # 如果邻居未被访问过
            if neighbor not in visited:
                visited.add(neighbor)  # 标记为已访问
                queue.append(neighbor)  # 加入队列等待处理
                
                # 打印更新信息
                print(f"新节点入队: {neighbor}")
                print(f"更新后已访问集合: {visited}")
            
            # 邻居处理完毕分隔线
            print("#" * 30)

# 示例图（无向图）
graph = {
    'A': ['B', 'C'],   # A连接B和C
    'B': ['A', 'D', 'E'],  # B连接A、D、E
    'C': ['A', 'F'],    # C连接A和F
    'D': ['B'],         # D只连接B
    'E': ['B', 'F'],    # E连接B和F
    'F': ['C', 'E']     # F连接C和E
}

# 执行BFS遍历
bfs(graph, 'A')