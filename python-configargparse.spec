Name:		python-configargparse
Version:	1.5.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/configargparse/ConfigArgParse-%{version}.tar.gz
Summary:	A drop-in replacement for argparse that allows options to also be set via config files and/or environment variables.
URL:		https://pypi.org/project/configargparse/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
A drop-in replacement for argparse that allows options to also be set via config files and/or environment variables.

%prep
%autosetup -p1 -n ConfigArgParse-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/configargparse.py
%{py_sitedir}/ConfigArgParse-*.*-info
