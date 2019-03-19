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
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import traceback
from django.http import HttpResponse
from web_ui.controllers.apic import ApicController
from web_ui.controllers.ise import IseController
from web_ui.controllers import db
from django.core import serializers
from rest_framework.renderers import JSONRenderer



# ====================>>>>>>>> Utils <<<<<<<<====================
class ModelsJSONResponse(HttpResponse):
    """
    An HttpResponse that renders django models its content into JSON.
    """

    def __init__(self, data, **kwargs):
        jsonData = serializers.serialize("json", data)
        #        content = JSONRenderer().render(jsonData)
        kwargs['content_type'] = 'application/json'
        super(ModelsJSONResponse, self).__init__(jsonData, **kwargs)


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# ====================>>>>>>>> Templates <<<<<<<<====================

def index(request):
    return render(request, 'web_app/index.html')

def home(request):
    return render(request, 'web_app/home.html')

def mac_association(request):
    return render(request, 'web_app/mac_association.html')

def settings(request):
    return render(request, 'web_app/settings.html')

def network_devices(request):
    return render(request, 'web_app/network_devices.html')

def ise_authorization_profile(request):
    return render(request, 'web_app/ise_authorization_profile.html')

def ise_endpoint_group(request):
    return render(request, 'web_app/ise_endpoint_group.html')


# ====================>>>>>>>> APIs <<<<<<<<====================

@csrf_exempt
def api_pod(request):
    """
       Return a json list of pods
       :param request:
       :return:
    """
    if request.method == 'GET':
        try:
            # Create a new controller
            apic = ApicController()

            # Get the pods
            pods = apic.getPods()

            # Send pods to the web client
            return JSONResponse(pods)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_tenant(request):
    """
       Return a json list of tenants
       :param request:
       :return:
    """
    if request.method == 'GET':
        try:
            # Create a new controller
            apic = ApicController()

            # Get the pods
            tenants = apic.getTenants(query_filter="")

            # Send pods to the web client
            return JSONResponse(tenants)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_iseleaf(request):
    """
       Return a json list of tenants
       :param request:
       :return:
    """
    if request.method == 'GET':
        try:
            payload = json.loads(request.body)
            print(payload)
            # Create a new controller
            apic = ApicController()

            # Get the pods
            tenants = apic.getTenants(query_filter="")

            # Send pods to the web client
            return JSONResponse(tenants)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_appprofile(request, tenantDn):
    """
       Return a list of switches for a given pod
       :param request:
       :return:
       """
    if request.method == 'GET':
        try:
            # Create a new controller
            apic = ApicController()

            # Get the leaf switches for a given pod
            appprofiles = apic.getAppProfiles(tenant_dn=tenantDn)

            # Send the leaf switches to the web client
            return JSONResponse(appprofiles)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_iseleaf(request, podDn):
    """
       Return a list of switches for a given pod
       :param request:
       :return:
       """
    if request.method == 'GET':
        try:
            # Create a new controller
            apic = ApicController()

            # Get the leaf switches for a given pod
            apicleafs = apic.getLeafs(pod_dn=podDn)

            # Send the leaf switches to the web client
            return JSONResponse(apicleafs)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_epg(request, apDn):
    """
       Return a list of EPG for a given tenant
       :param request:
       :return:
   """
    if request.method == 'GET':
        try:
            # Create a new controller
            apic = ApicController()

            # Get all EPGs from the first application profile
            epgs = apic.getEPGs(ap_dn=apDn)

            # Send EPGs to web client
            return JSONResponse(epgs)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_endpointgroup(request):
    """
       Return a list of EPG for a given tenant
       :param request:
       :return:
    """
    if request.method == 'GET':
        try:
            # Create a new controller
            ise = IseController()

            # Get all EPGs from the first application profile
            endpointgroup = ise.getEndPointIdentityGroup()

            # Send EPGs to web client
            return JSONResponse(endpointgroup)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_authorizationprofile(request):
        """
           Return a list of EPG for a given tenant
           :param request:
           :return:
        """
        if request.method == 'GET':
            try:
                # Create a new controller
                ise = IseController()

                # Get all EPGs from the first application profile
                authprofile = ise.getAuthorizationProfile()

                # Send EPGs to web client
                return JSONResponse(authprofile)
            except Exception as e:
                print(traceback.print_exc())
                # return the error to web client
                return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
        else:
            # return the error to web client
            return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_deploy(request):
    """
       Return a list of EPG for a given tenant
       :param request:
       :return:
    """
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            print(payload)
            ise = IseController()
            apic = ApicController()
            if payload["deployment"]["portType"] == "select":
                print("inhere1")
                #leafs = apic.getLeafs(pod_dn=payload["deployment"]["selectedPod"]["fabricPod"]["attributes"]["dn"])
                #for leaf in leafs:
                    #leaf_name = leaf["fabricNode"]["attributes"]["id"]
                    #leaf_ip_parameters = apic.getLeafMgmtIp(leaf_dn=leaf["fabricNode"]["attributes"]["dn"])
                    #print(leaf_ip_parameters)

                    #for leaf_ip in leaf_ip_parameters:
                        #ise.createNetworkDevice(leaf_name, leaf_ip["ipv4Addr"]["attributes"]["addr"][:-3])

                ise.createEndPoint(mac=payload["deployment"]["selectedMac"], endpointgroup_id=payload["deployment"]["selectedEndpointgroup"]["id"])
                print("Deployment Done!")

            elif payload["deployment"]["portType"] == "add":
                print("inhere2")
                ise.createEndPointIdentityGroup(name=payload["deployment"]["selectedIseeig"],
                                                description=payload["deployment"]["selectedIseeigdescrip"])
                apic_tenant = payload["deployment"]["selectedTenant"]["fvTenant"]["attributes"]["dn"]
                apic_tenant_trim = apic_tenant[apic_tenant.find('tn-'):]
                apic_apppro = payload["deployment"]["selectedAppPro"]["fvAp"]["attributes"]["dn"]
                apic_apppro_trim = apic_apppro[apic_apppro.find('ap-'):]
                apic_epg = payload["deployment"]["selectedEpg"]["fvAEPg"]["attributes"]["dn"]
                apic_epg_trim = apic_epg[apic_epg.find('epg-'):]

                ise.createAuthorizationProfile(apname=payload["deployment"]["selectedIseap"],
                                               apictenant=apic_tenant_trim,
                                               apicap=apic_apppro_trim,
                                               apicepg=apic_epg_trim,
                                               vlan = payload["deployment"]["selectedIseapvlan"])

                print("Deployment Done!")

            # Reply ok to the web client
            return JSONResponse("ok")
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_settings(request):
    """
    Retreive (GET) or change (POST) the settings for this app.
    :param request:
    :return:
    """

    try:
        if request.method == 'GET':
            print("here")

            return JSONResponse("Ok")

        elif request.method == "POST":

            payload = json.loads(request.body)
            print(payload)
            dbsettings = db.getFirstSettings()
            if dbsettings == None:
                db.addSettings(apicUrl=payload["settings"]["apicurl"],
                           apicUsername=payload["settings"]["apicusername"],
                           apicPassword=payload["settings"]["apicpassword"],
                           apicSharedSecret=payload["settings"]["apicsharedsecret"],
                           iseUrl=payload["settings"]["iseurl"],
                           iseUsername=payload["settings"]["iseusername"],
                           isePassword=payload["settings"]["isepassword"],
                           iseFqdn=payload["settings"]["isefqdn"],
                           iseSubname=payload["settings"]["isesubname"])
            else:
                dbsettings.apicUrl = payload["settings"]["apicurl"]
                dbsettings.apicUsername = payload["settings"]["apicusername"]
                dbsettings.apicPassword = payload["settings"]["apicpassword"]
                dbsettings.apicSharedSecret = payload["settings"]["apicsharedsecret"]
                dbsettings.iseUrl = payload["settings"]["iseurl"]
                dbsettings.iseUsername = payload["settings"]["iseusername"]
                dbsettings.isePassword = payload["settings"]["isepassword"]
                dbsettings.iseFqdn = payload["settings"]["isefqdn"]
                dbsettings.iseSubname = payload["settings"]["isesubname"]
                dbsettings.save()


            #set = db.getLastSettings('id')
            #print(set.apicUrl)
            #print(set.apicSharedSecret)

            return JSONResponse("Ok")
        else:
            return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

    except Exception as e:
        print(traceback.print_exc())
        # return the error to web client
        return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)

@csrf_exempt
def api_isedeployeig(request):
        """
           Return a list of EPG for a given tenant
           :param request:
           :return:
        """
        if request.method == 'POST':
            try:
                payload = json.loads(request.body)
                print(payload)
                ise = IseController()
                ise.createEndPointIdentityGroup(name=payload["iseparameters"]["iseeig"],
                                                description=payload["iseparameters"]["iseeigdescrip"])
                print("Deployment Done!")

                # Reply ok to the web client
                return JSONResponse("ok")
            except Exception as e:
                print(traceback.print_exc())
                # return the error to web client
                return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
        else:
            # return the error to web client
            return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_isedeployap(request):
        """
           Return a list of EPG for a given tenant
           :param request:
           :return:
        """
        if request.method == 'POST':
            try:
                payload = json.loads(request.body)
                print(payload)
                ise = IseController()
                #ise.createEndPointIdentityGroup(payload[])
                print("Deployment Done!")

                # Reply ok to the web client
                return JSONResponse("ok")
            except Exception as e:
                print(traceback.print_exc())
                # return the error to web client
                return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
        else:
            # return the error to web client
            return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

@csrf_exempt
def api_isedeployleaf(request):
        """
           Return a list of EPG for a given tenant
           :param request:
           :return:
        """
        if request.method == 'POST':
            try:
                payload = json.loads(request.body)
                print(payload)
                # Create a new controller
                apic = ApicController()
                ise = IseController()

                # Get all EPGs from the first application profile
                leafs = apic.getLeafs(pod_dn=payload["deployment"]["selectedPod"]["fabricPod"]["attributes"]["dn"])
                for leaf in leafs:
                    leaf_name = leaf["fabricNode"]["attributes"]["id"]
                    leaf_ip_parameters = apic.getLeafMgmtIp(leaf_dn=leaf["fabricNode"]["attributes"]["dn"])
                    print(leaf_ip_parameters)

                    for leaf_ip in leaf_ip_parameters:
                        ise.createNetworkDevice(leaf_name, leaf_ip["ipv4Addr"]["attributes"]["addr"][:-3])

                # Send EPGs to web client
                return JSONResponse(leafs)
            except Exception as e:
                print(traceback.print_exc())
                # return the error to web client
                return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
        else:
            # return the error to web client
            return JSONResponse("Bad request. " + request.method + " is not supported", status=400)