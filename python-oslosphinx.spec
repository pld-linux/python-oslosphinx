#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (not included in dist tarball?)

Summary:	OpenStack Sphinx extensions
Summary(pl.UTF-8):	Rozszerzenia modułu Sphinx z projektu OpenStack
Name:		python-oslosphinx
Version:	4.18.0
Release:	2
License:	Apache v2.0
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/oslosphinx/
Source0:	https://files.pythonhosted.org/packages/source/o/oslosphinx/oslosphinx-%{version}.tar.gz
# Source0-md5:	f2e63063eeae74ca0f92452d964b9b5c
URL:		http://www.openstack.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-hacking >= 0.12.0
BuildRequires:	python-hacking < 0.14
BuildRequires:	python-requests >= 2.14.2
BuildRequires:	python-six >= 1.10.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-hacking >= 0.12.0
BuildRequires:	python3-hacking < 0.14
BuildRequires:	python3-requests >= 2.14.2
BuildRequires:	python3-six >= 1.10.0
%endif
%endif
%if %{with doc}
BuildRequires:	python3-openstackdocstheme >= 1.17.0
BuildRequires:	python3-reno >= 2.5.0
BuildRequires:	sphinx-pdg-3 >= 1.6.2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Theme and extension support for Sphinx documentation from the
OpenStack project.

Note: this package is obsolete, the openstackdocstheme module should
be used instead.

%description -l pl.UTF-8
Motyw oraz rozszerzenia wspomagające tworzenie dokumentacji w systemie
Sphinx w projekcie OpenStack.

Uwaga: ten pakiet jest przestarzały, zamiast niego należy używać
modułu openstackdocstheme.

%package -n python3-oslosphinx
Summary:	OpenStack Sphinx extensions
Summary(pl.UTF-8):	Rozszerzenia modułu Sphinx z projektu OpenStack
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-oslosphinx
Theme and extension support for Sphinx documentation from the
OpenStack project.

Note: this package is obsolete, the openstackdocstheme module should
be used instead.

%description -n python3-oslosphinx -l pl.UTF-8
Motyw oraz rozszerzenia wspomagające tworzenie dokumentacji w systemie
Sphinx w projekcie OpenStack.

Uwaga: ten pakiet jest przestarzały, zamiast niego należy używać
modułu openstackdocstheme.

%package apidocs
Summary:	API documentation for Python oslosphinx module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona oslosphinx
Group:		Documentation

%description apidocs
API documentation for Python oslosphinx module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona oslosphinx.

%prep
%setup -q -n oslosphinx-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%if %{with doc}
sphinx-build-3 -b html doc/source doc/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/oslosphinx
%{py_sitescriptdir}/oslosphinx-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-oslosphinx
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/oslosphinx
%{py3_sitescriptdir}/oslosphinx-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,*.html,*.js}
%endif
