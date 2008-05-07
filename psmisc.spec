Summary:        Utilities for managing processes on your system
Name:           psmisc
Version:        22.6
Release:        %mkrel 3
License:        GPLv2+
Group:          Monitoring
URL:            http://psmisc.sourceforge.net/
Source0:        http://superb-east.dl.sourceforge.net/sourceforge/psmisc/psmisc-%{version}.tar.gz
Patch0:		%{name}-22.6-peekfd64.patch
Patch1:         %{name}-22.5-libsafe.patch
Patch2:		%{name}-22.6-pstree-overflow.patch
BuildRequires:  ncurses-devel
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf
export CFLAGS="%{optflags} -D_GNU_SOURCE"

%{configure2_5x} \
        --disable-rpath
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%{__mkdir_p} %{buildroot}/sbin
%{__mv} %{buildroot}%{_bindir}/fuser %{buildroot}/sbin

%ifnarch %ix86 x86_64 ppc ppc64 sparc
%{__rm} -f %{buildroot}%{_mandir}/man1/peekfd.1*
%endif

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
/sbin/fuser
%{_bindir}/killall
%{_bindir}/pstree*
%{_bindir}/oldfuser
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/pstree.1*
%ifarch %ix86 x86_64 ppc ppc64 sparc
%{_bindir}/peekfd
%{_mandir}/man1/peekfd.1.*
%endif
