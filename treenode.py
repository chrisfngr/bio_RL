from collections import defaultdict
import json

with open("./node_r_v2.json", "r", encoding="utf-8") as f:
    rewards_test = json.load(f)

# print(rewards_test[1])
def DFS (node,input_dict):
    if node.id in input_dict:  # 当前节点还有子节点时，继续对每个child向下构造
        for id in input_dict[node.id]:
            cur_node = TreeNode(id)
            DFS(cur_node, input_dict)
            node.add_childs(cur_node)
            node.add_reward(rewards_test[int(node.id)])
    else:  # 当前节点没有子节点，直接返回
        node.add_reward(rewards_test[int(node.id)])
        return


class TreeNode(object):
    year = 0
    r = 0
    def __init__(self, id=None) -> None:
        self.id = id
        self.childs = []

    def add_childs(self, child: "TreeNode"):
        self.childs.append(child)

    def __repr__(self) -> str:
        return str(self.id)
    
    def update_year(self,year):
        self.year = year
        
    def add_reward(self, reward):
        self.r = reward
        
    @classmethod
    def build_tree(cls, input_dict: dict):

        # 深度优先遍历构造多叉树结构

        # 获取字典的第一个key，并以此为根节点构造多叉树
        root = TreeNode(list(input_dict.keys())[0])
        DFS(root, input_dict)

        return root

    @classmethod
    def print_tree(cls, root: "TreeNode"):
        """按照字典输入形式打印输出"""
        if root:
            if root.childs:
                print(root.id, ": ", end="")
                print('[%s]' % (' '.join([str(_.id) for _ in root.childs])))
                for node in root.childs:
                    cls.print_tree(node)
            else:
                print(root.id, ": []")

    @classmethod
    def print_tree_graph(cls, root: "TreeNode"):
        """按照树的层级打印输出"""
        node_with_level = defaultdict(list)
        node_with_level[0].append([root])
        cur_level = 0

        while node_with_level:
            # 打印当前层节点
            cur_nodes_lists = node_with_level.pop(cur_level)
            for nodes_list in cur_nodes_lists:
                print(nodes_list, end=" ")

                for node in nodes_list:  # 如果还有子节点，将其添加到下一层
                    if node.childs:
                        node_with_level[cur_level + 1].append(node.childs)
                    else:  # 没有子节点的话，使用[]占位
                        node_with_level[cur_level + 1].append([])
            cur_level += 1
            print()


