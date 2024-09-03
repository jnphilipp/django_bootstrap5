# -*- coding: utf-8 -*-
# Copyright (C) 2022-2024 J. Nathanael Philipp (jnphilipp) <nathanael@philipp.land>
#
# This file is part of django_bootstrap5.
#
# django_bootstrap5 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django_bootstrap5 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django_bootstrap5. If not, see <http://www.gnu.org/licenses/>.

from django.template import Context, Template
from django.test import TestCase


class BootstrapTestCase(TestCase):
    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def test_load_css_js(self):
        rendered = self.render_template("{% load bootstrap %}{% bootstrap_css %}")
        self.assertEqual(
            rendered,
            '\n\n<link rel="stylesheet" media="all" href="/static/css/bootstrap.min.css'
            '"/>\n<link rel="stylesheet" media="all" href="/static/css/django-bootstrap'
            '5.css"/>\n<link rel="stylesheet" media="all" href="/static/css/jquery-ui.m'
            'in.css"/>\n<link rel="stylesheet" media="all" href="/static/css/jquery-ui.'
            'structure.min.css"/>\n<link rel="stylesheet" media="all" href="/static/css'
            '/jquery-ui.theme.min.css"/>\n<link rel="stylesheet" media="all" href="/sta'
            'tic/css/select2.min.css"/>\n',
        )

        rendered = self.render_template("{% load bootstrap %}{% bootstrap_js %}")
        self.assertEqual(
            rendered,
            '\n\n<script type="text/javascript" src="/static/js/jquery.min.js"></script'
            '>\n<script type="text/javascript" src="/static/js/jquery-ui.min.js"></scri'
            'pt>\n<script type="text/javascript" src="/static/js/bootstrap.bundle.min.j'
            's"></script>\n<script type="text/javascript" src="/static/js/select2.min.j'
            's"></script>\n<script type="text/javascript" src="/static/js/btn-toggle.js'
            '"></script>\n<script type="text/javascript">\n    $(function () {\n       '
            " $('[data-toggle=\"tooltip\"]').tooltip();\n    });\n</script>\n",
        )

    def test_iframeformmodal(self):
        rendered = self.render_template("{% load bootstrap %}{% iframe_form_modal %}")
        self.assertEqual(
            rendered,
            '\n\n<script type="text/javascript">\n    $(function() {\n        $("a.ifra'
            'meFormModal").modal({\n            show: false\n        });\n        $("#i'
            'frameFormModal").on("show.bs.modal", function(e) {\n            $("#iframe'
            'FormModalLabel").html(e.relatedTarget.title);\n            $("#iframeFormM'
            'odalIframe").attr("src", e.relatedTarget.href);\n        });\n\n        fu'
            "nction sleep(ms) {\n            return new Promise(resolve => setTimeout(r"
            'esolve, ms));\n        }\n\n        let iframe = document.getElementById("'
            'iframeFormModalIframe");\n        iframe.addEventListener("load", async (e'
            "vent) => {\n            try {\n                while ( true ) {\n         "
            "           if ( iframe.contentWindow.document.body.scrollHeight === 0 ) {"
            "\n                        await sleep(100);\n                    } else {"
            "\n                        iframe.style.height = iframe.contentWindow.docum"
            'ent.body.scrollHeight + "px";\n                        break;\n           '
            "         }\n                }\n            } catch (error) {\n            "
            '    console.log("Error:", error);\n            }\n        });\n    });\n</'
            'script>\n<div class="modal fade" id="iframeFormModal" tabindex="-1" role="'
            'dialog" aria-labelledby="iframeFormModalLabel" aria-hidden="true" data-bs-'
            'backdrop="static">\n    <div class="modal-dialog modal-xl modal-dialog-cen'
            'tered modal-dialog-scrollable" role="document">\n        <div class="modal'
            '-content">\n            <div class="modal-header">\n                <h5 cl'
            'ass="modal-title" id="iframeFormModalLabel"></h5>\n                <button'
            ' type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cance'
            'l"></button>\n            </div>\n            <div class="modal-body" styl'
            'e="padding-left: 0; padding-right: 0;">\n                <iframe id="ifram'
            'eFormModalIframe" name="iframeFormModalIframe" frameborder="0" style="widt'
            'h: 100%;  "></iframe>\n            </div>\n            <div class="modal-'
            'footer">\n                <button type="button" class="btn btn-secondary" '
            'data-bs-dismiss="modal">Cancel</button>\n                <button id="ifram'
            'eFormModalSubmit" type="submit" class="btn" onclick="window.frames[\'ifram'
            "eFormModalIframe'].document.forms[0].submit();\"></button>\n            </"
            "div>\n        </div>\n    </div>\n</div>\n",
        )
        rendered = self.render_template(
            '{% load bootstrap %}{% iframe_form_modal iframe_min_height="500px" %}'
        )
        self.assertEqual(
            rendered,
            '\n\n<script type="text/javascript">\n    $(function() {\n        $("a.ifra'
            'meFormModal").modal({\n            show: false\n        });\n        $("#i'
            'frameFormModal").on("show.bs.modal", function(e) {\n            $("#iframe'
            'FormModalLabel").html(e.relatedTarget.title);\n            $("#iframeFormM'
            'odalIframe").attr("src", e.relatedTarget.href);\n        });\n\n        fu'
            "nction sleep(ms) {\n            return new Promise(resolve => setTimeout(r"
            'esolve, ms));\n        }\n\n        let iframe = document.getElementById("'
            'iframeFormModalIframe");\n        iframe.addEventListener("load", async (e'
            "vent) => {\n            try {\n                while ( true ) {\n         "
            "           if ( iframe.contentWindow.document.body.scrollHeight === 0 ) {"
            "\n                        await sleep(100);\n                    } else {"
            "\n                        iframe.style.height = iframe.contentWindow.docum"
            'ent.body.scrollHeight + "px";\n                        break;\n           '
            "         }\n                }\n            } catch (error) {\n            "
            '    console.log("Error:", error);\n            }\n        });\n    });\n</'
            'script>\n<div class="modal fade" id="iframeFormModal" tabindex="-1" role="'
            'dialog" aria-labelledby="iframeFormModalLabel" aria-hidden="true" data-bs-'
            'backdrop="static">\n    <div class="modal-dialog modal-xl modal-dialog-cen'
            'tered modal-dialog-scrollable" role="document">\n        <div class="modal'
            '-content">\n            <div class="modal-header">\n                <h5 cl'
            'ass="modal-title" id="iframeFormModalLabel"></h5>\n                <button'
            ' type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cance'
            'l"></button>\n            </div>\n            <div class="modal-body" styl'
            'e="padding-left: 0; padding-right: 0;">\n                <iframe id="ifram'
            'eFormModalIframe" name="iframeFormModalIframe" frameborder="0" style="widt'
            'h: 100%; min-height: 500px; "></iframe>\n            </div>\n            <'
            'div class="modal-footer">\n                <button type="button" class="bt'
            'n btn-secondary" data-bs-dismiss="modal">Cancel</button>\n                '
            '<button id="iframeFormModalSubmit" type="submit" class="btn" onclick="wind'
            "ow.frames['iframeFormModalIframe'].document.forms[0].submit();\"></button"
            ">\n            </div>\n        </div>\n    </div>\n</div>\n",
        )
        rendered = self.render_template(
            '{% load bootstrap %}{% iframe_form_modal iframe_min_height="400px" '
            + 'iframe_max_height="800px" %}'
        )
        self.assertEqual(
            rendered,
            '\n\n<script type="text/javascript">\n    $(function() {\n        $("a.ifra'
            'meFormModal").modal({\n            show: false\n        });\n        $("#i'
            'frameFormModal").on("show.bs.modal", function(e) {\n            $("#iframe'
            'FormModalLabel").html(e.relatedTarget.title);\n            $("#iframeFormM'
            'odalIframe").attr("src", e.relatedTarget.href);\n        });\n\n        fu'
            "nction sleep(ms) {\n            return new Promise(resolve => setTimeout(r"
            'esolve, ms));\n        }\n\n        let iframe = document.getElementById("'
            'iframeFormModalIframe");\n        iframe.addEventListener("load", async (e'
            "vent) => {\n            try {\n                while ( true ) {\n         "
            "           if ( iframe.contentWindow.document.body.scrollHeight === 0 ) {"
            "\n                        await sleep(100);\n                    } else {"
            "\n                        iframe.style.height = iframe.contentWindow.docum"
            'ent.body.scrollHeight + "px";\n                        break;\n           '
            "         }\n                }\n            } catch (error) {\n            "
            '    console.log("Error:", error);\n            }\n        });\n    });\n</'
            'script>\n<div class="modal fade" id="iframeFormModal" tabindex="-1" role="'
            'dialog" aria-labelledby="iframeFormModalLabel" aria-hidden="true" data-bs-'
            'backdrop="static">\n    <div class="modal-dialog modal-xl modal-dialog-cen'
            'tered modal-dialog-scrollable" role="document">\n        <div class="modal'
            '-content">\n            <div class="modal-header">\n                <h5 cl'
            'ass="modal-title" id="iframeFormModalLabel"></h5>\n                <button'
            ' type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cance'
            'l"></button>\n            </div>\n            <div class="modal-body" styl'
            'e="padding-left: 0; padding-right: 0;">\n                <iframe id="ifram'
            'eFormModalIframe" name="iframeFormModalIframe" frameborder="0" style="widt'
            'h: 100%; min-height: 400px; max-height: 800px;"></iframe>\n            </d'
            'iv>\n            <div class="modal-footer">\n                <button type='
            '"button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>'
            '\n                <button id="iframeFormModalSubmit" type="submit" class="'
            "btn\" onclick=\"window.frames['iframeFormModalIframe'].document.forms[0].s"
            'ubmit();"></button>\n            </div>\n        </div>\n    </div>\n</div'
            ">\n",
        )
