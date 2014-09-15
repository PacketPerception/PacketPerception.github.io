Title: 
Date: 2014-14-03 22:45
Category: git azure Random

Authenticating GitLab to Office 365
###################################

:date: 2014-14-03 22:45
:modified: 2014-14-03 22:45
:tags: git, azure, gitlab, office 365, oauth
:category: Random
:slug: gitlan-auth-azure
:authors: Brian Knobbs
:summary: Setting up GitLab to authenticate to Office 365


Requires
========

* Access to domain you want to authenticate to in https://manage.windowsazure.com/
* GitLab installed and setup (we're using the omnibus install)
    chown -R git:git /opt/gitlab


Create a new Application in Azure
=================================

http://stackoverflow.com/questions/22666233/get-started-with-office-365-rest-api

https://www.paydici.com/blog/omniauth-and-windows-azure


Install omniauth-wsfed
===========================

* ``cd /opt/gitlab/embedded/gitlab-rails/``
* Add ``gem "omniauth-wsfed"`` to Gemfile

.. note:: Need build-essential and cmake on Ubuntu
* ``sudo -u git -H ../../bin/bundle install --without development test mysql --path vendor/bundle --no-deployment``


Configure omniauth-wsfed
========================

.. code:: ruby
  :issuer_name => "<EntityDescriptor - entityID>",
  :issuer      => "<EntityDescriptor/RoleDescriptor/fed:SecurityTokenServiceEndpoint/EndpointReference/Address>",
  :realm       => "<APP ID URL from Azure App configuration>",
  :reply       => "<REPLY URL from Azure App configuration>",
  :id_claim    => "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name",
  :idp_cert    => "<EntityDescriptor/RoleDescriptor/KeyDescriptor/KeyInfo/x509Data/x509Certificate>"
