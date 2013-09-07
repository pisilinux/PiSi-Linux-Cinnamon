#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    #shelltools.system("intltoolize --force --copy --automake")
    #autotools.autoreconf("-vif")
    autotools.configure("--disable-static --enable-compile-warnings=no --disable-compile-warnings")
                       
    #pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared  -Wl,-rpath /usr/lib/gnome-bluetooth/")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")