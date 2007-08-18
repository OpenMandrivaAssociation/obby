%define name   obby  
%define major   0.4
%define libname %mklibname obby %major
%define libname_devel %mklibname obby %major -d

Summary:    A library which provides synced document buffers
Name:       %{name}
Version:    0.4.4
Release:    %mkrel 1
URL:        http://gobby.0x539.de/
License:    GPL
Source0:    http://releases.0x539.de/%{name}/%{name}-%{version}.tar.bz2
Group:      System/Libraries
BuildRequires: sigc++2.0-devel gmpxx-devel
BuildRequires: libnet6-devel howl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description 
%{libname} is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.

%package -n %libname
Summary:    A library to ease the development of network-based applications
Group:      System/Libraries

%description -n %libname
%{libname} is a library which provides synced document buffers. It supports
multiple documents in one session and is portable to both Windows and
Unix-like platforms.

%package -n %libname_devel
Summary:    Development files for %libname
Group:      System/Libraries
Provides:   lib%{name}-devel
Requires:   %libname = %version
%description -n %libname_devel
Development files, header and includes for %libname.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --with-zeroconf --enable-ipv6
%make

%install
rm -Rf $RPM_BUILD_ROOT
%makeinstall_std
# remove translation, do not know where to place it 
rm -Rf $RPM_BUILD_ROOT/%_datadir/ 

%clean
rm -Rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root,-)
%doc ChangeLog README TODO NEWS AUTHORS 
%_libdir/*.so.*

%files -n %libname_devel
%defattr(-,root,root,-)
%_includedir/%name/
%_libdir/*.so
%_libdir/*.la
%_libdir/*.a
%_libdir/pkgconfig/*
