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
from django.db import models

# Create your models here.
from django.db import models


class Settings(models.Model):
    apicUrl = models.CharField(max_length=100)
    apicUsername = models.CharField(max_length=50)
    apicPassword = models.CharField(max_length=50)
    apicSharedSecret = models.CharField(max_length=50)
    iseUrl = models.CharField(max_length=100)
    iseUsername = models.CharField(max_length=50)
    isePassword = models.CharField(max_length=50)
    iseFqdn = models.CharField(max_length=50)
    iseSubname = models.CharField(max_length=50)



