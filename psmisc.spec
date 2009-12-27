Summary:        Utilities for managing processes on your system
Name:           psmisc
Version:        22.9
Release:        %mkrel 1
License:        GPLv2+
Group:          Monitoring
URL:            http://psmisc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/psmisc/%{name}/%{name}-%{version}.tar.gz
# Fix building of peekfd on x86_64
# http://bugs.archlinux.org/task/14514
Patch0:		%{name}-22.7-checkregs-fix.patch
BuildRequires:  ncurses-devel
# For patch0
BuildRequires:	gettext-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser.  The pstree command displays a tree
structure of all of the running processes on your system.  The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name.  The fuser command identifies the PIDs
of processes that are using specified files or filesystems.

%prep
%setup -q
%patch0 -p0 -b .header

%build
# for patch0
autoreconf -fis
export CFLAGS="%{optflags} -D_GNU_SOURCE"

%{configure2_5x} \
        --disable-rpath
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{__mkdir_p} %{buildroot}/sbin
%{__mv} %{buildroot}%{_bindir}/fuser %{buildroot}/sbin

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
/sbin/fuser
%{_bindir}/killall
%{_bindir}/prtstat
%{_bindir}/pstree*
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/prtstat.1*
%{_mandir}/man1/pstree.1*
%{_bindir}/peekfd
%{_mandir}/man1/peekfd.1*
