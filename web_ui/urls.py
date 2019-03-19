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
"""
URL mapping of the application
"""

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index),

    # Angular mappings
    url(r'^home/?$', views.index),
    url(r'^macass/?$', views.index),
    url(r'^settings/?$', views.index),
    url(r'^netdevice/?$', views.index),
    url(r'^iseauth?$', views.index),
    url(r'^iseendpoint/?$', views.index),

    url(r'^ng/home/?$', views.home),
    url(r'^ng/macass/?$', views.mac_association),
    url(r'^ng/settings/?$', views.settings),
    url(r'^ng/netdevice/?$', views.network_devices),
    url(r'^ng/iseauth/?$', views.ise_authorization_profile),
    url(r'^ng/iseendpoint/?$', views.ise_endpoint_group),

    # APIs Mappings
    # Maps the URL web/api/pod to the method api_pod inside views.py
    url(r'^api/pod/?$', views.api_pod),
    # Maps the URL web/api/tenant to the method api_tenant inside views.py
    url(r'^api/tenant/?$', views.api_tenant),
    # Maps the URL web/api/switch/ to the method api_switch inside views.py
    url(r'^api/appprofile/(?P<tenantDn>.*)/?$', views.api_appprofile),
    # Maps the URL web/api/epg to the method api_epg inside views.py
    url(r'^api/epg/(?P<apDn>.*)?$', views.api_epg),
    # Maps the URL web/api/epg to the method api_epg inside views.py
    url(r'^api/endpointgroup/?$', views.api_endpointgroup),
    url(r'^api/authprofile/?$', views.api_authorizationprofile),
    url(r'^api/deploy/?$', views.api_deploy),
    url(r'^api/settings/?$', views.api_settings),
    url(r'^api/isedeployeig/?$', views.api_isedeployeig),
    url(r'^api/isedeployap/?$', views.api_isedeployap),
    url(r'^api/isedeployleaf/?$', views.api_isedeployleaf),
    url(r'^api/iseleaf/(?P<podDn>.*)/?$', views.api_iseleaf),

]
