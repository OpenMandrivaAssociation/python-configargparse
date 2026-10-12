%define module configargparse
%define oname ConfigArgParse

Name:		python-configargparse
Version:	1.7.5
Release:	2
License:	MIT
Group:		Development/Python
Summary:	A drop-in replacement for argparse
URL:		https://pypi.org/project/configargparse/
Source0:	https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
A drop-in replacement for argparse with added support for
config filesand environment variables.

%prep -a
# Remove bundled egg-info
rm -rf ConfigArgParse.egg-info

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{py_sitedir}/%{module}.py
%{py_sitedir}/%{oname}-%{version}*.*-info
