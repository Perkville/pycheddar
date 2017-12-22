# vim: set fileencoding=utf-8 :


class MouseTrap(Exception):
    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        self.parent_exception = kwargs.pop('parent_exception', None)
        super(MouseTrap, self).__init__(*args, **kwargs)

    def __unicode__(self):
        if self.args:
            return str(self.args[0])
        elif self.parent_exception:
            return str(self.parent_exception)
        else:
            return ''

    def __str__(self):
        return str(self).encode('utf-8')


class NotFound(MouseTrap):
    pass


class AuthorizationRequired(MouseTrap):
    pass


class Forbidden(MouseTrap):
    pass


class UnexpectedResponse(MouseTrap):
    pass


class BadRequest(MouseTrap):
    pass


class GatewayFailure(MouseTrap):
    pass


class GatewayConnectionError(MouseTrap):
    pass


class ValidationError(MouseTrap):
    pass


class Timeout(MouseTrap):
    pass


class ConnectionError(MouseTrap):
    pass
