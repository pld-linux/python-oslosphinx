#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_with	tests	# test target

Summary:	OpenStack Sphinx extensions
Summary(pl.UTF-8):	Rozszerzenia modułu Sphinx z projektu OpenStack
Name:		python-oslosphinx
Version:	4.3.0
Release:	6
License:	Apache v2.0
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/oslosphinx/
Source0:	https://pypi.python.org/packages/source/o/oslosphinx/oslosphinx-%{version}.tar.gz
# Source0-md5:	5670ad4369ef54b67a3a4002bcbe091c
URL:		http://www.openstack.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pbr >= 1.8
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.1.2
BuildRequires:	python-hacking >= 0.10.0
BuildRequires:	python-hacking < 0.11
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-pbr >= 1.8
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.1.2
BuildRequires:	python3-hacking >= 0.10.0
BuildRequires:	python3-hacking < 0.11
%endif
%endif
Requires:	python-modules >= 1:2.7
Requires:	python-pbr >= 1.6
Requires:	python-requests >= 2.8.1
Requires:	python-six >= 1.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Theme and extension support for Sphinx documentation from the
OpenStack project.

%description -l pl.UTF-8
Motyw oraz rozszerzenia wspomagające tworzenie dokumentacji w systemie
Sphinx w projekcie OpenStack.

%package -n python3-oslosphinx
Summary:	OpenStack Sphinx extensions
Summary(pl.UTF-8):	Rozszerzenia modułu Sphinx z projektu OpenStack
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-pbr >= 1.6
Requires:	python3-requests >= 2.8.1
Requires:	python3-six >= 1.9.0

%description -n python3-oslosphinx
Theme and extension support for Sphinx documentation from the
OpenStack project.

%description -n python3-oslosphinx -l pl.UTF-8
Motyw oraz rozszerzenia wspomagające tworzenie dokumentacji w systemie
Sphinx w projekcie OpenStack.

%prep
%setup -q -n oslosphinx-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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
