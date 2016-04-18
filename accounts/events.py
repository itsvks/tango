from django.contrib.auth import get_user_model

from common.utills import Event

User = get_user_model()


class UserRegistered(Event):
    code = 'user_registered'
    notify = 'email'
    app_name = 'accounts'

    def run(self, ctx):
        ctx['user'] = User.objects.get(id=ctx['user_id'])
        super(UserRegistered, self).run(ctx)


class UserChangePassword(Event):
    code = 'change_password'
    notify = 'email'
    app_name = 'accounts'

    def run(self, ctx):
        super(UserChangePassword, self).run(ctx)

