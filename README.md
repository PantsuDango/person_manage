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


#### 添加房屋地址

##### 简要描述

- 添加房屋地址

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "AddAddr",
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


#### 更新房屋地址

##### 简要描述

- 更新房屋地址

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "UpdateAddr",
    "AddrId": 1,
    "Community": "东风路办事处",
    "Building": "3号楼",
    "Dormitory": "303室",
    "FamilyId": 0
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|AddrId |是  |int |房屋地址id   |
|Community |是  |string |社区名称   |
|Building |是  |string |楼(幢)号   |
|Dormitory |是  |string |户(室)号   |
|FamilyId |否  |int |绑定的家庭id   |


##### 返回示例 

``` 
{
    "Code": 0,
    "Data": "Success",
    "Message": "Success",
    "RequestId": "33179a4a-882e-415b-86ff-a7a69c9b000b"
}
```


#### 查询房屋地址信息列表

##### 简要描述

- 查询房屋地址信息列表, 管理员只能看到自己录入的, 超级管理员能看到所有

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "ListAddr"
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
            "family_id": 0,
            "id": 1
        }
    ],
    "Message": "Success",
    "RequestId": "bfa28710-2a8e-4c2c-a87b-7bad270d2f53"
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
    "Type": 1,
    "PersonnelId": 1
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|UserName |是  |string |登录用户名   |
|Password |否  |string |登录密码, 不传时默认为123456   |
|Type |是  |int |账号类型: 1-普通用户, 2-普通管理员, 3-超级管理员   |
|PersonnelId |否  |int |账户绑定的用户信息, 如果注册的账户类型为普通用户, 则必须传递   |

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


#### 添加家庭信息

##### 简要描述

- 添加家庭信息

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "AddFamily",
    "AddrId": 0,
    "MasterName": "珍珠哥",
    "JsonData": "{}"
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|AddrId |否  |int |绑定的房屋地址id   |
|MasterName |否  |string |户主姓名   |
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
    "FamilyId": 1,
    "AddrId": 0,
    "MasterName": "珍珠哥",
    "JsonData": "{}"
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|FamilyId |是  |int |家庭信息id   |
|AddrId |否  |int |绑定的房屋地址id   |
|MasterName |否  |string |户主姓名   |
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
            "addr_id": 0,
            "id": 1,
            "json_data": "{}",
            "master_name": "珍珠哥"
        }
    ],
    "Message": "Success",
    "RequestId": "47a0aac4-1c03-4233-a8d5-32393c11e17a"
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
    "UserId": 0,
    "FamilyId": 1,
    "Type": 0,
    "Domicile": "海南儋州",
    "JsonData": "{}"
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|UserId |否  |int |绑定的用户id   |
|FamilyId |是  |int |绑定的家庭id   |
|Type |否  |int |人口类型: 0-常驻人口, 1-流动人口, 2-新生人口, 3-死亡人口   |
|Domicile |否  |string |籍贯   |
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


#### 更新用户信息

##### 简要描述

- 更新用户信息

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "UpdatePersonnel",
    "PersonnelId": 1,
    "UserId": 0,
    "Type": 1,
    "Domicile": "海南儋州",
    "JsonData": "{}"
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|PersonnelId |是  |string |用户信息id   |
|UserId |否  |int |绑定的用户id   |
|Type |否  |int |人口类型: 0-常驻人口, 1-流动人口, 2-新生人口, 3-死亡人口   |
|Domicile |否  |string |籍贯   |
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


#### 查询人员信息列表

##### 简要描述

- 查询人员信息列表, 普通用户只能看到自己的, 管理员只能看到自己录入的, 超级管理员能看到所有

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "ListPersonnel"
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
        [
            {
                "domicile": "海南儋州",
                "family_id": 1,
                "id": 1,
                "json_data": "{}",
                "type": 1,
                "user_id": 7
            },
            {
                "domicile": "123",
                "family_id": 1,
                "id": 3,
                "json_data": "{\"IDCard\":\"1123\",\"ID\":\"编号编号\",\"Name\":\"姓姓姓\",\"NameTip\":\"名首字母名首字母\",\"Sex\":\"0\",\"Birthday\":\"2021-05-03T16:00:00.000Z\",\"Birthplace\":\"出生地出生地\",\"Relationship\":\"姻关系\",\"Matrimony\":\"姻关系\",\"Phone\":\"联系电\",\"Healthly\":\"联系电\",\"PeosonHeight\":\"联系电\",\"BloodTypes\":\"123\",\"Nationality\":\"123\",\"Education\":\"q21\",\"Politics\":\"123\",\"CensusRegister\":\"\",\"Address\":\"123\",\"Residences\":\"出生地出生地\",\"Profession\":\"123\",\"Job\":\"123\",\"OldName\":\"曾用名曾用名\",\"Desc\":\"123\"}",
                "type": 1,
                "user_id": 0
            }
        ],
        [
            {
                "domicile": "qwe",
                "family_id": 6,
                "id": 2,
                "json_data": "{\"IDCard\":\"123\",\"ID\":\"123\",\"Name\":\"123\",\"NameTip\":\"qew\",\"Sex\":\"0\",\"Birthday\":\"2021-04-12T16:00:00.000Z\",\"Birthplace\":\"qwe\",\"Relationship\":\"qwe\",\"Matrimony\":\"qwe\",\"Phone\":\"qweqw\",\"Healthly\":\"qqq\",\"PeosonHeight\":\"qwe\",\"BloodTypes\":\"qwe\",\"Nationality\":\"qwe\",\"Education\":\"qwe\",\"Politics\":\"eqwe\",\"CensusRegister\":\"\",\"Address\":\"qwe\",\"Residences\":\"qwe\",\"Profession\":\"qwe\",\"Job\":\"qwe\",\"OldName\":\"123\",\"Desc\":\"qwe\"}",
                "type": 0,
                "user_id": 0
            }
        ],
        []
    ],
    "Message": "Success",
    "RequestId": "bbf35f6c-39e9-4bbe-82b2-4a0e986fc5b4"
}
```


#### 获取账号列表

##### 简要描述

- 获取账号列表, 超级管理员能看到所有账号, 普通管理员能看到自己注册的账号

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "ListUser"
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
            "id": 1,
            "password": "123456",
            "type": 3,
            "username": "root"
        },
        {
            "id": 2,
            "password": "123456",
            "type": 2,
            "username": "admin"
        },
        {
            "id": 6,
            "password": "123456",
            "type": 2,
            "username": "123123"
        },
        {
            "id": 7,
            "password": "123456",
            "type": 1,
            "username": "inyin"
        }
    ],
    "Message": "Success",
    "RequestId": "8a04a02a-6f28-4ef6-bba4-94b3977644b9"
}
```


#### 查询家庭详情

##### 简要描述

- 查询家庭详情

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "FamilyInfo",
    "FamilyId": 1
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|FamilyId |是  |int |家庭id   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": {
        "family_info": {
            "addr_id": 1,
            "createtime": "Mon, 17 May 2021 23:53:12 GMT",
            "id": 1,
            "json_data": "{}",
            "lastupdate": "Tue, 18 May 2021 00:10:51 GMT",
            "master_name": "珍珠哥",
            "user_id": 2
        },
        "personnel_info": [
            {
                "createtime": "Tue, 18 May 2021 22:32:35 GMT",
                "domicile": "海南儋州",
                "family_id": 1,
                "id": 1,
                "json_data": "{}",
                "lastupdate": "Tue, 18 May 2021 22:51:40 GMT",
                "type": 1,
                "user_id": 7
            }
        ]
    },
    "Message": "Success",
    "RequestId": "662b06e4-9c45-4e01-a6d6-87ff6a71d2b5"
}
```


#### 信息检索

##### 简要描述

- 信息检索

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "SelectInfo",
    "Community": "东风路",
    "Type": 1,
    "Domicile": "海南",
    "MasterName": "珍珠"
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|Community |否  |string |社区名称, 模糊匹配   |
|Type |否  |int |人口类型   |
|Domicile |否  |string |籍贯, 模糊匹配   |
|MasterName |否  |string |户主姓名, 模糊匹配   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": [
        {
            "community": "东风路办事处",
            "domicile": "海南儋州",
            "family_id": 1,
            "family_json_data": "{}",
            "id": 1,
            "master_name": "珍珠哥",
            "personnel_json_data": "{}",
            "type": 1,
            "user_id": 7
        }
    ],
    "Message": "Success",
    "RequestId": "2b402953-aa4e-42bc-91cc-522b222ae1d9"
}
```


#### 修改账户信息

##### 简要描述

- 修改账户信息

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "ModifyUser",
    "Password": "123456",
    "UserId": 3
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|Password |是  |string |密码   |
|UserId |是  |int |账户id   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": "Success",
    "Message": "Success",
    "RequestId": "33179a4a-882e-415b-86ff-a7a69c9b000b"
}
```


#### 删除账户信息

##### 简要描述

- 删除账户信息

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "DeleteUser",
    "UserId": 3
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|UserId |是  |int |账户id   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": "Success",
    "Message": "Success",
    "RequestId": "33179a4a-882e-415b-86ff-a7a69c9b000b"
}
```


#### 查询人员详情

##### 简要描述

- 查询人员详情

##### 请求URL
- ` http://39.108.110.77/person_manage/api `
  
##### 请求方式
- POST 

##### 请求示例 

``` 
{
    "Action": "PersonnelInfo",
    "PersonnelId": 1
}
```

##### 参数

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|Action |是  |string |接口名   |
|PersonnelId |是  |int |人员Id   |

##### 返回示例 

``` 
{
    "Code": 0,
    "Data": {
        "family_info": [
            {
                "addr_id": 0,
                "id": 1,
                "json_data": "{\"FamilyNumber\":3,\"FamilyNumberID\":\"家庭编号家庭编号\",\"PermanentNumber\":\"户口编号户口编号\",\"MasterName\":\"户主\",\"Phone\":\"系电话\",\"Condition\":\"经济\",\"houseType\":\"所类型\",\"Address\":\"2312\",\"Desc\":\"3123123\"}",
                "master_name": "户主",
                "user_id": 2
            }
        ],
        "personnel_info": [
            {
                "domicile": "海南儋州",
                "family_id": 1,
                "id": 1,
                "json_data": "{}",
                "type": 1,
                "user_id": 7
            }
        ]
    },
    "Message": "Success",
    "RequestId": "df75471b-ad4b-4247-8d5c-bdf5dc054885"
}
```