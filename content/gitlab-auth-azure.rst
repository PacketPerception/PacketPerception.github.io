===================================
Authenticating GitLab to Office 365
===================================

:date: 2014-09-15 21:00
:modified: 2014-09-15 21:00
:tags: git, azure, gitlab, office 365, oauth
:category: Random
:slug: gitlab-auth-azure
:authors: Brian Knobbs
:summary: Setting up GitLab to authenticate to Office 365


Quick and dirty guide on configuring `GitLab <https://about.gitlab.com/>`_ to authenticate against
Microsoft's Office 365. Office 365 will create an Azure Active Directory server to manage users,
and we can use that AD server to authenticate using OAUTH2.0. 


Requires
--------

- Access to domain you want to authenticate to in the Azure Management Portal
  (https://manage.windowsazure.com/)

.. note:: 
    :class: bs-callout bs-callout-info

    You can use your 30-day trial to set this up without paying for Azure

- GitLab installed and setup (we're specifically using the omnibus install for this guide, but
  should easily adapt to manual installations)

.. note:: 
    :class: bs-callout bs-callout-info

    Make sure the permissions were set correctly for */opt/gitlab*; ``chown -R git:git /opt/gitlab``


Create a new Application in Azure
---------------------------------

- Log into `Azure Management Portal <https://manage.windowsazure.com/>`_
- Go to *Active Directory* -> *Applications* and click *ADD* at the bottom
- Select *Add an application my organization is developing*
- Name (GitLab), select *WEB APPLICATION AND/OR WEB API*
- Enter the URL for your GitLab installation (e.g. https://mygitlab.mycorp.org/)
- Enter a Microsoft endpoint URL for APP ID (e.g. https://mycorp.onmicrosoft.com/mygitlab) 
  # doesn't really matter, we wont use it, just have to be unique
- Go to the *Configuration* page for the Application you just added
- Take note of the *CLIENT ID* that will be used as the *client_id* below
- Create a new key by selecting a duration. *Make sure to copy down the value generated immediately
  as you will not be able to access it after leaving the page*. This key will be the
  *client_secret* below
- Ensure that under *permissions to other applications*, *Windows Azure Active Directory* as the
  *Enable sign-on and read users' profiles* permission selected
- Add a *REPLY URL* in the form of *https://mygitlab.mycorp.org/users/auth/azure_oauth2/callback*,
  replacing *mygitlab.mycorp.org* with the correct value
- Save your changes, then click the *VIEW ENDPOINTS* button at the bottom
- Note the OAUTH2.0 endpoints, they will look like
  *https://login.windows.net/<TENANT ID>/oauth2/token?api-version=1.0*. Copy down the value you
  have for the *<TENANT ID>* part of the URL, this will be used below

.. note::
    :class: bs-callout bs-callout-info

    Some useful links for setting this up

    http://stackoverflow.com/questions/22666233/get-started-with-office-365-rest-api
    https://www.paydici.com/blog/omniauth-and-windows-azure


Install omniauth-azure-auth2
----------------------------

- ``cd /opt/gitlab/embedded/gitlab-rails/``
- Add ``gem "omniauth-azure-auth2"`` to Gemfile

.. note:: 
    :class: bs-callout bs-callout-info

    Need build-essential, pkg-config and cmake on Ubuntu

- ``sudo -u git -H ../../bin/bundle install --without development test mysql --path vendor/bundle --no-deployment``

Configure omniauth-azure-auth2
------------------------------

Edit */etc/gitlab/gitlab.rb*, adding the following:

.. code:: yaml

    gitlab_rails['omniauth_enabled'] = true
    gitlab_rails['omniauth_allow_single_sign_on'] = true
    gitlab_rails['omniauth_providers'] = [
      { name: "azure_oauth2",
        args: {
          client_id: "<CLIENT ID from the newly configured app>",
          client_secret: "<Key value that you generated>",
          tenant_id: "<TENANT ID that you found above>"
        }
      }
    ]


Reconfigure gitlab
------------------

``gitlab-ctl reconfigure``


Log in
------

You should now have a *Sign in with: Azure Oauth2* button on the login screen. If you're already
logged into the Office 365 portal, you can click this for SSO. Otherwise, you can log in by
specifying *user@mycorp.org* and the Office 365 password and clicking *Sign in*. This will
automatically create a user account if the authentication was successful. The user's name will
probably have to be updated which can be done by the user after they've logged in by editing their
profile.
