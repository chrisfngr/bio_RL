import numpy as np
import pandas as pd
import gym
from gym.utils import seeding
from gym import spaces

class BioEnv(gym.Env):
    
    metadata = {'render.modes': ['human']}
    total_year  = 0
    trans_matrix = np.array([])
    np_random = 0
    current_reward = 0
    current_action = 0
    next_state = 0
    current_state = 0
    
    def __init__(self,year,states,trans_matrx) -> None:
        self.root = states
        self.states = states
        self.action_space = spaces.Discrete(7)
        # self.state_nnmber = amount_states
        self.total_year = year
        self.trans_matrix = trans_matrx
        #需要一个table来记录到底哪个状态经历过了
        self.seed()
        self.reset()
        
        
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
        
    def takeaction(self,action):
        next_p = np.random.choice([i for i in range(8)],p=self.trans_matrix[action])
        return next_p
    
    
    def step(self,action):
        state = self.states
        done = self.checkTerminal(state)
        self.current_state = state.id
        if done == True:
            self.current_reward = 0
            self.current_action = action
            return state, 0, True, {}
        next_index = self.takeaction(action)
        self.current_action = action
        #没判断是不是截至state
        next_state = state.childs[next_index]
        self.next_state = next_state.id
        self.states = next_state
        done = self.checkTerminal(next_state)#判断是不是截至state
        r = next_state.r#r表示奖励
        self.current_reward = next_state.r
        return next_state, r, done,{}
    
    
    def checkTerminal(self,state):
        if state.year == self.total_year:
            done = True
        else:
            done = False
        return done
    
    def render(self, mode="human", close=False):
        print(f'Current Year: {self.states.year}')
        print(f'Current action: {self.current_action}')
        print(f'State:{self.current_state} -> {self.next_state}')
        print(f'Gain Reward: {self.current_reward}')
        print('*'*20)
        
    #初始化，初始化到初始年份
    def reset(self):
        
        self.states = self.root
        self.current_reward  = 0
        self.next_state = 0
        
        return self.states