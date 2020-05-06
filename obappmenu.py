#!/usr/bin/env python3

from glob import glob
from xdg.DesktopEntry import DesktopEntry
from xdg import IconTheme

desk_entries = []

if __name__ == '__main__':
    print('<openbox_pipe_menu>')
    for desk_file in glob('/usr/share/applications/*.desktop'):
        de = DesktopEntry(desk_file)
        desk_entries.append((de.getName(),
                            IconTheme.getIconPath(de.getIcon(), theme='Adwaita'),
                            de.getExec().split('%')[0]))
        desk_entries.sort()
    for de in desk_entries:
        print('<item label="{}" icon="{}"><action name="Execute"><command>{}</command></action></item>'.format(*de))
    print('</openbox_pipe_menu>')
