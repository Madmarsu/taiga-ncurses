# -*- coding: utf-8 -*-

"""
gmncurses.ui.views.wiki
~~~~~~~~~~~~~~~~~~~~~~~
"""

import urwid

from gmncurses.ui import widgets

from . import base


class ProjectWikiSubView(base.SubView):
    def __init__(self, parent_view, project, notifier, tabs):
        super().__init__(parent_view)

        self.project = project
        self.notifier = notifier

        self.wiki_page = widgets.WikiPage(project)

        list_walker = urwid.SimpleFocusListWalker([
            tabs,
            widgets.box_solid_fill(" ", 1),
            self.wiki_page,
        ])
        list_walker.set_focus(2)
        self.widget = urwid.ListBox(list_walker)