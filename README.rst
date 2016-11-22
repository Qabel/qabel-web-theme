
qabel-web-theme
===============

Common template and theme files for Qabel microservices.

Packaged as a Django application.

Usage checklist
---------------

1. Add package to requirements.txt:

   This is not uploaded to any package index, therefore it should be referenced like
   this in requirements::

        git://github.com/Qabel/qabel-web-theme.git@<RELEASE>

   The ``@<RELEASE>`` part specifies a specific commit/tag/branch. It should be absolute,
   not master/HEAD/...

2. Add ``qabel_web_theme`` to the ``APPLICATIONS`` setting (before other apps)::

    INSTALLED_APPS = [
        'qabel_web_theme',
        'django...',
         ...
    ]

3. If not done already, ``USE_I18N = USE_L10N = USE_TZ = True`` and set a proper default
   language code, i.e. ``LANGUAGE_CODE = 'de-DE'``, and ``LANGUAGES``, if more than one language
   should be supported, eg::

        from django.utils.translation import ugettext_lazy as _

        LANGUAGES = [
            ('de', _('German')),
            ('en', _('English')),
        ]

4. Also enable the ``django.middleware.locale.LocaleMiddleware`` middleware

5. Add ``switch_language`` view to the URLconf::

        from qabel_web_theme import urls as theme_urls

        urlpatterns = [
            ...
            url(r'^', include(theme_urls)),
        ]

6. Using menus if needed, see below

l10n process
------------

- https://docs.djangoproject.com/en/1.9/topics/i18n/translation/#localization-how-to-create-language-files
- Lokalize is a pretty good translation tool, but there many other tools for most platforms as well.

Menus
-----

Setting ``MENU`` is list/tuple of dotted paths to functions creating your menu. Example::

    from django.utils.translation import ugettext_lazy as _

    def menu(request, menu_items):
        menu_items += (
            {
                'title': _('Page 1'),
                'view': test_page1,
            },
            {
                'title': _('Page 2'),
                'view': 'test-page2',
            },
            {
                'title': _('Visit qabel.de'),
                'url': 'https://www.qabel.de/',
            }
        )

``menu_items`` is a list of this requests' menu. The ``request`` can be queried as well, this is run after
view processing has completed. Every menu entry is a ``dict``, with at least a ``title`` and either a ``view``
or ``url``. The ``view`` is either a view name, or a view callable. When a view is used, parameters can be passed
just as you would for ``reverse`` via ``args`` and ``kwargs``.

Menu support requires ``MenuMiddleware``::

    MIDDLEWARE_CLASSES = [
        ...
        'qabel_web_theme.middleware.MenuMiddleware',
    ]

It also requires the use of the ``base_menu.html`` template, and the use of ``TemplateResponse`` instead of ``render``
(the two are compatible). Suggestion::

    from django.template.response import TemplateResponse as render

Running the test project
------------------------

Standard flow applies::

    # v- the Debian compatible way of putting it (Arch etc. can just do 'virtualenv _venv')
    python3 -m virtualenv --python=python3 _venv
    .  _venv/bin/activate
    pip install . django
    python theme_test/manage.py runserver
