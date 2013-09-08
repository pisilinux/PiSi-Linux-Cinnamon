#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

os.environ['GCONF_CONFIG_SOURCE']="xml:merged:/etc/gconf/gconf.xml.defaults"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('gconftool-2 --makefile-install-rule /etc/gconf/schemas/gnome-power-manager.schemas')

def preRemove():
    os.system('gconftool-2 --makefile-uninstall-rule /etc/gconf/schemas/gnome-power-manager.schemas')

