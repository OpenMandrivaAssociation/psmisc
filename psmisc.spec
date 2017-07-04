%bcond_with	crosscompile
%define _disable_rebuild_configure 1

Summary:	Utilities for managing processes on your system
Name:		psmisc
Version:	23.1
Release:	12
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
%setup -q
%apply_patches

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE"
%if %{with crosscompile}
export ac_cv_func_malloc_0_nonnull=yes
export ac_cv_func_realloc_0_nonnull=yes
%endif

%configure
%make

%install
%makeinstall_std

mkdir -p %{buildroot}/sbin
mv -f %{buildroot}%{_bindir}/fuser %{buildroot}/sbin

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
/sbin/fuser
%{_bindir}/killall
%{_bindir}/prtstat
%{_bindir}/pstree*
%{_bindir}/pslog
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/prtstat.1*
%{_mandir}/man1/pstree.1*
%{_mandir}/man1/pslog.1*
#need patch for aarch64
%ifnarch aarch64
%{_bindir}/peekfd
%endif
%{_mandir}/man1/peekfd.1*
