Summary:	Utilities for managing processes on your system
Name:		psmisc
Version:	22.5
Release:	%mkrel 1
License:	GPL
Group:		Monitoring
Url:		http://psmisc.sourceforge.net/
Source0:	http://download.sourceforge.net/psmisc/%{name}-%{version}.tar.bz2
Patch1:		%{name}-22.5-libsafe.patch
BuildRequires:	ncurses-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser.  The pstree command displays a tree
structure of all of the running processes on your system.  The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name.  The fuser command identifies the PIDs
of processes that are using specified files or filesystems.

%prep
%setup -q 
%patch1 -p1

%build
%configure2_5x \
	--disable-rpath

%make

%install
rm -rf %{buildroot}

%makeinstall_std

mkdir %{buildroot}/sbin
mv %{buildroot}%{_bindir}/fuser %{buildroot}/sbin

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
/sbin/fuser
%{_bindir}/peekfd
%{_bindir}/killall
%{_bindir}/pstree*
%{_bindir}/oldfuser
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/pstree.1*
%{_mandir}/man1/peekfd.1.*
