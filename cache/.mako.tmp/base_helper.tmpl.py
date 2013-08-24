# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1377329352.803409
_enable_loop = True
_template_filename = u'themes/site-ipython/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'ascii'
_exports = ['html_head', 'html_sidebar_links', 'late_load_js', 'html_social', 'html_translations']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'\n\n')
        # SOURCE LINE 57
        __M_writer(u'\n\n')
        # SOURCE LINE 73
        __M_writer(u'\n\n\n')
        # SOURCE LINE 84
        __M_writer(u'\n\n\n')
        # SOURCE LINE 93
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_head(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        description = context.get('description', UNDEFINED)
        title = context.get('title', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        blog_author = context.get('blog_author', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n    <meta charset="utf-8">\n    <meta name="title" content="')
        # SOURCE LINE 3
        __M_writer(unicode(title))
        __M_writer(u' | ')
        __M_writer(unicode(blog_title))
        __M_writer(u'" >\n    <meta name="description" content="')
        # SOURCE LINE 4
        __M_writer(unicode(description))
        __M_writer(u'" >\n    <meta name="author" content="')
        # SOURCE LINE 5
        __M_writer(unicode(blog_author))
        __M_writer(u'">\n    <title>')
        # SOURCE LINE 6
        __M_writer(unicode(title))
        __M_writer(u' | ')
        __M_writer(unicode(blog_title))
        __M_writer(u'</title>\n    <!-- Le styles -->\n    <script type="text/x-mathjax-config">\n    MathJax.Hub.Config({\n        tex2jax: {\n            inlineMath: [ [\'$\',\'$\'], ["\\\\(","\\\\)"] ],\n            displayMath: [ [\'$$\',\'$$\'], ["\\\\[","\\\\]"] ]\n        },\n        displayAlign: \'left\', // Change this to \'center\' to center equations.\n        "HTML-CSS": {\n            styles: {\'.MathJax_Display\': {"margin": 0}}\n        }\n    });\n    </script>\n')
        # SOURCE LINE 20
        if use_bundles:
            # SOURCE LINE 21
            __M_writer(u'        <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n        <script src="/assets/js/all.js" type="text/javascript"></script>\n')
            # SOURCE LINE 23
        else:
            # SOURCE LINE 24
            __M_writer(u'        <link href="/assets/css/ipython.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/bootstrap.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css"/>\n        <link href="/assets/css/slides.css" rel="stylesheet" type="text/css"/>\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css"/>\n')
            # SOURCE LINE 32
            if has_custom_css:
                # SOURCE LINE 33
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
            # SOURCE LINE 35
            __M_writer(u'        <link href="/assets/css/bootstrap-responsive.css" rel="stylesheet" type="text/css">\n        <script src="/assets/js/jquery-1.7.2.min.js" type="text/javascript"></script>\n        <script src="/assets/js/jquery.colorbox-min.js" type="text/javascript"></script>\n        <script src="/assets/js/slides.min.jquery.js" type="text/javascript"></script>\n        <script src="/assets/js/bootstrap.min.js" type="text/javascript"></script>\n        <script src="/assets/js/mathjax-onload.js" type="text/javascript"></script>\n')
        # SOURCE LINE 42
        __M_writer(u'    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->\n    <!--[if lt IE 9]>\n      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js" type="text/javascript"></script>\n    <![endif]-->\n')
        # SOURCE LINE 46
        if rss_link:
            # SOURCE LINE 47
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
            # SOURCE LINE 48
        else:
            # SOURCE LINE 49
            for language in translations:
                # SOURCE LINE 50
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS (')
                __M_writer(unicode(language))
                __M_writer(u')" href="')
                __M_writer(unicode(_link('rss', None, lang)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sidebar_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        sidebar_links = context.get('sidebar_links', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 76
        __M_writer(u'\n')
        # SOURCE LINE 77
        for url, text in sidebar_links[lang]:
            # SOURCE LINE 78
            if rel_link(permalink, url) == "#":
                # SOURCE LINE 79
                __M_writer(u'            <li class="active"><a href="')
                __M_writer(unicode(url))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a>\n')
                # SOURCE LINE 80
            else:
                # SOURCE LINE 81
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(url))
                __M_writer(u'">')
                __M_writer(unicode(text))
                __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer(u'\n    <!-- Little patch to make it work -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_social(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        add_this_buttons = context.get('add_this_buttons', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 59
        __M_writer(u'\n')
        # SOURCE LINE 60
        if add_this_buttons:
            # SOURCE LINE 61
            __M_writer(u'    <!-- Social buttons -->\n    <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">\n    <a class="addthis_button_more">Share</a>\n    <ul><li><a class="addthis_button_facebook"></a></li>\n    <li><a class="addthis_button_google_plusone_share"></a></li>\n    <li><a class="addthis_button_linkedin"></a></li>\n    <li><a class="addthis_button_twitter"></a></li>\n    </ul>\n    </div>\n    <script type="text/javascript" src="http://s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>\n    <!-- End of social buttons -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 87
        __M_writer(u'\n')
        # SOURCE LINE 88
        for langname in translations.keys():
            # SOURCE LINE 89
            if langname != lang:
                # SOURCE LINE 90
                __M_writer(u'            <a href="')
                __M_writer(unicode(_link("index", None, langname)))
                __M_writer(u'">')
                __M_writer(unicode(messages[langname]["LANGUAGE"]))
                __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


