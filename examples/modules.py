from django.conf.urls import url
from django.views import generic

from karenina import modules


class Website(modules.Module):
    """
    Home page module
    """
    order = 1
    label = 'Viewflow Demo'
    icon = 'fa fa-home'

    @property
    def urls(self):
        index_view = generic.TemplateView.as_view(template_name='examples/index.html')

        return modules.ModuleURLResolver('^$', [url('^$', index_view, name="index")], module=self,
                                         app_name=self.app_name, namespace=self.slug)

class Viewform(modules.Module):
    """
    """
    label = "Forms"
    order = 20

    def get_urls(self):
        index_view = generic.RedirectView.as_view(url="http://forms.viewflow.io/")
        return [url('^$', index_view, name="index")]
