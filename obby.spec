%define name   obby  
%define api 0.4
%define major   1
%define libname %mklibname obby %api %major
%define libname_devel %mklibname obby -d

Summary:    A library which provides synced document buffers
Name:       %{name}
Version:    0.4.8
Release:    2
URL:        http://gobby.0x539.de/
License:    GPLv2+
Source0:    http://releases.0x539.de/%{name}/%{name}-%{version}.tar.gz
Group:      System/Libraries
BuildRequires: pkgconfig(sigc++-2.0)
BuildRequires: gmpxx-devel
BuildRequires: pkgconfig(net6-1.3)
BuildRequires: pkgconfig(howl)

%description 
%{libname} is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.

%package -n %libname
Summary:    A library to ease the development of network-based applications
Group:      System/Libraries
Obsoletes:  %mklibname obby 0.4

%description -n %libname
%{libname} is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.

%package -n %libname_devel
Summary:    Development files for %libname
Group:      System/Libraries
Provides:   lib%{name}-devel = %version-%release
Requires:   %libname = %version
Obsoletes:  %mklibname -d obby 0.4

%description -n %libname_devel
Development files, header and includes for %libname.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --with-zeroconf --enable-ipv6
%make

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall_std
# remove translation, do not know where to place it 
rm -Rf $RPM_BUILD_ROOT/%_datadir/ 

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root,-)
%doc ChangeLog README TODO NEWS AUTHORS 
%_libdir/*-%{api}.so.%{major}*

%files -n %libname_devel
%defattr(-,root,root,-)
%_includedir/%name/
%_libdir/*.so
%_libdir/*.a
%_libdir/pkgconfig/*


%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.7-2mdv2010.0
+ Revision: 440359
- rebuild

* Fri Mar 06 2009 Michael Scherer <misc@mandriva.org> 0.4.7-1mdv2009.1
+ Revision: 349847
- update to 0.4.7

* Tue Nov 11 2008 Funda Wang <fundawang@mandriva.org> 0.4.6-1mdv2009.1
+ Revision: 302058
- fix libname
- Neew version 0.4.6

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.5-3mdv2009.0
+ Revision: 254157
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 27 2008 Funda Wang <fundawang@mandriva.org> 0.4.5-1mdv2008.1
+ Revision: 158585
- New version 0.4.5

* Fri Jan 25 2008 Funda Wang <fundawang@mandriva.org> 0.4.4-2mdv2008.1
+ Revision: 157804
- new devel package policy

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 18 2007 Michael Scherer <misc@mandriva.org> 0.4.4-1mdv2008.0
+ Revision: 66423
- new version
- Import obby



* Sat Sep 23 2006 Michael Scherer <misc@mandriva.org> 0.4.1-2mdv2007.0
- enable zeroconf, ipv6

* Mon Sep 04 2006 Michael Scherer <misc@mandriva.org> 0.4.1-1mdv2007.0
- New version 0.4.1

* Tue Dec 20 2005 Michael Scherer <misc@mandriva.org> 0.3.0-1mdk
- New release 0.3.0

* Fri Dec 16 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.0-0.rc3.1mdk
- New release 0.3.0rc3

* Thu Nov 10 2005 Michael Scherer <misc@mandriva.org> 0.2.1-1mdk
- New release 0.2.1

* Fri Nov 04 2005 Michael Scherer <misc@mandriva.org> 0.2.0-1mdk
- first package 
