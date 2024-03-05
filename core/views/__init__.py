from core.views.cancel import cancel
from core.views.checkout import checkout
from core.views.communications import communications
from core.views.contact_us import contact_us
from core.views.donate import donate
from core.views.faq import faq
from core.views.home import home
from core.views.payment import payment
from core.views.policies import policies
from core.views.set_faq import set_faq
from core.views.set_policies import set_policies
from core.views.success import success
from core.views.webhook import webhook

__all__ = [
    home,
    communications,
    contact_us,
    faq,
    policies,
    set_faq,
    set_policies,
    cancel,
    checkout,
    payment,
    success,
    webhook,
    donate,
]
