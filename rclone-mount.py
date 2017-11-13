#!/usr/bin/env python3
import os
import argparse
import json
import subprocess

DEFAULT_CONF = os.path.expanduser('~/.rclone-mount.json')

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='Mount rclone remotes to folders.',
                                 epilog=r'''Example config file

[{
    "source": "gsuite:/videos/",
    "dest": "~/Videos/Gsuite"
},
{
    "source": "onedrive:/Videos",
    "dest": "~/Videos/Onedrive"
}]
''')
parser.add_argument('-c', '-o', '--conf', action='store',
                    nargs='?', type=argparse.FileType('r'),
                    default=DEFAULT_CONF, metavar='options.json',
                    help="File to parse mounting options from")
parser.add_argument('-u', '--unmount', action='store_true',
                    help='Unmount only')
parser.add_argument('--max-read-ahead', action='store',
                    type=str, default='2G',
                    help='Max read ahead to pass to rclone')


def unmount(mount_path):
    """
    Unmounts rclone path
    :param mount_path: Path where filesystem might be mounted
    :return: True if unmounted, False if not found
    """
    command = ('fusermount',  '-uz', mount_path)
    umount = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    umount.wait(30)
    err = umount.stderr.read()
    if 'not found in' in err.decode('utf-8'):
        return False
    if err.decode('utf-8') == '': # if no errors assume it was a success
        return True


def mount(source, dest, read_ahead):
    """
    Mount path
    :param source: Source to mount
    :param dest: path to destination
    :return:
    """
    dest = os.path.expanduser(dest)
    command = ('rclone', 'mount', source, dest, '--read-only', '--max-read-ahead', read_ahead)
    subprocess.Popen(command)
    return


if __name__ == '__main__':
    args = parser.parse_args()
    j = json.load(args.conf)
    for i in j:
        for k, v in i.items():
            if k == 'dest':
                v = os.path.expanduser(v)
                unmount(v)
    if not args.unmount:
        for i in j:
            print(i)
            mount(read_ahead=args.max_read_ahead, **i)
