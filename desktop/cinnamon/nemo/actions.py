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
    #shelltools.touch("gtk-doc.make")
    #shelltools.touch("configure.ac")
    #autotools.autoreconf("-fi")
    shelltools.system("NOCONFIGURE=0 ./autogen.sh")
    autotools.configure("--disable-more-warnings \
                         --disable-update-mimedb \
                         --disable-gtk-doc-html \
                         --disable-schemas-compile")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "AUTHORS")