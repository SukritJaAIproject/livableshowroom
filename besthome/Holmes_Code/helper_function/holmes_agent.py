import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Activation

from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory

actions = 3
states = (5,)

def convertdic(action_T):
  if action_T == 0:
    action_r = "down"
  elif action_T == 1:
    action_r = "Do nothing"
  else:
    action_r = "Up"
  return action_r

def build_model(states, actions):
  model = Sequential()
  model.add(Flatten(input_shape=(1,) + states))
  model.add(Dense(128))
  model.add(Activation('relu'))
  model.add(Dense(64))
  model.add(Activation('relu'))
  model.add(Dense(32))
  model.add(Activation('relu'))
  model.add(Dense(actions))
  model.add(Activation('linear'))
  return model

def build_agent(model, actions):
  policy = BoltzmannQPolicy()
  memory = SequentialMemory(limit=50000, window_length=1)
  dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions, nb_steps_warmup=10,target_model_update=1e-2)
  return dqn






