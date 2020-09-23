from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class MembershipConfig(models.Model):
    org_id = models.CharField(max_length=100)
    price_plan_id = models.CharField(max_length=255, blank=True, null=True)
    days_valid = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    banner_message = models.CharField(max_length=255)
    is_displayed_on_site = models.BooleanField(
        verbose_name="Is displayed for purchase", default=True)
    is_subscription = models.BooleanField(default=False)
    display_order = models.IntegerField(default=1)


class Membership(models.Model):
    membership_config_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    initiation_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    payment_status = models.CharField(max_length=100)


class AuxMembership(models.Model):
    membership_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly', max_length=100)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']
