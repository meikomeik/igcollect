#!/usr/bin/env python
#
# igcollect - Sent currently deployed game version.
#
# Copyright (c) 2016 InnoGames GmbH
#

from argparse import ArgumentParser
from os.path import exists
from time import time


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--prefix', default='version')
    parser.add_argument('--filename', default='version')

    return vars(parser.parse_args())


def main(prefix, filename):
    if not exists(filename):
        raise Exception('No file on "{0}"'.format(filename))

    with open(filename) as fh:
        line = fh.readline()

    revision = line.strip().rsplit(' ', 1)[-1]
    if revision.startswith('v'):
        revision = revision[1:]
    if revision.startswith('branches/v'):
        revision = revision[10:]
    revision = revision.replace('.', '_')
    print('{}.{} 1 {}'.format(prefix, revision, int(time())))


if __name__ == '__main__':
    main(**parse_args())
