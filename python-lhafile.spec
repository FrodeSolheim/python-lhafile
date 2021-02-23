%define name python-lhafile
%define version 0.2.2
%define unmangled_version 0.2.2
%define release 1

Summary: LHA archive support for Python
Group: Development/Libraries
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source0: %{name}-%{unmangled_version}.tar.gz
License: BSD-3-Clause
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Frode Solheim <frode@solheim.dev>
Url: https://github.com/FrodeSolheim/python-lhafile
BuildRequires: python3-devel fdupes

%description
This project is an updated version of the project found at
http://trac.neotitans.net/wiki/lhafile. It is primarily used as a component
in FS-UAE Launcher to index and extract files from .lha archives. The project
consists of a Python package (lhafile) and a C extension for Python (lzhlib).

%package -n python3-lhafile
Summary: LHA archive support for Python
Group: Development/Libraries

%description -n python3-lhafile
This project is an updated version of the project found at
http://trac.neotitans.net/wiki/lhafile. It is primarily used as a component
in FS-UAE Launcher to index and extract files from .lha archives. The project
consists of a Python package (lhafile) and a C extension for Python (lzhlib).

%prep
%setup -n %{name}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build

%install
%{__python3} setup.py install -O1 \
--prefix=%{_prefix} \
--root=$RPM_BUILD_ROOT
%fdupes %{buildroot}/%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-lhafile
%defattr(-,root,root)
%{python3_sitearch}/*
