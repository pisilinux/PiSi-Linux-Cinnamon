#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    shelltools.system("./autogen.sh")
    autotools.configure("--with-mit-ext=no \
                         --with-pam-prefix=/etc/pam.d/cinnamon-screensaver \
                         --with-x \
                         --without-systemd \
                         --with-console-kit \
                         --with-xf86gamma-ext \
                         --libexecdir=/usr/lib/cinnamon-screensaver")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "AUTHORS")