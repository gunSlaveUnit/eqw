def exit_func(event, self):
    print("Ctrl+K pressed")
    reply = self.authorized_session.get('http://127.0.0.1:23432/auth/sign-out/')
    if reply.ok:
        self.authorized_session=None
        self.switch_frame(self.login_page)
    return reply

