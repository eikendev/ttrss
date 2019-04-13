%global pythonv python3
%global srcname ttrss

Name:           %{srcname}
Version:        1.1.1
Release:        1%{?dist}
Summary:        A tool for synchronizing feeds from a Tiny Tiny RSS server
License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
#Source0:        %%pypi_source
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{pythonv}-devel
BuildRequires:  %{pythonv}-setuptools
BuildRequires:  %{pythonv}-setuptools_scm
Requires:       %{pythonv}-keyring
Requires:       %{pythonv}-requests

%description
%{summary}.

%prep
%autosetup

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.rst
%doc data/config-example.ini
%{_bindir}/%{srcname}
%{python3_sitelib}/*

%changelog
* Sat Apr 13 2019 eikendev <raphael@eiken.dev> - 1.1.1-1
- Initial package
