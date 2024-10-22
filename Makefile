ARCH=x86_64
OS_VERSION=fc40
PACKAGE=atuin
PACKAGE_VERSION=18.3.0

all: spec rpm install

spec: rust2rpm.toml
	rust2rpm -V -s $(PACKAGE) $(PACKAGE_VERSION)
	mv -f rust-$(PACKAGE).spec $(PACKAGE).spec

rpm: spec
	mkdir -p $(HOME)/rpmbuild/SOURCES
	cp -f $(PACKAGE)-$(PACKAGE_VERSION).crate $(HOME)/rpmbuild/SOURCES
	cp -f $(PACKAGE)-$(PACKAGE_VERSION)-vendor.tar.xz $(HOME)/rpmbuild/SOURCES
	export MAKE_PWD=$(shell pwd)
	rpmbuild --define "make_pwd_ ${MAKE_PWD}" -bb ./$(PACKAGE).spec
	unset MAKE_PWD

install: rpm
	sudo dnf install -y $(HOME)/rpmbuild/RPMS/$(ARCH)/$(PACKAGE)-$(PACKAGE_VERSION)-1.$(OS_VERSION).$(ARCH).rpm

uninstall:
	sudo dnf remove -y atuin

tools:
	sudo dnf install -y rustc cargo rust2rpm rpm-build postgresql-test-rpm-macros protobuf-devel

clean:
	sudo rm -rf *.spec *.crate *.tar.gz *.tar.xz
