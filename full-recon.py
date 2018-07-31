#!/usr/bin/env python
# coding: utf-8

import sys
import argparse
import os
import errno
import sublist3r

parser = argparse.ArgumentParser()
parser.add_argument("domainFile")

def recon(domainFile):
    domainFileDir = os.path.dirname(domainFile)
    subDomainDir = domainFileDir + "/subdomains"
    try:
        os.mkdir(subDomainDir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        else:
            print(subDomainDir + '已存在')

    print(subDomainDir)
    with open(domainFile) as f:
        domains = f.read().splitlines()
        for domain in domains:
            no_threads = 5
            savefile = subDomainDir + '/' + domain + '.sublist3r.txt'
            ports = None
            silent = False
            verbose = True
            enable_bruteforce = False # subbrute 貌似有问题，会卡住不动
            engines = None
            subdomains = sublist3r.main(domain, no_threads, savefile, ports, silent, verbose, enable_bruteforce,
                                        engines)
            print(subdomains)

if __name__ == '__main__':
    args = parser.parse_args()
    if (args.domainFile):
        recon(args.domainFile)
    else:
        print('you must specify a domain file')
