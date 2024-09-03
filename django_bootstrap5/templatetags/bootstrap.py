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
"""Django bootstrap 5 template tags bootstrap library."""

import types

from copy import copy
from django.core.paginator import Page, Paginator
from django.forms import Form
from django.template import Library
from typing import Any, Dict, Optional

register = Library()


def _process_field_attributes(field, attr, process):
    # split attribute name and value from 'attr:value' string
    params = attr.split(":", 1)
    attribute = params[0]
    value = params[1] if len(params) == 2 else ""

    field = copy(field)

    # decorate field.as_widget method with updated attributes
    old_as_widget = field.as_widget

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        attrs = attrs or {}
        process(widget or self.field.widget, attrs, attribute, value)
        html = old_as_widget(widget, attrs, only_initial)
        self.as_widget = old_as_widget
        return html

    field.as_widget = types.MethodType(as_widget, field)
    return field


@register.filter
def startswith(value: Any, start: str) -> bool:
    """Startswith template filter."""
    if isinstance(value, str):
        return value.startswith(start)
    else:
        return str(value).startswith(start)


@register.filter
def endswith(value: Any, end: str) -> bool:
    """Endswith template filter."""
    if isinstance(value, str):
        return value.endswith(end)
    else:
        return str(value).endswith(end)


@register.filter
def substring(value: Any, sub: str) -> bool:
    """Substring template filter."""
    if isinstance(value, str):
        return sub in value
    else:
        return sub in str(value)


@register.filter
def append_attr(field, attr):
    """Append atrribute template filter."""

    def process(widget, attrs, attribute, value):
        if attrs.get(attribute):
            attrs[attribute] += " " + value
        elif widget.attrs.get(attribute):
            attrs[attribute] = widget.attrs[attribute] + " " + value
        else:
            attrs[attribute] = value

    return _process_field_attributes(field, attr, process)


@register.filter
def add_class(field, css_class):
    """Add a css class template filter."""
    return append_attr(field, "class:" + css_class)


@register.inclusion_tag("bootstrap/css.html")
def bootstrap_css():
    """Load bootstrap css files template tag."""
    return {}


@register.inclusion_tag("bootstrap/js.html")
def bootstrap_js() -> Dict:
    """Load bootstrap js files template tag."""
    return {}


@register.inclusion_tag("bootstrap/messages.html", takes_context=True)
def messages(context: Dict) -> Dict:
    """Add message template tag."""
    return {"messages": context["messages"]}


@register.inclusion_tag("bootstrap/pagination.html", takes_context=True)
def pagination(
    context: Dict,
    paginator: Paginator,
    page: Page,
    base_path: str,
    title: Optional[str] = None,
    **kwargs: str,
):
    """Pagination template tag."""
    start_page = max(int(page.number) - 4, 0)
    end_page = min(int(page.number) + 3, paginator.num_pages)
    context["prange"] = paginator.page_range[start_page:end_page]
    context["page"] = page
    context["base_path"] = base_path
    context["title"] = title

    get_params = "?"
    for k, v in kwargs.items():
        if not get_params.endswith("&") and not get_params.endswith("?"):
            get_params += "&"
        if v:
            get_params += "%s=%s" % (k, v)
    if get_params == "?":
        get_params = ""
    context["get_params"] = get_params

    return context


@register.inclusion_tag("bootstrap/form/base.html", takes_context=True)
def bootstrap_form(
    context: Dict,
    form: Form,
    url: str = "",
    method: str = "post",
    type: str = "horizontal",
    csrf: bool = True,
    **kwargs: str,
):
    """From template tag."""
    assert type in ["horizontal", "inline", "vertical"]
    context["form"] = form
    context["url"] = url
    context["method"] = method
    context["type"] = type
    context["csrf"] = csrf
    for k, v in kwargs.items():
        context[k] = v
    return context


@register.inclusion_tag("bootstrap/sortable_th.html", takes_context=True)
def sortable_th(
    context: Dict,
    column_name: str,
    o: str,
    get_name: str,
    get_value: str,
    colspan: int = 1,
    rowspan: int = 1,
    **kwargs: str,
):
    """Table header cell with sort link template tag."""
    context["column_name"] = column_name
    context["colspan"] = colspan
    context["rowspan"] = rowspan
    context["sort_icon"] = "up" if o.startswith("-") else "down"
    context["show_options"] = o.endswith(get_value)

    params = "&".join([f"{k}={v}" for k, v in kwargs.items() if v])
    context["link"] = (
        f"?{get_name}={'' if o.startswith('-') else '-'}{get_value}&{params}"
    )
    context["remove_link"] = f"?{get_name}=&{params}"
    return context


@register.inclusion_tag("bootstrap/iframe_form_modal.html", takes_context=True)
def iframe_form_modal(
    context: Dict,
    iframe_min_height: Optional[int] = None,
    iframe_max_height: Optional[int] = None,
    static_backdrop: bool = True,
):
    """Add modal with an iframe."""
    context["iframe_min_height"] = iframe_min_height
    context["iframe_max_height"] = iframe_max_height
    context["static_backdrop"] = static_backdrop

    return context
