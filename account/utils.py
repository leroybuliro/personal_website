from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class activationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_deactivated)

activation_token = activationTokenGenerator()