from desktop.settings import LOGOUT_URL


def exit_func(event, self):
    print("Ctrl+K pressed")
    reply = self.authorized_session.get(LOGOUT_URL)
    if reply.ok:
        self.authorized_session=None
        self.switch_frame(self.login_page)
    return reply

