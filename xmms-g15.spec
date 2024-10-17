Name:                   xmms-g15
Version:                2.5.4
Release:                %mkrel 5
Summary:                Very simple spectrum analyzer for XMMS
License:                GPL
Group:                  System/Configuration/Hardware
URL:                    https://g15daemon.sourceforge.net/
Source0:                http://downloads.sourceforge.net/g15daemon/g15daemon-xmms-%{version}.tar.bz2
Provides:               g15daemon-xmms = %{version}-%{release}
Requires:               xmms
BuildRequires:          g15-devel
BuildRequires:          g15daemon_client-devel
BuildRequires:          g15render-devel
BuildRequires:          xmms-devel
BuildRoot:              %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A very simple spectrum analyzer for XMMS.
Improvements and patches are welcome.

This plugin depends on glib devel and xmms + X11 devel packages.

%prep
%setup -q -n g15daemon-xmms-%{version}
./autogen.sh

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} %{buildroot}%{_libdir}/xmms/Visualization/*.a
%{__rm} %{buildroot}%{_libdir}/xmms/Visualization/*.la

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
%defattr(-,root,root,0755)
%{_libdir}/xmms/Visualization/libg15daemon_xmms_spectrum.so
