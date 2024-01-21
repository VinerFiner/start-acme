# -*- coding: utf-8 -*-

import logging
import os
import json
import alibabacloud_fc.manage as mannge

# 初始化
def init_invoke():
    print("FC Initialize Start RequestId:")
    # do your things
    # if not os.path.exists("/mnt/auto/acmenas"):
    #     # 下载仓库
    #     os.system(
    #         "git clone https://github.com/acmesh-official/acme.sh.git")
    #     # 装载
    #     os.system(
    #         "cd acme.sh && bash acme.sh --install  \
    #         --home /mnt/auto/acmenas \
    #         --accountemail  \"my@example.com\" \
    #         --nocron")
    if not os.path.exists("/mnt/auto/nginx"):
        # 证书输出位置
        os.system("mkdir -p /mnt/auto/nginx")
    print("FC Initialize End RequestId:")

# 颁发证书
def invoke_acme(domain):
    print(domain)
    # 获取 DNS 平台, 默认 dns_ali
    if "DNS_TYPE" in os.environ:
        dnstype = os.environ['DNS_TYPE']
    else:
        dnstype = "dns_ali"
        # 设置域名服务器环境变量
        # os.environ["Ali_Key"]=''
        # os.environ["Ali_Secret"]=''
    issuestring = "acmenas/acme.sh \
            --issue \
            --server letsencrypt \
            --dns {0} \
            -d {1} \
            -k 2048"
    print(issuestring.format(dnstype, domain))
    # 颁发证书
    os.system(issuestring.format(dnstype, domain))
    installstring = "acmenas/acme.sh \
        --install-cert \
        -d {0} \
        --key-file /mnt/auto/nginx/{1}_key.pem  \
        --fullchain-file /mnt/auto/nginx/{2}_cert.pem \
        "
    print(installstring.format(domain, domain, domain))
    # 导出证书
    os.system(installstring.format(domain, domain, domain))
    # 证书信息
    with open(os.path.join('/mnt/auto/nginx', '{0}_key.pem'.format(domain))) as keyfile:
        key = keyfile.read()
        keyfile.close()
    with open(os.path.join('/mnt/auto/nginx', '{0}_cert.pem'.format(domain))) as certfile:
        cert = certfile.read()
        certfile.close()
    acmedic = {
        "key": str(key),
        "cert": str(cert)
    }
    return acmedic

def handler(event, context):
    logger = logging.getLogger()
    logger.info(event)
    if type(event):
        evt = json.loads(event)
        payload = evt.get("payload")
        if payload is not None:
            json_payload=json.loads(payload)
    # 获取 domain
    function_name = json_payload.get("function")
    domain_name = json_payload.get("domain")
    region = json_payload.get("region")

    # 初始化
    init_invoke()

    # 颁发证书
    acmedic = invoke_acme(domain=domain_name)
    
    # 配置云函数证书
    accountId = os.environ.get('ALICLOUD_ACCOUNT_ID')
    keyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID')
    keySecret = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET')
    mannge.Manage.config_domain([accountId, keyId, keySecret, function_name, domain_name], dicts=acmedic, region=region)
    return event
