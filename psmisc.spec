%global optflags %{optflags} -Oz

%bcond_with crosscompile
%define _disable_rebuild_configure 1

Summary:	Utilities for managing processes on your system
Name:		psmisc
Version:	23.6
Release:	2
License:	GPLv2+
Group:		Monitoring
Url:		http://psmisc.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/psmisc/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(ncursesw)

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser.  The pstree command displays a tree
structure of all of the running processes on your system.  The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name.  The fuser command identifies the PIDs
of processes that are using specified files or filesystems.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE"
%if %{with crosscompile}
export ac_cv_func_malloc_0_nonnull=yes
export ac_cv_func_realloc_0_nonnull=yes
%endif

%configure
%make_build

%install
%make_install

%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/fuser
%{_bindir}/killall
%{_bindir}/prtstat
%{_bindir}/pstree*
%{_bindir}/pslog
%doc %{_mandir}/man1/fuser.1*
%doc %{_mandir}/man1/killall.1*
%doc %{_mandir}/man1/prtstat.1*
%doc %{_mandir}/man1/pstree.1*
%doc %{_mandir}/man1/pslog.1*
#need patch for riscv64
%ifnarch riscv64
%{_bindir}/peekfd
%endif
%doc %{_mandir}/man1/peekfd.1*
