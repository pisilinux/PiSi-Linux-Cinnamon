#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-authentication-scheme=pam \
                         --with-sysconfsubdir=X11/gdm \
                         --disable-scrollkeeper \
                         --with-user=gdm \
                         --with-group=gdm \
                         --with-xauth-dir=/var/lib/gdm \
                         --with-screenshot-dir=/var/lib/gdm \
                         --with-xevie")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")