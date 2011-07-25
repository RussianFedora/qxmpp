Name:       qxmpp
Version:    0.3.45.1
Release:    0.1%{?dist}.R
License:    LGPLv2+
Source:     https://github.com/downloads/0xd34df00d/qxmpp-dev/%{name}-%{version}-extras.tar.bz2
Patch:      qxmpp.patch
Group:      Development/Libraries
Summary:    Qt XMPP library
URL:        http://github.com/0xd34df00d/qxmpp-dev 
BuildRequires:  gcc-c++
BuildRequires:  qt-devel
 
%description
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

This package's the fork of QXmpp for Leechcraft Internet Client

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt is the only
third party library it is dependent on. Users need to a have working knowledge of
C++ and Qt basics (Signals and Slots and Qt data types). The underlying TCP socket
and the XMPP RFCs (RFC3920 and RFC3921) have been encapsulated into classes and
functions. Therefore the user would not be bothered with these details. But it is
always recommended to the advanced users to read and enjoy the low level details.
 
%prep
%setup -q -n %{name}-%{version}
%patch -p 0

%build
%{_qt4_qmake} PREFIX=/usr
make %{?_smp_mflags} 

%install
make install INSTALL_ROOT=%{buildroot}
%ifarch x86_64
%__mv %{buildroot}/usr/{lib,lib64}
%endif
 
%files 
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG LICENSE.LGPL README
%{_libdir}/lib%{name}.a
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
 
%changelog
* Mon Jul 25 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1
- new version
* Mon Jun 06 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.44-0.1.pre21062011
- initial build 
