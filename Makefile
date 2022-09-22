SHELL:=/bin/bash

DOC_DIR?=/usr/share/doc
SHARE_DIR?=/usr/share
DEST_DIR?=

FILES := $(shell find django_bootstrap5/* -type f ! -path "**/__pycache__")


ifdef VERBOSE
  Q :=
else
  Q := @
endif


clean:
	$(Q)rm -rf ./build
	$(Q)rm -rf ./django_bootstrap5.egg-info
	$(Q)find django_bootstrap5 -depth -name __pycache__ -exec rm -rf {} \;


print-%:
	@echo $*=$($*)


deb: build/package/DEBIAN/control
	$(Q)fakeroot dpkg-deb -b build/package build/python-django-bootstrap5.deb
	$(Q)lintian -Ivi --suppress-tags embedded-javascript-library,font-outside-font-dir,font-in-non-font-package build/python-django-bootstrap5.deb
	@echo "python-django-bootstrap5.deb completed."


deb-sig: deb
	$(Q)dpkg-sig -s builder build/python-django-bootstrap5.deb
	@echo "Signed python-django-bootstrap5.deb."


install: build/copyright build/changelog.Debian.gz build/package/DEBIAN
	$(Q)python setup.py build
	$(Q)python setup.py install --root="${DEST_DIR}/" --optimize=1 --skip-build

	$(Q)install -Dm 0644 build/changelog.Debian.gz "${DEST_DIR}${DOC_DIR}"/python-django-bootstrap5/changelog.Debian.gz
	$(Q)install -Dm 0644 build/copyright "${DEST_DIR}${DOC_DIR}"/python-django-bootstrap5/copyright

	@echo "python-django-bootstrap5 install completed."


uninstall:
	$(Q)python setup.py build
	$(Q)python setup.py install --root="build/tmp/" --optimize=1 --skip-build --record build/files.txt
	$(Q)xargs rm -r < build/files.txt
	$(Q)rm -r "${DEST_DIR}${DOC_DIR}"/python-django-bootstrap5
	@echo "python-django-bootstrap5 uninstall completed."


build:
	$(Q)mkdir -p build


build/package/DEBIAN: build
	@mkdir -p build/package/DEBIAN


build/copyright: build
	$(Q)echo "Upstream-Name: django_bootstrap5" > build/copyright
	$(Q)echo "Source: https://github.com/jnphilipp/django_bootstrap5" >> build/copyright
	$(Q)echo "" >> build/copyright
	$(Q)echo "Files: *" >> build/copyright
	$(Q)echo "Copyright: 2014-2022 J. Nathanael Philipp (jnphilipp) <nathanael@philipp.land>" >> build/copyright
	$(Q)echo "License: GPL-3+" >> build/copyright
	$(Q)echo " This program is free software: you can redistribute it and/or modify" >> build/copyright
	$(Q)echo " it under the terms of the GNU General Public License as published by" >> build/copyright
	$(Q)echo " the Free Software Foundation, either version 3 of the License, or" >> build/copyright
	$(Q)echo " any later version." >> build/copyright
	$(Q)echo "" >> build/copyright
	$(Q)echo " This program is distributed in the hope that it will be useful," >> build/copyright
	$(Q)echo " but WITHOUT ANY WARRANTY; without even the implied warranty of" >> build/copyright
	$(Q)echo " MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the" >> build/copyright
	$(Q)echo " GNU General Public License for more details." >> build/copyright
	$(Q)echo "" >> build/copyright
	$(Q)echo " You should have received a copy of the GNU General Public License" >> build/copyright
	$(Q)echo " along with this program. If not, see <http://www.gnu.org/licenses/>." >> build/copyright
	$(Q)echo " On Debian systems, the full text of the GNU General Public" >> build/copyright
	$(Q)echo " License version 3 can be found in the file" >> build/copyright
	$(Q)echo " '/usr/share/common-licenses/GPL-3'." >> build/copyright


build/changelog.Debian.gz: build
	$(Q)( \
		declare TAGS=(`git tag`); \
		for ((i=$${#TAGS[@]};i>=0;i--)); do \
			if [ $$i -eq 0 ]; then \
				echo -e "django_bootstrap5 ($${TAGS[$$i]}) unstable; urgency=medium" >> build/changelog; \
				git log $${TAGS[$$i]} --no-merges --format="  * %h %s"  >> build/changelog; \
				git log $${TAGS[$$i]} -n 1 --format=" -- %an <%ae>  %aD" >> build/changelog; \
			elif [ $$i -eq $${#TAGS[@]} ] && [ $$(git log $${TAGS[$$i-1]}..HEAD --oneline | wc -l) -ne 0 ]; then \
				echo -e "django_bootstrap5 ($${TAGS[$$i-1]}-$$(git log -n 1 --format='%h')) unstable; urgency=medium" >> build/changelog; \
				git log $${TAGS[$$i-1]}..HEAD --no-merges --format="  * %h %s"  >> build/changelog; \
				git log HEAD -n 1 --format=" -- %an <%ae>  %aD" >> build/changelog; \
			elif [ $$i -lt $${#TAGS[@]} ]; then \
				echo -e "django_bootstrap5 ($${TAGS[$$i]}) unstable; urgency=medium" >> build/changelog; \
				git log $${TAGS[$$i-1]}..$${TAGS[$$i]} --no-merges --format="  * %h %s"  >> build/changelog; \
				git log $${TAGS[$$i]} -n 1 --format=" -- %an <%ae>  %aD" >> build/changelog; \
			fi; \
		done \
	)
	$(Q)cat build/changelog | gzip -n9 > build/changelog.Debian.gz


changelog.latest.md:
	$(Q)( \
		declare TAGS=(`git tag`); \
		for ((i=$${#TAGS[@]};i>=0;i--)); do \
			if [ $$i -eq 0 ]; then \
				echo -e "$${TAGS[$$i]}" >> changelog.latest.md; \
				git log $${TAGS[$$i]} --no-merges --format="  * %h %s"  >> changelog.latest.md; \
			elif [ $$i -eq $${#TAGS[@]} ] && [ $$(git log $${TAGS[$$i-1]}..HEAD --oneline | wc -l) -ne 0 ]; then \
				echo -e "$${TAGS[$$i-1]}-$$(git log -n 1 --format='%h')" >> changelog.latest.md; \
				git log $${TAGS[$$i-1]}..HEAD --no-merges --format="  * %h %s"  >> changelog.latest.md; \
			elif [ $$i -lt $${#TAGS[@]} ]; then \
				echo -e "$${TAGS[$$i]}" >> changelog.latest.md; \
				git log $${TAGS[$$i-1]}..$${TAGS[$$i]} --no-merges --format="  * %h %s"  >> changelog.latest.md; \
				break; \
			fi; \
		done \
	)


build/package/DEBIAN/md5sums:
	$(Q)make install DEST_DIR=build/package
	$(Q)mkdir -p build/package/DEBIAN
	$(Q)find build/package -type f -not -path "*DEBIAN*" -exec md5sum {} \; > build/md5sums
	$(Q)sed -e "s/build\/package\///" build/md5sums > build/package/DEBIAN/md5sums
	$(Q)chmod 0644 build/package/DEBIAN/md5sums


build/package/DEBIAN/control: build/package/DEBIAN/md5sums
	$(Q)echo "Package: python-django-bootstrap5" > build/package/DEBIAN/control
	$(Q)echo "Version: `git describe --tags`-`git log --format=%h -1`" >> build/package/DEBIAN/control
	$(Q)echo "Section: python" >> build/package/DEBIAN/control
	$(Q)echo "Priority: optional" >> build/package/DEBIAN/control
	$(Q)echo "Architecture: all" >> build/package/DEBIAN/control
	$(Q)echo "Depends: python3 (<< 3.11), python3 (>= 3.7), python3:any" >> build/package/DEBIAN/control
	$(Q)echo "Installed-Size: `du -sk build/package/usr | grep -oE "[0-9]+"`" >> build/package/DEBIAN/control
	$(Q)echo "Maintainer: J. Nathanael Philipp (jnphilipp) <nathanael@philipp.land>" >> build/package/DEBIAN/control
	$(Q)echo "Homepage: https://github.com/jnphilipp/django_bootstrap5" >> build/package/DEBIAN/control
	$(Q)echo "Description: Bootstrap5 app for Django" >> build/package/DEBIAN/control
	$(Q)echo " Includes Bootstrap 5.2.1, jQuery 3.6.1, jQuery UI 1.13.2 and select2 4.0.13" >> build/package/DEBIAN/control
