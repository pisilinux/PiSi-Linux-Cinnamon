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
    shelltools.system("sed -i -e '/AC_SUBST(DISABLE_DEPRECATED_CFLAGS)/d' configure.in")
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    autotools.configure("--prefix=/usr \
                         --libexecdir=/usr/lib/nemo \
                         --disable-static \
                         --enable-unique \
                         --disable-packagekit \
                         --disable-tracker \
                         --disable-update-mimedb \
                         --disable-gtk-doc-html \
                         --disable-schemas-compile \
                         --with-gnu-ld \
                         --with-x ")
    
    #pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "AUTHORS")