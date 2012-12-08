Summary:        Utilities for managing processes on your system
Name:           psmisc
Version:        22.13
Release:        %mkrel 3
License:        GPLv2+
Group:          Monitoring
URL:            http://psmisc.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/psmisc/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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


%changelog
* Mon Dec 19 2011 Oden Eriksson <oeriksson@mandriva.com> 22.13-3.1
- built for updates

* Fri Nov 25 2011 Franck Bui <franck.bui@mandriva.com> 22.13-3mdv2011.0
+ Revision: 733324
- Fix fuser '-s' option which return incorrect value in some cases
  The patch is a backport from 06c3bb5ca810e6262c39ea476e2dfa80aa788b20 of the
  psmisc git tree (git://psmisc.git.sourceforge.net/gitroot/psmisc/psmisc).
  The fix will be included in the 22.15 release.

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 22.13-2
+ Revision: 667895
- mass rebuild

* Mon Sep 27 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 22.13-1mdv2011.0
+ Revision: 581175
- new release: 22.13
-drop peekfd build fix patch (P0, fixed upstream)

* Sun Aug 15 2010 Sandro Cazzaniga <kharec@mandriva.org> 22.12-1mdv2011.0
+ Revision: 570049
- rediff patch
- new version

* Mon May 17 2010 Eugeni Dodonov <eugeni@mandriva.com> 22.11-1mdv2010.1
+ Revision: 544961
- Updated to new version 22.11.

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 22.10-1mdv2010.1
+ Revision: 486816
- update to new version 22.10

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 22.9-1mdv2010.1
+ Revision: 482728
- Fix BuildRequires
- Update to new version 22.9 (new prstat command)
- Let autoreconf create missing files

* Sun Aug 02 2009 Eugeni Dodonov <eugeni@mandriva.com> 22.8-1mdv2010.0
+ Revision: 407500
- Updated to 22.8.

* Sun May 10 2009 Frederik Himpe <fhimpe@mandriva.org> 22.7-1mdv2010.0
+ Revision: 374065
- Update to new version 22.7
- Remove old patches for problems fixed upstream
- Add patch from Arch Linux to fix building of peekfd on x86_64

* Sun Mar 08 2009 Michael Scherer <misc@mandriva.org> 22.6-5mdv2009.1
+ Revision: 352750
- remove  patch0, as it was nullified by patch3, and was not working
- disable peekfd on x86_64 as it doesn't compile and as this requires too
  much code adaptation for me ( since I do not know the register used by peekfd on
  64 bits archs )
- adapt patch from Fedora to make peekfs compile again

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Wed May 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 22.6-3mdv2009.0
+ Revision: 203286
- Patch2: fix overflow in pstree

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 22.6-2mdv2008.1
+ Revision: 169862
- new license policy
- do not package COPYING file
- fix building on x86_64 with patch 0
- include peekfd for other architectures

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 10 2007 David Walluck <walluck@mandriva.org> 22.6-1mdv2008.1
+ Revision: 107353
- 22.6

* Sun Jul 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 22.5-2mdv2008.0
+ Revision: 49886
- exclude peekfd and its manpages on non-i586 architectures
- new version
- rediff patch 1
- fix file list
- spec file clean
- Import psmisc



* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 22.2-2mdv2007.0
- Rebuild

* Thu May 04 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 22.2-1mdk
- 22.2

* Fri Dec 23 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 21.9-1mdk
- 21.9
- also ship oldfuser
- regenerate P1
- drop P2 (fixed upstream)
- fix summary-ended-with-dot

* Sat Jun 12 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 21.5-3mdk
- fixed patch2, removed termcap-devel buildrequires

* Thu Jun 10 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 21.5-2mdk
- fix buildrequires

* Tue Jun 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 21.5-1mdk
- 21.5
- fix conflicting types in src/pstree.c (P2)
- spec cosmetics

* Mon Feb 02 2004 Nicolas Planel <nplanel@mandrakesoft.com> 21.4-1mdk
- 21.4.

* Tue Jul 22 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 21.3-2mdk
- rebuild

* Thu Jun 05 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 21.3-1mdk
- new release
- added locale files

* Tue Oct 22 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21.2-1mdk
- new release :
	* bug fixes in pstree:
	  o pstree -a would often fail badly (swapped variable  not set)
	  o fix pstree -a extra bracket problem
	* removed pidof.1 and a variable not used.
	* SELINUX/hurd/lfs support
	* changed killall.1 to be less ambigous
	* fix UTF8 problem
	* return for fuser -k will mean no.

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 21-2mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Tue May 21 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 21-1mdk
- new release
- remove patch0 (merged upstream)

* Tue May 14 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 20.2-3mdk
- gcc-3.1 build
- fix "fails to show process tree" problem with libsafe [Patch1]:
  the source string for comm is too short for "%%15c" wich potentially allow the
  code to read beyond the end of the source string.
  The new format '%%[^)]' will never read beyond the end of the source string,
  which keeps libsafe happy. (It appears that glibc doesn't "sniff" the stack
  in this way, so the authors of libsafe may be overly cautious.)

* Mon Jan 14 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 20.2-2mdk
- hum, try to use the same signal numbers as the kernel... 15 signals
  names were wrong!

* Thu Jan 10 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 20.2-1mdk
- this is gpl, not distributable
- sanitize
- new version

* Sun Apr 08 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 20.1-1mdk
- Bump up to 20.1.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 19-4mdk
- automatically added BuildRequires


* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 19-3mdk
- macros, BM, spechelper ( :-( )

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 19-2mdk
- Fix bad tag value.

* Tue Mar 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 19-1mdk
- Version update (19)
- Use default Mandrake Optimisations.
- Patch the Makefile for psmisc rpm to be compiled by non root user.
- bziped psmisc-17-buildroot.patch

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Move fuser to /sbin(r).

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale

* Sat Mar 13 1999 Michael Maher <mike@redhat.com>
- updated package

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- renamed the patch file .patch instead of .spec

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to psmisc version 17
- buildrooted

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- updated from version 11 to version 16
- spec file cleanups

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
