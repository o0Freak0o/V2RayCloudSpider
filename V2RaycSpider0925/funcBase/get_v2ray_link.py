# windows10 下不可用
import sys

sys.path.append('/qinse/V2RaycSpider0925')
from config import NGINX_V2RAY_PATH

from MiddleKey.VMes_IO import vmess_IO
from spiderNest.v2ray_ufo_spider import UFO_Spider

if __name__ == '__main__':
    vio = vmess_IO('v2ray')
    if '无' in vio:
        UFO_Spider().start()
        v2ray = vmess_IO('v2ray')
        print(v2ray)
        with open(NGINX_V2RAY_PATH, 'w', encoding='utf-8') as f:
            f.write(v2ray)
    else:
        print(vio)
