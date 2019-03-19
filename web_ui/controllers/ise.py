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
import base64
from .. import envs
from . import db

DIR_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
JSON_TEMPLATES = Environment(loader=FileSystemLoader(DIR_PATH + '/json_templates'))
# Disable warnings
requests.packages.urllib3.disable_warnings()

class IseController:

    """
    url = envs.get_ise_url()
    dbsettings = db.getLastSettings('id')
    url = dbsettings.iseUrl
    credentials = dbsettings.iseUsername + ":" + dbsettings.isePassword
    """


    def makeCall(self, p_url, method, data="", headers={}):
        """
        Single exit point for all APIs calls for Prime Infrastructure
        :param p_url:
        :param method:
        :param data:
        :return:
        """
        dbsettings = db.getFirstSettings()
        if dbsettings == None:
            self.url = dbsettings.iseUrl
            self.credentials = dbsettings.iseUsername + ":" + dbsettings.isePassword
        else:
            self.url = dbsettings.iseUrl
            self.credentials = dbsettings.iseUsername + ":" + dbsettings.isePassword
        #credentials = envs.get_ise_username() + ":" + envs.get_ise_password()


        print (self.url)
        headers["Authorization"] = "Basic " + base64.b64encode(bytes(self.credentials, "utf-8")).decode("utf-8")
        headers["Content-Type"] = "application/json"
        headers["Accept"] = "application/json"

        if method == "POST":
            response = requests.post(self.url + p_url, data=data, headers=headers, verify=False)
        elif method == "GET":
            response = requests.get(self.url + p_url, headers=headers, verify=False)
        else:
            raise Exception("Method " + method + " not supported by this controller")
        if 199 > response.status_code > 300:
            errorMessage = json.loads(response.text)["errorDocument"]["message"]
            raise Exception("Error: status code" + str(response.status_code) + " - " + errorMessage)
        return response


    def getEndPointIdentityGroup(self):
        """

        :return:
        """
        pURL = "/ers/config/endpointgroup"
        EPname = self.makeCall(p_url=pURL, method="GET").json()['SearchResult']['resources']
        return EPname

    def getAuthorizationProfile(self):
        """

        :return:
        """
        pURL = "/ers/config/authorizationprofile"
        AuthP = self.makeCall(p_url=pURL, method="GET").json()['SearchResult']['resources']
        return AuthP

    def createEndPointIdentityGroup(self, name, description):
        """

        :return:
        """
        pURL = "/ers/config/endpointgroup"
        method = "POST"
        template = JSON_TEMPLATES.get_template('endpointgroup.j2.json')
        payload = template.render(endpoint_name=name, endpoint_description=description)
        self.makeCall(p_url=pURL, method=method, data=payload)

    def createAuthorizationProfile(self, apname, apictenant, apicap, apicepg, vlan):
        """

        :return:
        """
        pURL = "/ers/config/authorizationprofile"
        method = "POST"
        template = JSON_TEMPLATES.get_template('authorizationprofile.j2.json')
        payload = template.render(ap_name=apname, apic_tenant=apictenant, apic_ap=apicap, apic_epg=apicepg, vlanid=vlan)
        self.makeCall(p_url=pURL, method=method, data=payload)


    def createEndPoint(self, mac, endpointgroup_id):
        """

        :return:
        """
        pURL = "/ers/config/endpoint"
        method = "POST"
        template = JSON_TEMPLATES.get_template('endpoint.j2.json')
        payload = template.render(macadd=mac, endpointgroupid=endpointgroup_id)
        self.makeCall(p_url=pURL, method=method, data=payload)

    def createNetworkDevice(self, name, leaf_ip):
        """

        :return:
        """
        dbsettings = db.getLastSettings('id')
        shared_secret = dbsettings.apicSharedSecret
        pURL = "/ers/config/networkdevice"
        method = "POST"
        template = JSON_TEMPLATES.get_template('networkdevice.j2.json')
        payload = template.render(leafname=name, sharedsecret=shared_secret, leafip=leaf_ip)
        self.makeCall(p_url=pURL, method=method, data=payload)



