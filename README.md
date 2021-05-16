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


#### 用户登录

##### 简要描述

- 用户登录

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "Login",
    "ValidateCode": "7607",
    "UserName": "admin",
    "Password": "mB8yj9CXYuXm6qIwrDF8RAQmsCjwpYs0w24cvsHZ/a+IirR1is4GbqVHb7B0rG+hdATojKUk90vTDj9tjjDnoxV7fj3e1E15DivYTu0dRKXYrS4qwQep0P5f8N483R9vL8cAmm46+tkzmKeebIGi6lyXanqhYHHBYu5C5PXt5Gs="
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|ValidateCode |是  |string |图片验证码   |
|UserName |是  |string |登录用户名   |
|Password |是  |string |登录密码, rsa加密   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": {
        "id": 2,
        "type": 2,
        "username": "admin"
    },
    "Message": "Success",
    "RequestId": "ef9fc964-5c30-408b-b603-b66b9e05ac7b"
}
```


#### 添加小区房屋

##### 简要描述

- 添加小区房屋

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "AddFamily",
    "Community": "东风路办事处",
    "Building": "3号楼",
    "Dormitory": "303室"
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|Community |是  |string |社区名称   |
|Building |是  |string |楼(幢)号   |
|Dormitory |是  |string |户(室)号   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": "Success",
    "Message": "Success",
    "RequestId": "33179a4a-882e-415b-86ff-a7a69c9b000b"
}
```


#### 更新家庭信息

##### 简要描述

- 更新家庭信息

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "UpdateFamily",
    "FamilyId": 4,
    "MasterName": "珍珠哥",
    "JsonData": "{}"
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|FamilyId |是  |int |房屋id   |
|MasterName |是  |string |户主姓名   |
|JsonData |是  |string |家庭信息json字符串, 内部格式随意   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": "Success",
    "Message": "Success",
    "RequestId": "33179a4a-882e-415b-86ff-a7a69c9b000b"
}
```


#### 查询家庭信息列表

##### 简要描述

- 查询家庭信息列表, 管理员只能看到自己录入的, 超级管理员能看到所有

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "ListFamily"
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
    "Data": [
        {
            "building": "3号楼",
            "community": "东风路办事处",
            "dormitory": "303室",
            "id": 4,
            "json_data": "{}",
            "master_name": "珍珠哥"
        }
    ],
    "Message": "Success",
    "RequestId": "0cfbaea3-175e-4e8f-b52f-ed4f68d1ad09"
}
```


#### 注册用户

##### 简要描述

- 注册用户, 超级管理员可以注册管理员, 管理员可以注册普通用户

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "Register",
    "UserName": "inyin",
    "Password": "123456",
    "Type": 1
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|UserName |是  |string |登录用户名   |
|Password |否  |string |登录密码, 不传时默认为123456   |
|Type |是  |int |账号类型: 1-普通用户, 2-普通管理员, 3-超级管理员   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": "Success",
    "Message": "Success",
    "RequestId": "33179a4a-882e-415b-86ff-a7a69c9b000b"
}
```


#### 新增用户信息

##### 简要描述

- 新增用户信息

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "AddPersonnel",
    "UserId": 4,
    "FamilyId": 4,
    "Type": 0,
    "Domicile": "海南儋州",
    "JsonData": "{}"
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|UserId |是  |int |绑定的用户id   |
|FamilyId |是  |int |绑定的家庭id   |
|Type |是  |int |人口类型: 0-常驻人口, 1-流动人口, 2-新生人口, 3-死亡人口   |
|Domicile |是  |string |籍贯   |
|JsonData |是  |string |人员信息json字符串, 内部格式随意   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": "Success",
    "Message": "Success",
    "RequestId": "33179a4a-882e-415b-86ff-a7a69c9b000b"
}
```


#### 退出登录

##### 简要描述

- 退出登录

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "Logout",
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
    "Data": "Success",
    "Message": "Success",
    "RequestId": "33179a4a-882e-415b-86ff-a7a69c9b000b"
}
```