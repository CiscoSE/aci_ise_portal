"""
Copyright (c) 2018 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""
from jinja2 import Environment
from jinja2 import FileSystemLoader
import os
import requests
from . import db
from .. import envs

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
JSON_TEMPLATES = Environment(loader=FileSystemLoader(DIR_PATH + '/json_templates'))
# Disable warnings
requests.packages.urllib3.disable_warnings()

class ApicController:




    """
    dbsettings = db.getLastSettings('id')
    username = dbsettings.apicUsername
    password = dbsettings.apicPassword
    url = dbsettings.apicUrl

    """

    token = ""

    def __init__(self):
        dbsettings = db.getFirstSettings()
        if dbsettings == None:
            self.username = dbsettings.apicUsername
            self.password = dbsettings.apicPassword
            self.url = dbsettings.apicUrl
            self.token = ""
        else:
            self.username = dbsettings.apicUsername
            self.password = dbsettings.apicPassword
            self.url = dbsettings.apicUrl

        self.token = self.get_token(self.username, self.password)

    def get_token(self, username, password):
        """
        Returns authentication token
        :param url:
        :param username:
        :param password:
        :return:
        """
        template = JSON_TEMPLATES.get_template('login.j2.json')
        payload = template.render(username=username, password=password)
        auth = self.makeCall(p_url='/api/aaaLogin.json', data=payload, method="POST").json()
        login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
        return login_attributes['token']

    def makeCall(self, p_url, method, data=""):
        """
        Basic method to make a call. Please this one to all the calls that you want to make
        :param p_url: APIC URL
        :param method: POST/GET
        :param data: Payload that you want to send
        :return:
        """
        cookies = {'APIC-Cookie': self.token}
        if method == "POST":
            response = requests.post(self.url + p_url, data=data, cookies=cookies, verify=False)
        elif method == "GET":
            response = requests.get(self.url + p_url, cookies=cookies, verify=False)
        if 199 < response.status_code < 300:
            return response
        else:
            error_message = json.loads(response.text)['imdata'][0]['error']['attributes']['text']
            if error_message.endswith("already exists."):
                return None
            elif error_message.endswith("unavailable)"):
                return None
            else:
                raise Exception(error_message)

    def getPods(self):
        pods = self.makeCall(p_url='/api/node/class/fabricPod.json', method="GET").json()['imdata']
        return pods

    def getTenants(self, query_filter=""):
        query_strings = "?order-by=fvTenant.name|asc"
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        tenants = self.makeCall(
            p_url='/api/node/class/fvTenant.json' + query_strings,
            method="GET").json()['imdata']
        return tenants

    def getAppProfiles(self, tenant_dn, query_filter=""):
        query_strings = '?order-by=fvAp.name|asc&query-target=subtree&target-subtree-class=fvAp'
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        aps = self.makeCall(
            p_url='/api/node/mo/' + tenant_dn + '.json' + query_strings,
            method="GET").json()['imdata']
        return aps

    def getEPGs(self, ap_dn, query_filter=""):
        query_strings = "?query-target=children&target-subtree-class=fvAEPg&order-by=fvAEPg.name"
        if query_filter != '':
            query_strings += '&query-target-filter=' + query_filter
        epgs = self.makeCall(
            p_url='/api/node/mo/' + ap_dn + '.json' + query_strings,
            method="GET").json()['imdata']
        return epgs

    def getLeafs(self, pod_dn):
        print(pod_dn)
        switches = self.makeCall(
            p_url='/api/node/mo/' + pod_dn + '.json?query-target=children&target-subtree-class=fabricNode&query-target-filter=and(eq(fabricNode.role,"leaf"))',
            method="GET").json()['imdata']
        return switches

    def getLeafMgmtIp(self, leaf_dn):
        print(leaf_dn)
        leafip = self.makeCall(
            p_url='/api/node/mo/' + leaf_dn + '/sys/ipv4/inst/dom-management/if-[mgmt0].json?query-target=children&target-subtree-class=ipv4Addr',
            method="GET").json()['imdata']
        return leafip





