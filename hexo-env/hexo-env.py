#!/usr/bin/env python3
# encoding: utf-8
# Author: pyclear <cappyclear@gmail.com>
import os
import sys

package = """
      {
        "name": "hexo-site",
        "version": "0.0.0",
        "private": true,
        "hexo": {
            "version": "3.2.2"
        },
        "dependencies": {
             "hexo": "^3.2.0",
             "hexo-deployer-git": "^0.2.0",
             "hexo-generator-archive": "^0.1.4",
             "hexo-generator-category": "^0.1.3",
             "hexo-generator-index": "^0.2.0",
             "hexo-generator-tag": "^0.2.0",
             "hexo-renderer-ejs": "^0.2.0",
             "hexo-renderer-marked": "^0.2.10",
             "hexo-renderer-scss": "^1.0.2",
             "hexo-server": "^0.2.0"
        }
      }
"""
class HexoEnv:
    def __init__(self, package):
        self.package =  package

    def replace_package(self):
        pass

    def create_package_file(self):
        with open('./package.json','w') as f:
            f.write(self.package)

    def npm_install(self):
        os.system("npm install --registry=https://registry.npm.taobao.org")

    def replace_yml(self, yml,**kargs):
        pass

    def replace_theme(self, theme_name):
        self.replace_yml(yml, them=theme_name)

    def done(self):
        self.npm_install()


    @staticmethod
    def is_node():
        return 'node' in os.environ['PATH'] or os.environ['NODE_VERSION']

if __name__ == '__main__':
    is_node = HexoEnv.is_node()
    if not is_node:
        print('you need install nodejs')
        sys.exit(1)
    hexo_env = HexoEnv(package)
    hexo_env.create_package_file()
    hexo_env.done()





