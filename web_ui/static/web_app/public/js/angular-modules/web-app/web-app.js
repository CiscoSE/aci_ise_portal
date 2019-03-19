/**
 * Angular JavaScript that controls the user interface interactions .
 * @module App module
 * @author Santiago Flores Kanter <sfloresk@cisco.com>
 * @copyright Copyright (c) 2018 Cisco and/or its affiliates.
 * @license Cisco Sample Code License, Version 1.0
 */

/**
 * @license
 * Copyright (c) 2018 Cisco and/or its affiliates.
 *
 * This software is licensed to you under the terms of the Cisco Sample
 * Code License, Version 1.0 (the "License"). You may obtain a copy of the
 * License at
 *
 *                https://developer.cisco.com/docs/licenses
 *
 * All use of the material herein must be in accordance with the terms of
 * the License. All rights not expressly granted by the License are
 * reserved. Unless required by applicable law or agreed to separately in
 * writing, software distributed under the License is distributed on an "AS
 * IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied.
 */
 /* Global variables */

var appModule = angular.module('appModule',['ngRoute','ngAnimate'])

/*  Configuration    */

// To avoid conflicts with other template tools such as Jinja2, all between {a a} will be managed by ansible instead of {{ }}
appModule.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);


// Application routing
appModule.config(function($routeProvider, $locationProvider){
    // Maps the URLs to the templates located in the server
    $routeProvider
        .when('/', {templateUrl: 'ng/home'})
        .when('/home', {templateUrl: 'ng/home'})
        .when('/macass', {templateUrl: 'ng/macass'})
        .when('/settings', {templateUrl: 'ng/settings'})
        .when('/netdevice', {templateUrl: 'ng/netdevice'})
        .when('/iseauth', {templateUrl: 'ng/iseauth'})
        .when('/iseendpoint', {templateUrl: 'ng/iseendpoint'})
    $locationProvider.html5Mode(true);
});




function property(){
    function parseString(input){
        return input.split(".");
    }

    function getValue(element, propertyArray){
        var value = element;

        _.forEach(propertyArray, function(property){
            value = value[property];
        });

        return value;
    }

    return function (array, propertyString, target){
        var properties = parseString(propertyString);

        return _.filter(array, function(item){
            return getValue(item, properties).toUpperCase().startsWith(target.toUpperCase());
        });
    }
}

appModule.filter('property', property);

/*  Controllers    */


// App controller is in charge of managing all services for the application
appModule.controller('AppController', function($scope, $location, $http, $window, $rootScope){

    $scope.error = ""
    $scope.success = ""
    $scope.loading = false;
    $scope.pods = [];
    $scope.tenants = [];
    $scope.deployment={selectedPod: ""};
    $scope.settings = {};
    $scope.newSettings = [];
    $scope.iseparameters = {};
    $scope.deployment.portType = "select";



    $scope.go = function ( path ) {
        $location.path( path );
    };

    $scope.clearError = function(){
        $scope.error = "";
    };
    $scope.clearSuccess = function(){
        $scope.success = "";
    };

    $scope.setPortType = function(portType){
        $scope.deployment.portType = portType;
    };

    $scope.getPods = function(){

        $scope.loading = true;
        // Does a GET call to api/pod to get the pod list
        $http
            .get('api/pod')
            .then(function (response, status, headers, config){
                // Save the data into the $scope.pods variable
                $scope.pods = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
            })
    };

    $scope.getPods();

    $scope.getTenants = function(){

        $scope.loading = true;
        // Does a GET call to api/pod to get the pod list
        $http
            .get('api/tenant')
            .then(function (response, status, headers, config){
                // Save the data into the $scope.pods variable
                $scope.tenants = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
            })
    };

    $scope.getTenants();


    $scope.getLeafDevices = function(pod){
        if(pod.fabricPod){
        // Does a GET call to api/switch to get the switches list
        $scope.loading = true;
        $http
            .get('api/iseleaf/' + pod.fabricPod.attributes.dn)
            .then(function (response, status, headers, config){
                    $scope.apicleafs = response.data

            })
            .catch(function(response, status, headers, config){
                    $scope.error = response.data.message
            })
            .finally(function(){
                    $scope.loading = false;
            })
        }
    };




    $scope.getAppPro = function(tenant){
        if(tenant.fvTenant){
            // Does a GET call to api/switch to get the switches list
            $scope.loading = true;
            $http
                .get('api/appprofile/' + tenant.fvTenant.attributes.dn)
                .then(function (response, status, headers, config){
                    $scope.apppros = response.data
                })
                .catch(function(response, status, headers, config){
                    $scope.error = response.data.message
                })
                .finally(function(){
                    $scope.loading = false;
                })
        }
    };


    $scope.getEPGs = function(apppro){
        if(apppro.fvAp){
        // Does a GET call to api/epgs to get the EPG/VLANs list
            $scope.loading = true;
            $http
                .get('api/epg/' + apppro.fvAp.attributes.dn)
                .then(function (response, status, headers, config){
                    $scope.epgs = response.data
                })
                .catch(function(response, status, headers, config){
                    $scope.error = response.data.message
                })
                .finally(function(){
                    $scope.loading = false;
                })
        }
    };

    $scope.getEndPointGroup = function(){

        $scope.loading = true;
        // Does a GET call to api/pod to get the pod list
        $http
            .get('api/endpointgroup')
            .then(function (response, status, headers, config){
                // Save the data into the $scope.pods variable
                $scope.endpointgroups = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
            })
    };

    $scope.getEndPointGroup();

    $scope.getAuthorizationProfile = function(){

        $scope.loading = true;
        // Does a GET call to api/pod to get the pod list
        $http
            .get('api/authprofile')
            .then(function (response, status, headers, config){
                // Save the data into the $scope.pods variable
                $scope.authprofiles = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
            })
    };

    $scope.getAuthorizationProfile();

    $scope.deploy = function(){
        $scope.loading = true;

        // Does a POST call to api/deploy to send the deployment information to the server for processing.
        $http
            .post('api/deploy', {'deployment': $scope.deployment })
            .then(function (response, status, headers, config){
                $scope.success = "Deployment done!"
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
                // After the deployment is done, refresh the EPGs/VLANs items
            })
    };

    $scope.getSettings = function(){
        $http
            .get('api/settings')
            .then(function (response, status, headers, config){

                $scope.settings = response.data

            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
            })
    };

    $scope.setSettings = function(){
        $http
            .post('api/settings',{'settings': $scope.settings })
            .then(function (response, status, headers, config){

                $scope.success = "Settings Updated"

            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
            })
    };

    $scope.isedeployeig = function(){
        $scope.loading = true;

        // Does a POST call to api/deploy to send the deployment information to the server for processing.
        $http
            .post('api/isedeployeig', {'iseparameters': $scope.iseparameters })
            .then(function (response, status, headers, config){
                $scope.success = "Deployment done!"
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
                // After the deployment is done, refresh the EPGs/VLANs items
            })
    };

    $scope.isedeployap = function(){
        $scope.loading = true;

        // Does a POST call to api/deploy to send the deployment information to the server for processing.
        $http
            .post('api/isedeployap', {'iseparameters': $scope.iseparameters })
            .then(function (response, status, headers, config){
                $scope.success = "Deployment done!"
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
                // After the deployment is done, refresh the EPGs/VLANs items
            })
    };

    $scope.isedeployleaf = function(){
        $scope.loading = true;

        // Does a POST call to api/deploy to send the deployment information to the server for processing.
        $http
            .post('api/isedeployleaf', {'deployment': $scope.deployment })
            .then(function (response, status, headers, config){
                $scope.success = "Deployment done!"
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
                // After the deployment is done, refresh the EPGs/VLANs items
            })
    };

});
