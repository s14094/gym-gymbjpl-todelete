from gym.envs.registration import register

register(
    id='gymbjpl-v0',
    entry_point='gym_gymbjpl.envs:GymbjplEnv',
)