#### 获取公钥

##### 简要描述

- 获取公钥

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "GetPublicKey"
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCmvJEKmwkLN8A02rRw84uWp4PJDlYP52rJuXniWsxNw5a9LRt/Ni3SiCUyOaYLeXHxmP0Bfzbw6D9sGeYKsXjKVdGiKIwqP04ajJ6dzJl/HjYbX3N3iqc/EkNOrjpnnz7SHm7MKx1NXASWOhioydHFj6JvD8tz8ajiS8Iji+A8TQIDAQAB",
    "Message": "Success",
    "RequestId": "33191dd9-d31f-4d08-aff3-8e886c5e4dab"
}
```