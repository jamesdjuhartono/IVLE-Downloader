import os
import config
import auth
import modules
import workbin


def setup():
    if not os.path.exists(config.credentialdir):
        os.makedirs(config.credentialdir)

    if not os.path.exists(config.authfile):
        with open(config.authfile, 'w') as fi:
            fi.write('{"Token": "NULL"}') #init of empty token

if __name__ == '__main__':
    
    setup()
    token = auth.authenticate()
    modules = modules.getModules(token)
    workbin.getFiles(modules, token)
