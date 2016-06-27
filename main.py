#!/usr/bin/env python

from argparse import Namespace, ArgumentParser
import os

import updown
from network import get_public_ip

HOME = os.path.expanduser('~')

LOCAL_UPLOAD_FOLDER = HOME + '/camera_data'
DROPBOX_FOLDER = '/camera_data'
LOCAL_IP_FILE = HOME + '/camera_data/ip'
DROPBOX_IP_FILE = DROPBOX_FOLDER + '/ip'
ACCESS_TOKEN = ''


def upload_videos():
    args = Namespace(default=False, folder=DROPBOX_FOLDER, no=False, rootdir=LOCAL_UPLOAD_FOLDER,
                     token=ACCESS_TOKEN,
                     yes=True)
    updown.main(args)


def upload_ip():
    try:
        local_ip = open(LOCAL_IP_FILE, 'r').read()
    except IOError:
        if not os.path.exists(LOCAL_UPLOAD_FOLDER):
            os.mkdir(LOCAL_UPLOAD_FOLDER)
        open(LOCAL_IP_FILE, 'w')
        local_ip = ''
    public_ip = get_public_ip()

    if local_ip != public_ip:
        with open(LOCAL_IP_FILE, 'w') as f:
            f.write(public_ip)
        updown.TransferFile(ACCESS_TOKEN).upload_file(LOCAL_IP_FILE, DROPBOX_IP_FILE)


def main():
    """Upload """
    args = get_args()

    if args.upload_videos:
        upload_videos()
    if args.upload_ip:
        upload_ip()


def get_args():
    parser = ArgumentParser(description='Upload all videos saved at {0} to Dropbox.'.format(LOCAL_UPLOAD_FOLDER))
    parser.add_argument('-u', '--upload-videos', required=False, default=False, action='store_true')
    parser.add_argument('-i', '--upload-ip', help='Upload ip file only', required=False, default=False,
                        action='store_true')

    args = parser.parse_args()

    if sum([bool(b) for b in (args.upload_ip, args.upload_videos)]) > 1:
        print('At most one of --upload-videos, --upload-ip is allowed')
        exit(2)

    return args



if __name__ == '__main__':
    main()
