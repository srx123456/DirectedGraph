import networkx as nx
import matplotlib.pyplot as plt

# 配置
config = {
    "a:1234": "b:2346",
    "b:2346": "c:786",
    "b:345": "d:356",
    "d:356": "a:378"
}

# 创建有向图
G = nx.DiGraph()

# 添加边
for start, end in config.items():
    G.add_edge(start, end)

# 画图
nx.draw(G, with_labels=True)
plt.show()
