from agent.agent import Agents
from common.rollout import Evaluator
from common.arguments import get_evaluate_args
import matplotlib.pyplot as plt
from tqdm import tqdm, trange
import numpy as np


class Degre_evaluator(Evaluator):
    def __init__(self, env, args):
        super().__init__(env, Agents(args), args.episode_limit)
        self.evaluate_epoch = args.evaluate_epoch
        self.evaluate_task = args.evaluate_task

    def evaluate_process(self):
        epoch_rewards = []
        epoch_steps = []
        epoch_success = []
        health= np.zeros((self.evaluate_epoch,env.width,env.length))
        for epoch in trange(self.evaluate_epoch):
            # print(self.env.routing_manager.m_health)
            health[epoch]=self.env.routing_manager.m_health
            rewards, steps, _, success = self.evaluate(self.evaluate_task)
            epoch_rewards.append(rewards)
            epoch_steps.append(steps)
            epoch_success.append(success)
        return epoch_rewards, epoch_steps, epoch_success, health


if __name__ == '__main__':
    args, ENV = get_evaluate_args()
    # args.evaluate_task = 20
    t_rewads = []
    t_steps = []
    t_succe = []
    health = []
    np.random.seed(1)
    path = 'DegreData' + '/' + '{}by{}-{}d{}b{}heal'.format(
        args.width, args.length, args.drop_num, args.block_num, args.heal_init) + '/'
    import os

    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(1):
        env = ENV(args.width, args.length, args.drop_num, n_blocks=args.block_num, fov=args.fov, stall=args.stall,
                  b_degrade=True, per_degrade=args.per_degrade, isTrain=False)
        args.__dict__.update(env.get_env_info())
        Eva = Degre_evaluator(env, args)
        rewards, steps, success, healthy = Eva.evaluate_process()
        t_steps.append(steps)
        t_succe.append(success)
        t_rewads.append(rewards)
        health.append(healthy)
        health = np.asanyarray(health)
        np.save(path + 'rewards.npy', t_rewads)
        np.save(path + 'steps.npy', t_steps)
        np.save(path + 'success.npy', t_succe)
        np.save(path+'health.npy', health)
