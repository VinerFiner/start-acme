# 使用 acme 进行证书申请

- 下载并安装

```
git clone https://github.com/acmesh-official/acme.sh.git
cd acme.sh
./acme.sh --install  \
--home ~/myacme \
--config-home ~/myacme/data \
--cert-home  ~/mycerts \
--accountemail  "my@example.com" \
--accountkey  ~/myaccount.key \
--accountconf ~/myaccount.conf \
--useragent  "this is my client."
```

- 设置`dns_ali`环境变量，并颁发`dns_ali`证书

```
export Ali_Key="LTAI4Fd8J9qs4fxxxxxxxxxx"
export Ali_Secret="Xp3Z7NDOW0CJcPLKoUwqxxxxxxxxxx"
```

```
./acme.sh  \
  --issue \
  --server letsencrypt \
  --dns dns_ali \
  -d aaa.com \
  -d *.aaa.com \
  -d bbb.com \
  -d *.bbb.com \
  -d ccc.com \
  -d *.ccc.com \
  -k 2048
```

- 输出证书

```
./acme.sh  \
  --install-cert \
  -d aaa.com \
  -d *.aaa.com \
  --key-file /nginx/aaa_com.key  \
  --fullchain-file /nginx/aaa_com.pem
```

## 使用云函数部署

```
s deploy -t ./s.yaml -a fc-access --use-local -y
```
> 需要在 `invoke-acme` 函数配置 DNS 平台秘钥 https://www.ioiox.com/archives/87.html

> 我们需要在 定时触发器添加域名 `aaa.com`

> 我们也可以直接请求

```
curl -X POST -H "Content-type: application/json" -d "{\"domain\" : \"aaa.com\"}" "localhost:5000/invoke"
```