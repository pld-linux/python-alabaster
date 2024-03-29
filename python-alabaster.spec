#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	alabaster
Summary:	A configurable sidebar-enabled Sphinx theme
Summary(pl.UTF-8):	Konfigurowany motyw z bocznym panelem dla Sphinksa
Name:		python-%{module}
Version:	0.7.12
Release:	6
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/alabaster/
Source0:	https://files.pythonhosted.org/packages/source/a/alabaster/%{module}-%{version}.tar.gz
# Source0-md5:	3591827fde96d1dd23970fb05410ed04
URL:		https://pypi.org/project/alabaster/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools >= 1:7.0
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools >= 1:7.0
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A configurable sidebar-enabled Sphinx theme.

This theme is a modified "Kr" Sphinx theme from @kennethreitz
(especially as used in his Requests project), which was itself
originally based on @mitsuhiko's theme used for Flask & related
projects.

%description -l pl.UTF-8
Konfigurowany motyw z bocznym panelem (sidebarem) dla Sphinksa.

Motyw ten to zmodyfikowany motyw Sphinksa "Kr" od @kennethreitz
(konkretnie wersja używana w jego projekcie Requests), pierwotnie
oparty na motywie @mitsuhiko używanym w projekcie Flash i powiązanych
z nim.

%package -n python3-%{module}
Summary:	A configurable sidebar-enabled Sphinx theme
Summary(pl.UTF-8):	Konfigurowany motyw z bocznym panelem dla Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
A configurable sidebar-enabled Sphinx theme

This theme is a modified "Kr" Sphinx theme from @kennethreitz
(especially as used in his Requests project), which was itself
originally based on @mitsuhiko's theme used for Flask & related
projects.

%description -n python3-%{module} -l pl.UTF-8
Konfigurowany motyw z bocznym panelem (sidebarem) dla Sphinksa.

Motyw ten to zmodyfikowany motyw Sphinksa "Kr" od @kennethreitz
(konkretnie wersja używana w jego projekcie Requests), pierwotnie
oparty na motywie @mitsuhiko używanym w projekcie Flash i powiązanych
z nim.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
