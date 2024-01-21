# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys

from typing import List

from alibabacloud_fc20230330.client import Client as FC20230330Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_fc20230330 import models as fc20230330_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class Manage:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        account_id: str,
        access_key_id: str,
        access_key_secret: str,
        region: str
    ) -> FC20230330Client:
        """
        Initialize the Client with the AccessKey of the account
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # Required, your AccessKey ID,
            access_key_id=access_key_id,
            # Required, your AccessKey secret,
            access_key_secret=access_key_secret
        )
        # See https://api.alibabacloud.com/product/FC.
        config.endpoint = f'{account_id}.{region}.fc.aliyuncs.com'
        return FC20230330Client(config)
    
# 配置 domain
    @staticmethod
    def config_domain(
        args: List[str],
        dicts: dict(),
        region: str
    ) -> None:
        accountId = args[0]
        keyId = args[1]
        keySecret = args[2]
        function_name = args[3]
        domain_name = args[4]
        key=dicts['key']
        cert=dicts['cert']
        # Please ensure that the environment variables ALIBABA_CLOUD_ACCESS_KEY_ID and ALIBABA_CLOUD_ACCESS_KEY_SECRET are set.
        # The project code leakage may result in the leakage of AccessKey, posing a threat to the security of all resources under the account. The following code example is called by using the environment variable to obtain the AccessKey, for reference only. It is recommended to use the more secure STS credential. For more credentials, please refer to: https://www.alibabacloud.com/help/en/alibaba-cloud-sdk-262060/latest/configure-credentials-378659
        client = Manage.create_client(accountId , keyId, keySecret, region)
        update_custom_domain_input_route_config_path_config_0 = fc20230330_models.PathConfig(
            function_name=function_name,
            methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH'],
            path='/*'
        )
        update_custom_domain_input_route_config = fc20230330_models.RouteConfig(
            routes=[
                update_custom_domain_input_route_config_path_config_0
            ]
        )
        update_custom_domain_input_cert_config = fc20230330_models.CertConfig(
            cert_name=domain_name.replace('.', '_'),
            private_key=key,
            certificate=cert
        )
        update_custom_domain_input = fc20230330_models.UpdateCustomDomainInput(
            cert_config=update_custom_domain_input_cert_config,
            route_config=update_custom_domain_input_route_config,
            # 这里可以只允许 HTTPS,'HTTP,HTTPS'
            protocol='HTTPS'
        )
        update_custom_domain_request = fc20230330_models.UpdateCustomDomainRequest(
            body=update_custom_domain_input
        )
        runtime = util_models.RuntimeOptions()
        headers = {}
        try:
            # Copy the code to run, please print the return value of the API by yourself.
            client.update_custom_domain_with_options(domain_name, update_custom_domain_request, headers, runtime)
        except Exception as error:
            # Print error if needed.
            UtilClient.assert_as_string(error)

# 这里只在脚本时候运行
if __name__ == '__main__':
    Manage.create_domain(sys.argv[1:])