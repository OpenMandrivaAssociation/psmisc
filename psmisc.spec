Summary:	Utilities for managing processes on your system
Name:		psmisc
Version:	22.2
Release:	%mkrel 2
License:	GPL
Group:		Monitoring
Url:		http://psmisc.sourceforge.net/
BuildRequires:	ncurses-devel
Source0:	http://download.sourceforge.net/psmisc/%{name}-%{version}.tar.bz2
Patch1:		psmisc-21.9-libsafe.patch.bz2
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
%configure

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir $RPM_BUILD_ROOT/sbin
mv $RPM_BUILD_ROOT%{_bindir}/fuser $RPM_BUILD_ROOT/sbin

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
/sbin/fuser
%{_bindir}/killall
%{_bindir}/pstree*
%{_bindir}/oldfuser
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/pstree.1*
