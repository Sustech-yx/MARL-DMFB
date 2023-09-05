import os

def config(name, version = None):
    if name == 'dmfb':
        os.chdir('data-dmfb/')
        if version == '0.1':
            from env.DMFB.dmfb import DMFBenv_v0_1
            return DMFBenv_v0_1
        elif version == "0.2":
            from env.DMFB.dmfb import DMFBenv_v0_2
            return DMFBenv_v0_2
        else:
            from env.DMFB.dmfb import DMFBenv
            return DMFBenv
    elif name == 'meda':
        os.chdir('data-meda/')
        if version == '0.1':
            from env.MEDA.meda import MEDAEnv_v0_1
            return MEDAEnv_v0_1
        if version == '0.2':
            from env.MEDA.meda import MEDAEnv_v0_2
            return MEDAEnv_v0_2