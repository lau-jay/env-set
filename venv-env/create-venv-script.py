#!/usr/bin/env python
# encoding: utf-8

import subprocess

import virtualenv

virtualenv_path = subprocess.check_output(['which', 'virtualenv']).strip()

EXTRA_TEXT = '''
def extend_parser(parser):
    parser.add_option('-r', '--req', action='append', type='string',
    help='spacify additional required packages', default=[]
    )

def adjust_options(options, args):
    if not args:
        return
    base_dir = args[0]
    args[0] = join(ROOT_PATH, base_dir)

def after_install(options, home_dir):
    subprocess.call(['{}/bin/pip'.format(home_dir), 'install', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple', req])
'''

def main():
    text = virtualenv.create_bootstrap_script(EXTRA_TEXT, python_version='2.7')
    print('Updating %s' % virtualenv_path)
    with open(virtualenv_path, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    main()
