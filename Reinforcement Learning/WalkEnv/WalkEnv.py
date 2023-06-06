from turtle import shape
from gym import Env, spaces
from gym.utils import seeding, colorize
import sys
from io import StringIO
import numpy as np
import time
import os
from IPython.display import clear_output
from IPython import get_ipython

from stable_baselines3 import PPO, DQN
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import *


def clear_console():
    if 'google.colab' in str(get_ipython()):
        clear_output()
    else:
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

ACTION_STOP  = 0
ACTION_LEFT  = 1
ACTION_RIGHT = 2

action_map ={
    "0" : "no_op",
    "1" : "left",
    "2" : "right"    
}

MAP = [
    "+-------------------+",
    "|S: : : : : : : : :E|",    
    "+-------------------+",
]

class WalkEnv(Env):
    
    metadata = {'render_modes': ['human', 'rgb_array']}

    def __init__(self):
        self.desc = np.asarray(MAP, dtype="c")
        self.action_space = spaces.Discrete(3)         
        self.shape = (1, 12)
        self.observation_space = spaces.Box(low=0, high=12, shape=self.shape , dtype=np.uint8)                
        self.cstep = -1
        self.time_steps = 0
        self.corridor = np.full(12, -1)
        self.laststep = 0      
        self.reward = 0
        self.action = 0 
        self.is_render = False
        self.corridor[len(self.corridor)-1] = self.time_steps
        self.corridor[len(self.corridor)-2] = 0
    
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]    

    def step(self, action):

        self.laststep = self.cstep

        reward = 0.0
        done = False
        self.time_steps += 1

        if (action == ACTION_STOP):
            reward = -50
        elif (action == ACTION_LEFT):
            self.cstep -= 1
            self.cstep = max(0, self.cstep)
            reward = -20             
        elif (action == ACTION_RIGHT):            
            self.cstep += 1
            self.cstep = min(self.cstep, 9)
            reward = 10

        self.corridor[self.laststep] = -1        
        self.corridor[self.cstep] = 10      
          
        self.corridor[len(self.corridor)-1] = self.time_steps
        self.corridor[len(self.corridor)-2] = action
        info = {"is_success" : False}
        
        if self.cstep >= 9:
            reward = 500
            done = True                                   
            info = {"is_success" : True}
        elif self.time_steps >= 300 and not done:
            done = True  
            reward = -200
            info = {"is_success" : False}    

        clear_console()

        self.reward = reward
        self.action = action        
        obs = np.reshape(self.corridor, self.shape)
        self.render()        

        return obs, reward, done, info

    def reset(self):        
        self.cstep = -1  
        self.laststep = 0      
        self.corridor = np.full(12, -1)           
        self.time_steps = 0
        self.corridor[0] = 10
        self.corridor[len(self.corridor)-1] = self.time_steps
        self.corridor[len(self.corridor)-2] = 0
        return np.reshape(self.corridor, self.shape) 

    def render(self, mode="human"):
        
        outfile = StringIO() if mode == "ansi" else sys.stdout

        out = self.desc.copy().tolist()
        out = [[c.decode("utf-8") for c in line] for line in out]

        def ul(x):
            return "_" if x == " " else x

        out[1][2 * self.cstep+1] = colorize(out[1][2 * self.cstep+1], "yellow", highlight=True)
        outfile.write("\n".join(["".join(row) for row in out]) + "\n")
        if self.action is not None:
            outfile.write(
                f"  ({['Stop', 'Left', 'Right'][self.action]}),({self.reward}),({self.cstep})\n"
            )
        else:
            outfile.write("\n")   

        #print(self.corridor, action_map[str(int(self.action))], self.action, self.reward, self.cstep, self.laststep)                
        return self.corridor

if __name__ == "__main__":
    
    #seed = 42    
    env = WalkEnv()   
    env = Monitor(env=env)
    #env.seed(seed)
    #set_random_seed(seed)
    
    model = PPO("MlpPolicy", env=env, verbose=1, n_steps=2048)    
    #model = DQN("MlpPolicy", env=env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("D:\ppo_walkenv")

    del model #excluir para demonstrar o carregamento do modelo
    
    #model = DQN.load("D:\ppo_walkenv")    
    model = PPO.load("D:\ppo_walkenv")
    
    env = WalkEnv()    
    env = Monitor(env=env)
    #env.seed(seed)
    success = 0
    for e in range(100):
        obs = env.reset()
        done = False           
        total_reward = 0 
        while not done:
            action, _states = model.predict(obs)
            obs, rewards, done, info = env.step(action)
            if info["is_success"]:
                success += 1

            #time.sleep(0.2)
            #env.render()    
            total_reward += rewards
        print('Total Reward for episode {} is {}'.format(e, total_reward))                
    print("Success {}".format(success))