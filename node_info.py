from env import BioEnv
import pandas as pd
import numpy as np
# from state import State
from treenode import TreeNode
from collections import defaultdict
from Qlearning import Qlearning



def leveltree(root: "TreeNode"):
    """按照树的层级打印输出"""
    node_with_level = defaultdict(list)
    node_with_level[0].append([root])
    cur_level = 0

    while node_with_level:
        # 打印当前层节点
        cur_nodes_lists = node_with_level.pop(cur_level)
        for nodes_list in cur_nodes_lists:
            # print(nodes_list, end=" ")

            for node in nodes_list:  # 如果还有子节点，将其添加到下一层
                if node.childs:
                    node_with_level[cur_level + 1].append(node.childs)
                else:  # 没有子节点的话，使用[]占位
                    node_with_level[cur_level + 1].append([])
        cur_level += 1
    return node_with_level

def post_order_traverse(root):
    if not root:
        root.update_year(0)
        return
    for child in root.childs:
        if child.childs == []:
            child.update_year(3)
        elif child.childs[0].childs == []:
            child.update_year(2)
        else:
            child.update_year(1)
        post_order_traverse(child)
    # print(root.id)


def main():
    trans_matrix = np.array([[0.7 , 0.  , 0.  , 0.  , 0.3 , 0.  , 0.  , 0.  ],
                            [0.6 , 0.  , 0.4 , 0.  , 0.  , 0.  , 0.  , 0.  ],
                            [0.5 , 0.5 , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ],
                            [0.42, 0.  , 0.28, 0.  , 0.18, 0.  , 0.12, 0.  ],
                            [0.35, 0.35, 0.  , 0.  , 0.15, 0.15, 0.  , 0.  ],
                            [0.3 , 0.3 , 0.2 , 0.2 , 0.  , 0.  , 0.  , 0.  ],
                            [0.21, 0.21, 0.14, 0.14, 0.09, 0.09, 0.06, 0.06]])
    total_states = {}
    for i in range(585):
        if i < 73:
            total_states[i] = np.array([x for x in range(8 * i + 1 , 8  * (i+1) + 1)])
        else:
            #total_states[i] = np.array([])
            pass
    
    tree = TreeNode.build_tree(total_states)
    post_order_traverse(tree)
    epsilo_start = 1
    epsilo_end = 0.001
    number_steps = 1
    decay_factor = (epsilo_end/epsilo_start) ** (1/number_steps)
    # TreeNode.print_tree(tree)
    # TreeNode.print_tree_graph(tree)
    # env = BioEnv(3,tree,trans_matrix)
    # RL = Qlearning(actions=list(range(7)),observation_space=585,learning_rate=0.1,reward_decay=1, e_greedy=epsilo_start,e_decay=decay_factor)
    
    node = tree
    for _ in range(3):
        print(f'Current State: {node.id}')
        print(f'Possible Next State: {node.childs}')
        print(f'Pleas input a number between 0 to 7 to select next possible state')
        print('------')
        next_state = int(input())
        print('------')
        print(f'Next State:{node.childs[next_state]}')
        print(f'Rewards:{node.childs[next_state].r}')
        possible_r = []
        for x in node.childs:
            possible_r.append([x.id,x.r])
        print(f'Possible rewards:{possible_r}')
        node = node.childs[next_state]
        print('*****')
        
    # for _ in range(number_steps):
    
    #     ob = env.reset()
    #     epi_state = []


    #     while True:
    #         # env.render()
    #         print('please input a next state number 0 to 7')
    #         action = input()
    #         observation_,reward,done,_ = env.step(int(action))
    #         epi_state.append([ob,action,observation_,reward])
    #         # RL.learn(ob,action,reward,observation_)
            
    #         # action = action_
    #         ob = observation_
    #         env.render()
    #         if done:
    #             break
    #         # env.render()
    #     # RL.learn(ob,action,reward,observation_,done)
    #     # epi_state.reverse()
    #     # print(epi_state)
    #     for x in epi_state:
    #         RL.learn(x[0],x[1],x[3],x[2])

        
    # print('game over')       
    # # print(RL.q_table)
    # result = pd.DataFrame(RL.q_table)
    # result.to_csv('q_table_test.csv',index=True)

if __name__ == '__main__':
    main()