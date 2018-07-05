# ***********************************************************************************************************
#
#  Starfish Storage Corporation ("COMPANY") CONFIDENTIAL
#  Unpublished Copyright (c) 2011-2018 Starfish Storage Corporation, All Rights Reserved.
#
#  NOTICE:  All information contained herein is, and remains the property of COMPANY. The intellectual and
#  technical concepts contained herein are proprietary to COMPANY and may be covered by U.S. and Foreign
#  Patents, patents in process, and are protected by trade secret or copyright law. Dissemination of this
#  information or reproduction of this material is strictly forbidden unless prior written permission is
#  obtained from COMPANY.  Access to the source code contained herein is hereby forbidden to anyone except
#  current COMPANY employees, managers or contractors who have executed Confidentiality and Non-disclosure
#  agreements explicitly covering such access.
#
#  ANY REPRODUCTION, COPYING, MODIFICATION, DISTRIBUTION, PUBLIC  PERFORMANCE, OR PUBLIC DISPLAY OF OR
#  THROUGH USE  OF THIS  SOURCE CODE  WITHOUT  THE EXPRESS WRITTEN CONSENT OF COMPANY IS STRICTLY PROHIBITED,
#  AND IN VIOLATION OF APPLICABLE LAWS AND INTERNATIONAL TREATIES.  THE RECEIPT OR POSSESSION OF  THIS SOURCE
#  CODE AND/OR RELATED INFORMATION DOES NOT CONVEY OR IMPLY ANY RIGHTS TO REPRODUCE, DISCLOSE OR DISTRIBUTE
#  ITS CONTENTS, OR TO MANUFACTURE, USE, OR SELL ANYTHING THAT IT  MAY DESCRIBE, IN WHOLE OR IN PART.
#
#  FOR U.S. GOVERNMENT CUSTOMERS REGARDING THIS DOCUMENTATION/SOFTWARE
#    These notices shall be marked on any reproduction of this data, in whole or in part.
#    NOTICE: Notwithstanding any other lease or license that may pertain to, or accompany the delivery of,
#    this computer software, the rights of the Government regarding its use, reproduction and disclosure are
#    as set forth in Section 52.227-19 of the FARS Computer Software-Restricted Rights clause.
#    RESTRICTED RIGHTS NOTICE: Use, duplication, or disclosure by the Government is subject to the
#    restrictions as set forth in subparagraph (c)(1)(ii) of the Rights in Technical Data and Computer
#    Software clause at DFARS 52.227-7013.
#
# ***********************************************************************************************************
import requests
import six


# This is basic version of sfutils.api.sentry.SentryApi class, without dependencies from sfutils
class SentryApi(object):

    API_VERSION = '0'

    def __init__(self, sentry_api_key, url_prefix):
        self._url_prefix = url_prefix
        self._sentry_api_key = sentry_api_key
        self._organization_slug = 'sentry'
        self._team_slug = 'sentry'
        self._project_slug = 'starfish'

    def _post(self, *args, **kwargs):
        return requests.request("POST", verify=False, headers=self._headers(), *args, **kwargs)

    def _get(self, *args, **kwargs):
        return requests.request("GET", verify=False, headers=self._headers(), *args, **kwargs)

    def _headers(self):
        return {
            'Authorization': 'Bearer {token}'.format(token=self._sentry_api_key)
        }

    def _base_url(self):
        suffix = "api/{self.API_VERSION}/".format(self=self)
        return six.moves.urllib.parse.urljoin(self._url_prefix, suffix)

    def create_default_project(self):
        base_url = self._base_url()
        team_projects_url = base_url + "teams/{self._organization_slug}/{self._team_slug}/projects/".format(self=self)
        project_keys_url = base_url + "projects/{self._organization_slug}/{self._project_slug}/keys/".format(self=self)
        response = self._post(team_projects_url, data={'name': 'Starfish', 'slug': self._project_slug})
        response.raise_for_status()
        response = self._post(project_keys_url, data={'name': 'key'})
        response.raise_for_status()
        return response.json()
