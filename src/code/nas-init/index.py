# coding=utf-8
import os

def handler(event, context):
    if not os.path.exists("/mnt/auto/acmenas"):
        # 下载仓库
        os.system(
            "git clone https://github.com/acmesh-official/acme.sh.git")
        # 装载
        os.system(
            "cd acme.sh && bash acme.sh --install  \
            --home /mnt/auto/acmenas \
            --accountemail  \"my@example.com\" \
            --nocron")
    if not os.path.exists("/mnt/auto/nginx"):
        # 证书输出位置
        os.system("mkdir -p /mnt/auto/nginx")   
    return "nas init"
