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
    autotools.configure("--libexecdir=/usr/lib/cinnamon-settings-daemon \
                         --disable-static \
                         --disable-pulse  \
                         --enable-profiling \
                         --enable-polkit \
                         --disable-schemas-compile \
                         --with-x \
                         --with-dbus-services=/usr/share/dbus-1/services/ \
                         --with-dbus-sys=/usr/share/dbus-1/system-services/ \
                         --with-nssdb")
    
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")
    
    #rpath fix
    #pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "AUTHORS")