# -*- coding: utf-8 -*-

"""
gmncurses.ui.views.auth
~~~~~~~~~~~~~~~~~~~~~~~
"""

from gmncurses.ui import widgets

from . import base


class LoginView(base.View):
    login_button = None

    def __init__(self, username_text, password_text):
        # Header
        header = widgets.banner()
        # Username and password prompts
        max_prompt_length = max(len(username_text), len(password_text))
        max_prompt_padding = max_prompt_length + 2

        self._username_editor = widgets.editor()
        username_prompt = widgets.username_prompt(username_text, self._username_editor, max_prompt_padding)
        self._password_editor = widgets.editor(mask="♥")
        password_prompt = widgets.password_prompt(password_text, self._password_editor, max_prompt_padding)
        # Login button
        self.login_button = widgets.button("login")
        login_button_widget = widgets.wrap_login_button(self.login_button)
        # Notifier
        self.notifier = widgets.Notifier("")

        login_widget = widgets.Login([header,
                                      widgets.box_solid_fill(" ", 2),
                                      username_prompt,
                                      widgets.box_solid_fill(" ", 1),
                                      password_prompt,
                                      widgets.box_solid_fill(" ", 2),
                                      login_button_widget,
                                      widgets.box_solid_fill(" ", 1),
                                      self.notifier])
        self.widget = widgets.center(login_widget)

    @property
    def username(self):
        return self._username_editor.get_edit_text()

    @property
    def password(self):
        return self._password_editor.get_edit_text()
