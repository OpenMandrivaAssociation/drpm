%global _hardened_build 1

%define major 0
%define oldlibname %mklibname %name 0
%define libname %mklibname %name
%define libname_devel %mklibname -d %name

Name:		drpm
Version:	0.5.2
Release:	2
Summary:	A small library for fetching information from DeltaRPM packages
Group:		System/Libraries
License:	LGPLv2+
URL:		https://github.com/rpm-software-management/%{name}
Source0:	https://github.com/rpm-software-management/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(rpm)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	cmake >= 2.8
BuildRequires:	pkgconfig(cmocka) >= 1.0
%ifnarch %{armx} %{riscv}
BuildRequires:	valgrind
%endif
BuildRequires:	doxygen

%package -n %{libname}
Summary:	A small library for fetching information from DeltaRPM packages
Group:		System/Libraries
%rename %{oldlibname}

%package -n %{libname_devel}
Summary:	C interface for the drpm library
Group:		Development/C
Provides:	%{name}-devel%{?_isa} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname}%{?_isa} = %{version}-%{release}

%description
The drpm package provides a small library allowing one to fetch
various info from DeltaRPM packages.

%description -n %{libname}
This package provides a small library allowing one to fetch
information from DeltaRPM packages.

%description -n %{libname_devel}
This package provides a C interface (drpm.h) for the drpm library.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DINCLUDE_INSTALL_DIR=%{_includedir} -DWITH_ZSTD:BOOL=ON
%make_build

%install
cd ./build
%make_install
cd -

%files -n %{libname}
%{_libdir}/libdrpm.so.%{major}
%{_libdir}/libdrpm.so.%{major}.*
%license COPYING

%files -n %{libname_devel}
%{_libdir}/libdrpm.so
%{_includedir}/drpm.h
%{_libdir}/pkgconfig/drpm.pc
