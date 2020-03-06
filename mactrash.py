#!/usr/bin/env python3
from gi.repository import Gio, GLib

class SetTrashIcon:

    def __init__(self):
        # edit path to .desktop file and icon names below
        self.fpath = "/home/zacharygough/.local/share/applications/trashcan.desktop"
        self.iconempty = "user-trash"
        self.iconfull = "user-trash-full"
        # don't edit below
        self.trashdir = Gio.File.new_for_uri("trash:///")
        monitor = self.trashdir.monitor_directory(0, None)
        monitor.connect("changed", self.actonfile)
        self.currempty = None
        self.check_empty()
        loop = GLib.MainLoop()
        loop.run()

    def replace(self, newicon):
        # set the new icon, replace the Icon- line
        text = open(self.fpath).read()
        toreplace = [s for s in text.split() if s.startswith("Icon=")][0]
        newtext = text.replace(toreplace, "Icon=" + newicon)
        open(self.fpath, "wt").write(newtext)

    def set_icon(self, newempty):
        # if trash state changes, decide which icon to set
        if newempty != self.currempty:
            if newempty:
                self.replace(self.iconempty)
            else:
                self.replace(self.iconfull)
            self.currempty = newempty

    def check_empty(self):
        # check if trash is empty
        newempty = len(list(self.trashdir.enumerate_children(
            "standard::*", Gio.FileQueryInfoFlags.NONE, None
        ))) == 0
        self.set_icon(newempty)

    def actonfile(self, arg1=None, arg2=None, arg3=None, arg4=None):
        # act on changes in the trash content
        if arg4 == Gio.FileMonitorEvent.ATTRIBUTE_CHANGED:
            self.check_empty()

SetTrashIcon()
