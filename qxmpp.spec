Name:       qxmpp
Version:    0.3.45.1
Release:    1%{?dist}.R
License:    LGPLv2+
Source0:    https://github.com/downloads/0xd34df00d/qxmpp-dev/%{name}-%{version}-extras.tar.bz2
Patch0:     qxmpp.patch
Patch1:     qxmpp-dynamiclib.patch
Group:      Development/Libraries
Summary:    Qt XMPP Library
URL:        http://github.com/0xd34df00d/qxmpp-dev 

BuildRequires:  qt-devel
BuildRequires:  speex-devel

%description
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

This package's the fork of QXmpp for Leechcraft Internet Client

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt is the only
third party library it is dependent on. Users need to a have working knowledge of
C++ and Qt basics (Signals and Slots and Qt data types). The underlying TCP socket
and the XMPP RFCs (RFC3920 and RFC3921) have been encapsulated into classes and
functions. Therefore the user would not be bothered with these details. But it is
always recommended to the advanced users to read and enjoy the low level details.

%package devel
Summary:      QXmpp Development Files
Group:        Development/Libraries

%description devel
It's a development package for qxmpp.

QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

%prep
%setup -q -n %{name}-%{version}
%patch0
%patch1

%build
%{_qt4_qmake} PREFIX=/usr
make %{?_smp_mflags} 

%install
make install INSTALL_ROOT=%{buildroot}
%ifarch x86_64
%__mv %{buildroot}/usr/{lib,lib64}
%endif

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig
 
%files 
%defattr(-,root,root,-)
%{_libdir}/libqxmpp.so.*

%files devel
%doc AUTHORS CHANGELOG LICENSE.LGPL README
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
 
%changelog
* Tue Aug 02 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1
- dynamic libs

* Mon Jul 25 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1
- new version

* Mon Jun 06 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.44-0.1.pre21062011
- initial build 
