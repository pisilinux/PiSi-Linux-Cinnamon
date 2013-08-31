#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    pisitools.dosed("configure.ac", "AM_CONFIG_HEADER", "AC_CONFIG_HEADER")
    pisitools.dosed("gnome-panel/libpanel-util/panel-dconf.c", "dconf-client.h", "dconf/client/dconf-client.h")
    pisitools.dosed("gnome-panel/libpanel-util/panel-dconf.c", "dconf-paths.h", "dconf/common/dconf-paths.h")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-schemas-compile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")