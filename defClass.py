#! /usr/bin/python3


import json

class AppGroup:
    @staticmethod
    def fromJson(**js):
        if 'appGr' in js:
            appGr = AppGroup()
            appGr.name = js['appGr']['name']
            appGr.apps = js['appGr']['apps']
            return appGr
        return None
    name = ''
    apps = []

class App:
    @staticmethod
    def fromJson(**js):
        if 'app' in js:
            app = App()
            app.name = js['app']['name']
            app.path = js['app']['path']
            return app
        return None
    name = ''
    path = ''

class Env:
    apps = []
    appsGr = []

class CustEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (list, dict, str, int, float, bool, type(None))):
            return super().default(obj)
        if isinstance(obj, App):
            return {'app': obj.__dict__}
        if isinstance(obj, AppGroup):
            return {'appGr': obj.__dict__}

class CustDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if 'appGr' in obj:
            return AppGroup.fromJson(**obj)
        if 'app' in obj:
            return App.fromJson(**obj)
        return obj

