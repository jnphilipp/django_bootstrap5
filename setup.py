#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:
# Copyright (C) 2022 J. Nathanael Philipp (jnphilipp) <nathanael@philipp.land>
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
"""Setup django_bootstrap5 package."""

from setuptools import setup


def read_file(name):
    """Get the string contained in the file named name."""
    with open(name, "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="django_bootstrap5",
    version="0.2.1",
    description="Add Bootstrap 5 to Django.",
    author="J. Nathanael Philipp",
    author_email="nathanael@philipp.land",
    url="http://github.com/jnphilipp/django_bootstrap5",
    keywords=["django", "Bootstrap", "Bootstrap5"],
    packages=[
        "django_bootstrap5",
        "django_bootstrap5.templatetags",
    ],
    package_data={
        "django_bootstrap5": [
            "static/*",
            "static/css/*",
            "static/css/images/*",
            "static/js/*",
            "static/js/i18n/*",
            "templates/bootstrap/*",
            "templates/bootstrap/form/*",
        ],
    },
    include_package_data=True,
    long_description=read_file("README.md"),
    long_description_content_type="text/plain",
    zip_safe=True,
    install_requires=[],
    tests_require=[],
    python_requires=">=3.8",
    license="GPL",
    platforms=["any"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
