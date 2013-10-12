#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --disable-rpath \
                         --disable-examples \
                         --disable-gnome-vfs \
                         --enable-libvisual \
                         --enable-experimental \
                         --with-package-name='PisiLinux gstreamer-plugins-base package' \
                         --with-package-origin='http://www.pisilinux.org'")

def build():
    autotools.make()

# tests fail sandbox
#def check():
#    autotools.make("-C tests/check check")

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.remove("/usr/share/locale/fr/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/lt/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/id/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/da/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/az/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/ja/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/nl/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/it/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/gl/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/sr/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/vi/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/uk/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/bg/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/sl/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/or/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/af/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/es/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/tr/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/sq/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/sv/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/pl/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/zh_CN/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/fi/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/eu/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/hu/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/ca/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/de/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/ro/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/sk/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/lv/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/nb/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/ru/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/eo/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/pt_BR/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/el/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/en_GB/LC_MESSAGES/.mo")
    pisitools.remove("/usr/share/locale/cs/LC_MESSAGES/.mo")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
