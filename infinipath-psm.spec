Summary: QLogic PSM Libraries
Name: infinipath-psm
Version: 1.13
Release: 2%{?dist}
License: BSD or GPLv2
ExclusiveArch: x86_64
Group: System Environment/Libraries
URL: http://www.qlogic.com/
Source0: %{name}-%{version}.tar.gz
Prefix: /usr
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: libuuid >= 2.17.2-3.el6
Conflicts: infinipath-libs

%package devel
Summary: Development files for QLogic PSM
Group: System Environment/Development
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: libuuid-devel >= 2.17.2-3.el6
Conflicts: infinipath-devel

%description
The PSM Messaging API, or PSM API, is QLogic's low-level
user-level communications interface for the Truescale
family of products. PSM users are enabled with mechanisms
necessary to implement higher level communications
interfaces in parallel environments.

%description devel
Development files for the libpsm_infinipath library

%prep
%setup -q

%build
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libpsm_infinipath.so.*
%{_libdir}/libinfinipath.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libpsm_infinipath.so
%{_libdir}/libinfinipath.so
%{_includedir}/psm.h
%{_includedir}/psm_mq.h


%changelog
* Thu Jun 3 2010 Jay Fenlason <fenlason@redhat.com> - 1.13-2
- Use macros for lib and include directories, and include dist tag in
  release field.
- Corrected License field.
- Corrected Requires lines for libuuid.
- Add Exclusive-arch x86_64
  Related: rhbz570274

* Tue May 11 2010 Mitko Haralanov <mitko@qlogic.com> - 1.13-1
- Initial build.

