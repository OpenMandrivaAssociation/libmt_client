%define name libmt_client
%define version 0.1.98
%define release %mkrel 7
%define major 0
%define libname %mklibname mt_client %major

Summary: The Maitretarot client library
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Games/Cards
Source: http://www.nongnu.org/download/maitretarot/devel.pkg/%{version}/%{name}-%{version}.tar.bz2
URL: http://www.nongnu.org/maitretarot/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: glib2-devel
BuildRequires: libmaitretarot-devel

%description
Maitretarot is a tarot server game. Libmt_client is a library
for the client.

%description -l fr
Maitretarot est le serveur pour un jeu de tarot. Libmt_client
est une biblothèque pour les logiciels client.

%package -n %libname
Summary: The Maitretarot client library
Group: System/Libraries
Provides: %name = %version-%release

%description -n %libname
Maitretarot is a tarot server game. Libmt_client is a library
for any client.

%description -n %libname -l fr
Maitretarot est le serveur pour un jeu de tarot. Libmt_client
est une biblothèque pour les logiciels client.

%package -n %libname-devel
Summary: Development files from Libmaitretarot
Group: System/Libraries
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %libname-devel
This package is need to build application wich use Libmt_client.

%description -n %libname-devel -l fr
Ce package est utilisé pour compiler les applications qui utilise 
Libmt_client.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_libdir}/*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/mt_client.h



