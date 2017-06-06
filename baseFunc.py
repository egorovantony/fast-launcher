#! /usr/bin/python3

import defClass as cls

def getAppList():
    print("hello")

def getAppGroupList():
    print("hello")

def printAppList(apps):
    for app in apps:
        print(app.name + ' ' + app.path)

def printAppGroupList(appsGroup):
    for appGroup in appsGroup:
        print(appGroup.name)
        for app in appGroup.apps:
            print(app.name + ' ' + app.path)

def exec(instr, env):
    error = 'Error input command!!!'
    pos = instr.find(' ')
    if pos < 0:
        print(error)
        return

    command = instr[0:pos]
    inInstr = instr[pos+1:len(instr)]

    if command == 'app':
        app = parsingApp(inInstr)
        if app == 'err':
            print(error)
            return
        env.apps.append(app)

    if command == 'agr':
        agr = parsingAgr(inInstr)
        if agr == 'err':
            print(error)
            return
        env.appsGr.append(agr)

    if command == 'a2gr':
        return False
    if command == 'oapp':
        printAppList(env.apps)
    if command == 'oagr':
        printAppGroupList(env.appsGr)
    if command == 'dapp':
        return False
    if command == 'dagr':
        return False
    if command == "save":
        saveData(env)
    if command == 'run':
        return False
    if command == 'kill':
        return False


    print('Error, nonexist command!!!')

def parsingApp(str):
    arrStr = str.split(' ')
    if len(arrStr) != 2:
        return 'err'
    app = cls.App()
    app.name = arrStr[0]
    app.path = arrStr[1]
    return app

def parsingAgr(str):
    agr = cls.AppGroup()
    agr.name = str
    return agr;

def saveData(env):
    return False