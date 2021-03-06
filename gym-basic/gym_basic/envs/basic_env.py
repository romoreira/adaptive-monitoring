'''
Auhor: Rodrigo Moreira rodrigo at ufv dot br
Based on: https://towardsdatascience.com/beginners-guide-to-custom-environments-in-openai-s-gym-989371673952
'''


import gym
from stable_baselines.common.env_checker import check_env
import numpy as np

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2
import matplotlib.pyplot as plt
import random
from gym.spaces import Discrete
from gym.spaces import Box

class BasicEnv(gym.Env):

    def __init__(self):
        self.action_space = Discrete(3)
        self.observation_space = Box(low=np.array([0]), high=np.array([100]))
        self.state = 38 + random.randint(-3,3)
        #print("\ninit: "+str(self.state)+"\n")
        self.shower_lenght = 60
    def step(self, action):
        #print("\nAction: "+str(action))
        #print("On state: "+str(self.state))
        self.state += action - 1
        #print("State after aplly action: "+str(self.state))
        self.shower_lenght -= 1
        #print("State of shower_lenght: "+str(self.shower_lenght))
        if self.state >= 37 and self.state <= 39:
        #    print("Estabilizando a temperatura")
        #    print("Current: "+str(self.state))
            reward = 1
        else:
            reward = -1

        if self.shower_lenght <= 0:
        #    print("banho finalizado, retornando")
            done = True
        else:
            done = False

        self.state += random.randint(-1, 1)

        info = {}

        return self.state, reward, done, info

    def reset(self):
        self.state = 38 + random.randint(-3,3)
        self.shower_lenght = 60
        return self.state

    def render(slef, mode='human'):

        if mode == 'human':
            plt.imshow(np.asarray(im))
            plt.axis('off')
        elif mode == 'rgb_array':
            return np.asarray(im)
