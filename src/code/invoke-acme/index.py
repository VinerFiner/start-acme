# coding=utf-8
import os
import json

def handler(event, context):
    evt = json.loads(event)
    payload = evt["payload"]
    print(payload)

    # 获取 DNS 平台, 默认 dns_ali
    if "DNS_TYPE" in os.environ:
        dnstype = os.environ['DNS_TYPE']
    else:
        dnstype = "dns_ali"
    # 设置域名服务器环境变量
    # os.environ["Ali_Key"]=''
    # os.environ["Ali_Secret"]=''
    issuestring = "/mnt/auto/acmenas/acme.sh \
            --issue \
            --server letsencrypt \
            --dns {0} \
            -d {1} \
            -k 2048"
    print(issuestring.format(dnstype, payload))
    # 颁发证书
    os.system(issuestring.format(dnstype, payload))

    installstring = "/mnt/auto/acmenas/acme.sh \
        --install-cert \
        -d {0} \
        --key-file /mnt/auto/nginx/{1}_key.pem  \
        --fullchain-file /mnt/auto/nginx/{2}_cert.pem \
        "
    print(installstring.format(payload, payload, payload))
    # 导出证书
    os.system(installstring.format(payload, payload, payload))

    return payload
