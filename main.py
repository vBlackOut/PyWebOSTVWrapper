from pywebostv.discovery import *    # Because I'm lazy, don't do this.
from pywebostv.connection import *
from pywebostv.controls import *
import os
import json

class TVControl():

    def __init__(self, ip):

        self.client = WebOSClient(ip)
        self.client.connect()

        if os.path.isfile('store.json'):
            with open("store.json") as jsonFile:
                store = json.load(jsonFile)
                jsonFile.close()
            self.store = store
        else:
            self.store = {}

        for status in self.client.register(self.store):
            if status == WebOSClient.PROMPTED:
                print("Please accept the connect on the TV!")
            elif status == WebOSClient.REGISTERED:
                print("Registration successful!")

        if os.path.isfile('store.json') == False:
            with open('store.json', 'w') as jsonFile:
                json.dump(store, jsonFile)
                jsonFile.close()

    def MediaControls(self, command):
        media = MediaControl(self.client)
        command = getattr(media, command)
        return command()

    def TvControls(self, command):
        tvcontrol = TvControl(self.client)
        command = getattr(tvcontrol, command)
        return command()

    def SourceControls(self, command, sources_input=0):
        source_control = SourceControl(self.client)

        if command == "list_sources":
            command = getattr(source_control, command)
            return command()

        elif command == "set_source":
            command = getattr(source_control, "list_sources")
            sources = command()
            return source_control.set_source(sources[sources_input])

    def InputControls(self, command, params={}):
        inp = InputControl(self.client)
        inp.connect_input()

        if command != "move" and command != "type" and command != "delete":
            command = getattr(inp, command)
            return command()

        elif command == "move":
            command = inp.move(params[0], params[1])

        elif command == "delete":
            command = inp.delete(params[0])

    def SystemControls(self, command, msg=""):
        system = SystemControl(self.client)

        if command == "notify":
            return system.notify(msg)
        else:
            command = getattr(system, command)
            return command()

tv = TVControl("192.168.1.196")
tv.MediaControls("volume_up")
tv.SourceControls("set_source", 0)
tv.InputControls("move", [100,100])
tv.SystemControls("info")
