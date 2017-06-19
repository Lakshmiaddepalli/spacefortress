import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)),"../"))

import ssf
import ssf.gym

import cv2
import numpy as np

if __name__ == '__main__':
    env = ssf.gym.SSF_Env(gametype="explode", scale=.25)
    state = env.reset()
    out = cv2.VideoWriter("gym.avi" ,cv2.VideoWriter_fourcc(*"H264"), env.metadata['video.frames_per_second'], (env.w,env.h))
    out.write(state)
    done = False
    while not done:
        action = env.action_space.sample()
        state, r, done, _ = env.step(action)
        out.write(state)
    out.release()
    cv2.destroyAllWindows()