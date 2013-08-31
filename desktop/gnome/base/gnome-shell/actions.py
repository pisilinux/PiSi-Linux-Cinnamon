#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():

#    shelltools.export("LDFLAGS", "%s -rpath=/usr/lib" % get.LDFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-schemas-install \
                         --enable-introspection=yes \
                         --enable-compile-warnings=no")
    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared  -Wl,-rpath /usr/lib/gnome-bluetooth/")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")

