#!/bin/bash

# Copyright (c) 2018 Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.0 (the "License"). You may obtain a copy of the
# License at
#
#                https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.
#
# AUTHOR(s): Santiago Flores Kanter <sfloresk@cisco.com>, Jason Mah <jamah@cisco.com>

# Set up any db change
python /usr/src/app/manage.py makemigrations

# Updates/Creates Database
python /usr/src/app/manage.py migrate

# Starts server
python /usr/src/app/manage.py runserver 0.0.0.0:8080