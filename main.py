#!/usr/bin/env python

import updown
from argparse import Namespace


LOCAL_UPLOAD_FOLDER = '~/camera_data'
DROPBOX_FOLDER = '/camera_data'


def main():
    """Upload """
    access_token = ''
    args = Namespace(default=False, folder=DROPBOX_FOLDER, no=False, rootdir=LOCAL_UPLOAD_FOLDER, token=access_token,
                     yes=True)

    updown.main(args)

if __name__ == '__main__':
    main()
