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

Main access for environmental variables. You will need to restart the app to apply those changes

"""

import os

__author__ = "Jason Mah (jamah@cisco.com)"



def get_ise_url():
    return os.getenv("ISE_URL", "")

def get_ise_username():
    return os.getenv("ISE_USER", "")

def get_ise_password():
    return os.getenv("ISE_PASSWORD", "")

def get_ise_shared_secret():
    return os.getenv("ISE_SHARED_SECRET", "")

def get_ise_fqdn():
    return os.getenv("ISE_FQDN", "")

def get_ise_subscriber_name():
    return os.getenv("ISE_SUBSCRIBER_NAME", "")

def get_ise_credentials():
    return os.getenv("ISE_CREDENTIALS", "")

def get_apic_url():
    return os.getenv("APIC_URL", "")

def get_apic_username():
    return os.getenv("APIC_USER", "")

def get_apic_password():
    return os.getenv("APIC_PASSWORD", "")