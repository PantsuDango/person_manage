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


#### 获取验证码图片

##### 简要描述

- 获取验证码图片

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "GetValidateCode"
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
    "Data": "data:image/jpeg;base64,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",
    "Message": "Success",
    "RequestId": "648020b5-c9f7-4ed1-b220-1f25bd7f6b47"
}
```