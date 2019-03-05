#!/usr/bin/python3


import os
import logging
import fnmatch
import subprocess
import functools
import re

class _GpgpuDriver(object):

    def __init__(self, vendor=None, flavour=None):
        self.vendor = vendor
        self.flavour = flavour

    def is_valid(self):
        return not (not self.vendor and not self.flavour)

def _process_driver_string(string):
    '''Returns a _GpgpuDriver object'''
    driver = _GpgpuDriver()
    if string.find(':') != -1:
        details = string.split(':')
        if len(details) > 2:
            return None
        for elem in details:
            try:
                int(elem)
            except ValueError:
                driver.vendor = elem
            else:
                driver.flavour = elem
    else:
        driver.flavour = string
    return driver


def gpgpu_install_filter(drivers_str):
    drivers = []
    allow = []
    result = {}
    '''Filter the Ubuntu packages according to the parameters the users passed

    Ubuntu-drivers syntax

    ubuntu-drivers autoinstall --gpgpu [[driver:]version]
    ubuntu-drivers autoinstall --gpgpu driver[:version][,driver[:version]]

    If no version is specified, gives the “current” supported version for the GPU in question.

    Examples:
    ubuntu-drivers autoinstall --gpgpu
    ubuntu-drivers autoinstall --gpgpu 390
    ubuntu-drivers autoinstall --gpgpu nvidia:390

    Today this is only nvidia.  In the future there may be amdgpu-pro.  Possible syntax, to be confirmed only once there are driver packages that could use it:
    ubuntu-drivers autoinstall --gpgpu nvidia:390,amdgpu
    ubuntu-drivers autoinstall --gpgpu amdgpu:version
    '''

    # No args, just --gpgpu
    if drivers_str == 'nvidia':
        driver = _GpgpuDriver()
        drivers.append(driver)
    else:
        #if drivers_str.find(',') != -1:
        # Multiple drivers
        # e.g. --gpgpu nvidia:390,amdgpu
        print('the split is:\n%s' % (drivers_str.split(',')))
        for item in drivers_str.split(','):
            driver = _process_driver_string(item)
            if driver.is_valid():
                drivers.append(driver)
#        else:
            # Just one driver
            # e.g. --gpgpu 390
            #      --gpgpu nvidia:390
#            driver = _process_driver_string(drivers_str)
#            if driver.is_valid():
#                drivers.append(driver)

    for drv in drivers:
        print('vendor %s, flavour %s' % (drv.vendor, drv.flavour))


if __name__ == '__main__':
    print('390:')
    gpgpu_install_filter('390')
    print('nvidia:390:')
    gpgpu_install_filter('nvidia:390')
    print('nvidia:390,amdgpu')
    gpgpu_install_filter('nvidia:390,amdgpu')