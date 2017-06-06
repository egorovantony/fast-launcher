#! /usr/bin/python3

import sys
import json as js
import os
import subprocess
import defClass as cls
import baseFunc as func

APP_GROUP_FILE = "app_group.json"
APP_FILE = "app.json"

env = cls.Env()
env.apps = func.getAppList()
env.appsGr = func.getAppGroupList()



apps = []
appGr = cls.AppGroup()
appGr.name = '1'
app = cls.App()
app.name = '1'
app.path = 'myNewPath'
apps.append(app)
app = cls.App()
app.name = '2'
app.path = 'myNewPath12'
apps.append(app)
appGr.apps = apps
with open('apps.txt', 'w') as appsfile:
    js.dump(appGr, appsfile, cls=cls.CustEncoder)

json_data=open('apps.txt').read()

data = js.loads(json_data, cls=cls.CustDecoder)
print(data['appGr'])
# appsStore = []
# for dat in data:
#     appsStore.append(cls.App(**dat))

print('hello')





while False:
    inp = input("Input command: ")

    if inp == '':
        print("Command not input")
        continue

    if inp == 'exit':
        sys.exit()

    func.exec(inp, env)

# Read file

#subprocess.Popen(["/opt/WebStorm/bin/webstorm.sh","%f"])
#print os.getcwd()

