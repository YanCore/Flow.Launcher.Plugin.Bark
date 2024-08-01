# -*- coding: utf-8 -*-

import copy
from typing import List

from flowlauncher import FlowLauncher

from plugin.templates import *
import requests
import webbrowser

class Main(FlowLauncher):
    messages_queue = []

    def sendNormalMess(self, title: str, subtitle: str):
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

        self.messages_queue.append(message)

    def sendActionMess(self, title: str, subtitle: str, method: str, value: List):
        # information
        message = copy.deepcopy(RESULT_TEMPLATE)
        message["Title"] = title
        message["SubTitle"] = subtitle

        # action
        action = copy.deepcopy(ACTION_TEMPLATE)
        action["JsonRPCAction"]["method"] = method
        action["JsonRPCAction"]["parameters"] = value
        message.update(action)

        self.messages_queue.append(message)

    def query(self, param: str) -> List[dict]:
        query = q = param.strip()
        self.sendActionMess(
            title="Hello World, this is where title goes. {}".format(('Your query is: ' + query , query)[query == '']),
            subtitle="This is where your subtitle goes, press enter to open Flow's url",
            method="open_url",
            value=["https://github.com/Flow-Launcher/Flow.Launcher"],
        )
        
        return self.messages_queue
        
    def open_url(self, url):
        webbrowser.open(url)