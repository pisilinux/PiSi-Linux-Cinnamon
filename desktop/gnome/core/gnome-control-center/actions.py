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
    autotools.autoreconf("-fiv")
    shelltools.system("intltoolize --force --copy --automake")
    autotools.configure("--disable-static")

    shelltools.system("""
    sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' -e 's/ if test "$export_dynamic" = yes && test -n "$export_dynamic_flag_spec"; then/ func_append compile_command " -Wl,-O1,--as-needed"\n func_append finalize_command " -Wl,-O1,--as-needed"\n\0/' libtool
    """)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.domove("/usr/share/pkgconfig/*","/usr/lib/pkgconfig")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")