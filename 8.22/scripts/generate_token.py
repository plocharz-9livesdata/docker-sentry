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

from sentry.models import ApiToken, User


def main():
    user = User.objects.filter(is_superuser=True)[0]  # Get any superuser
    values = ApiToken.scopes.values()
    super_key_flag_list = list(ApiToken.scopes.keys())

    super_key_value = 0
    for value in values:
        super_key_value |= value

    token = ApiToken.objects.create(
        user=user,
        scopes=super_key_value,
        scope_list=super_key_flag_list,
        refresh_token=None,
        expires_at=None,
    )
    token.save()
    print(token.token)


if __name__ == '__main__':
    main()
