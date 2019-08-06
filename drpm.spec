%global _hardened_build 1

%define major 0
%define libname %mklibname %name %major
%define libname_devel %mklibname -d %name

Name:           drpm
Version:        0.3.0
Release:        %mkrel 3
Summary:        A small library for fetching information from DeltaRPM packages
Group:          System/Libraries
License:        LGPLv3+
URL:            http://fedorahosted.org/%{name}
Source0:        http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  rpm-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  bzip2-devel
BuildRequires:  lzma-devel
BuildRequires:  pkgconfig(openssl)

BuildRequires:  cmake >= 2.8
BuildRequires:  pkgconfig(cmocka) >= 1.0
%ifnarch %{armx} %{riscv}
BuildRequires:  valgrind
%endif
BuildRequires:  doxygen

%package -n %{libname}
Summary:        A small library for fetching information from DeltaRPM packages
Group:          System/Libraries

%package -n %{libname_devel}
Summary:        C interface for the drpm library
Group:          Development/C
Provides:       %{name}-devel%{?_isa} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description
The drpm package provides a small library allowing one to fetch
various info from DeltaRPM packages.

%description -n %{libname}
This package provides a small library allowing one to fetch
information from DeltaRPM packages.

%description -n %{libname_devel}
This package provides a C interface (drpm.h) for the drpm library.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DINCLUDE_INSTALL_DIR=%{_includedir}
%make_build

%install
pushd ./build
%make_install
popd

%check
pushd ./build
ctest -VV
popd

%files -n %{libname}
%{_libdir}/libdrpm.so.%{major}
%{_libdir}/libdrpm.so.%{major}.*
%license COPYING COPYING.LESSER

%files -n %{libname_devel}
%{_libdir}/libdrpm.so
%{_includedir}/drpm.h
%{_libdir}/pkgconfig/drpm.pc
