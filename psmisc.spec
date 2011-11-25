Summary:        Utilities for managing processes on your system
Name:           psmisc
Version:        22.14
Release:        %mkrel 2
License:        GPLv2+
Group:          Monitoring
URL:            http://psmisc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/psmisc/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

# can be dropped once 22.15 will be released.
Patch0:		fuser-fix--s-option.patch

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser.  The pstree command displays a tree
structure of all of the running processes on your system.  The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name.  The fuser command identifies the PIDs
of processes that are using specified files or filesystems.

%prep
%setup -q
%patch0 -p1

%build
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
