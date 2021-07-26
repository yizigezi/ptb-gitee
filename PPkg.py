import requests
import os
import sys
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos.demo import client

print("PPkg 包管理器 0.0.1 Beta")
# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 BucketName-APPID 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region

secret_id = 'AKIDjHYYHkwrVt0rQjlkSt3vWquhCQN3SZPy'      # 替换为用户的 secretId
secret_key = 'LPCjzxe3C4fz2nHUQ5TaQzGGzRcW9WbP'      # 替换为用户的 secretKey
region = 'ap-nanjing'     # 替换为用户的 Region

token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
response = client.get_presigned_download_url(
    Bucket='pydos-1301360149',
    Key='exampleobject',
    Expired=300,
    Headers={
        'Range': 'string'
    },
    Params={
        'param1': 'string',
        'param2': 'string'
    }
)