import pandas as pd
import numpy as np
class Qlearning():
    
    def __init__(self, actions,observation_space, learning_rate=0.01, reward_decay=1, e_greedy=0.1,e_decay = 0):
        self.actions = actions  # a list
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = np.zeros((observation_space, len(actions)))
        self.decay = e_decay
        # self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
    
    def choose_action(self,observation):
        # self.check_state_exist(observation)
        
        if np.random.uniform(0,1) > self.epsilon * self.decay:
            state_action = self.q_table[observation.id,:]
            action = np.argmax(state_action)
        else:
            action = np.random.choice(self.actions)        
        return action
    
    
    def learn(self,observationNow,action,rewards,nextState):
        # self.check_state_exist(nextState)
        
        # print(self.q_table)
        # print(observationNow.id)
        q_predict = self.q_table[observationNow.id,int(action)]
        # if done:
        #     q_target = rewards
        # else:
        q_target = rewards + self.gamma * np.max(self.q_table[nextState.id,:])
            
        self.q_table[observationNow.id,int(action)] += self.lr * (q_target - q_predict)
    
    def check_state_exist(self,state):
        
        if state.id not in self.q_table.index:
            self.q_table =  self.q_table.append(
                pd.Series(
                    [0]*len(self.actions),
                    index = self.q_table.columns,
                    name = state.id
                )
            )
    