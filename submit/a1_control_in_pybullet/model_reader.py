# coding=utf-8
# Copyright 2020 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0, parentdir)

import numpy as np
import tensorflow as tf


from motion_imitation.envs import env_builder as env_builder
from motion_imitation.learning import imitation_policies as imitation_policies
from motion_imitation.learning import ppo_imitation as ppo_imitation


TIMESTEPS_PER_ACTORBATCH = 4096
OPTIM_BATCHSIZE = 256

ENABLE_ENV_RANDOMIZER = True


def build_model(env, num_procs, timesteps_per_actorbatch, optim_batchsize, output_dir):
    policy_kwargs = {
        "net_arch": [{"pi": [512, 256], "vf": [512, 256]}],
        "act_fun": tf.nn.relu,
    }

    timesteps_per_actorbatch = int(np.ceil(float(timesteps_per_actorbatch) / num_procs))
    optim_batchsize = int(np.ceil(float(optim_batchsize) / num_procs))

    model = ppo_imitation.PPOImitation(
        policy=imitation_policies.ImitationPolicy,
        env=env,
        gamma=0.95,
        timesteps_per_actorbatch=timesteps_per_actorbatch,
        clip_param=0.2,
        optim_epochs=1,
        optim_stepsize=1e-5,
        optim_batchsize=optim_batchsize,
        lam=0.95,
        adam_epsilon=1e-5,
        schedule="constant",
        policy_kwargs=policy_kwargs,
        tensorboard_log=output_dir,
        verbose=1,
    )
    return model

def get_env(motion_file, enable_rendering=False):
    env = env_builder.build_a1_imitation_env(
        motion_files=[motion_file],
        num_parallel_envs=1,
        mode="test",
        enable_randomizer=False,
        enable_rendering=enable_rendering,
    )
    return env

# read model
def read_model(motion_file, model_file):

    env = get_env(motion_file)
    model = build_model(
        env=env,
        num_procs=1,
        timesteps_per_actorbatch=TIMESTEPS_PER_ACTORBATCH,
        optim_batchsize=OPTIM_BATCHSIZE,
        output_dir=None,
    )
    model.load_parameters(model_file)
    return model


def pybullet_env(motion_file, model_file):
    env = get_env(motion_file, True)
    model = read_model(motion_file, model_file)
    o = env.reset()
    dataStr = ""
    while True:
        a, _ = model.predict(o, deterministic=True)
        dataStr += ",".join(str(j) for j in a) + "\n"
        print(dataStr)
        with open("data.txt", "w") as f:
            f.write(dataStr)
        o, r, done, info = env.step(a)
        if done:
            o = env.reset()
            break
    return

def main():
    motion_file = "/home/sz/legged/legged_robot_sheffield/motion_imitation/data/motions/a1_pace.txt"
    model_file = "/home/sz/legged/legged_robot_sheffield/motion_imitation/data/policies/a1_pace.zip"
    pybullet_env(motion_file,model_file)
    return


if __name__ == "__main__":
    main()
