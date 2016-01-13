Summary:	A web editor for the KDE Desktop Environment
Name:		kdewebdev
Version:	15.12.1
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://kdewebdev.org/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	automoc4
BuildRequires:	boost-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	ruby-devel
BuildRequires:	tidy-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
Requires:	kfilereplace
Requires:	kimagemapeditor
Requires:	klinkstatus
Requires:	kommander

%description
A web editor for the KDE Desktop Environment.

%files
%doc README

#--------------------------------------------------------------------------

%package -n kfilereplace
Summary:	Search and replace tool
Group:		Graphical desktop/KDE
Conflicts:	kdewebdev4-devel < 1:4.11.0

%description -n kfilereplace
Search and replace tool.

%files -n kfilereplace
%{_kde_bindir}/kfilereplace
%{_kde_applicationsdir}/kfilereplace.desktop
%{_kde_appsdir}/kfilereplace
%{_kde_appsdir}/kfilereplacepart
%{_kde_iconsdir}/*/*/apps/kfilereplace.png
%{_kde_iconsdir}/*/*/actions/*
%{_kde_services}/kfilereplacepart.desktop
%{_kde_libdir}/kde4/libkfilereplacepart.so
%{_kde_docdir}/HTML/en/kfilereplace
%{_datadir}/dbus-1/interfaces/org.kde.kfilereplace.xml

#--------------------------------------------------------------------------

%package -n kimagemapeditor
Summary:	HTML image map editor
Group:		Graphical desktop/KDE

%description -n kimagemapeditor
HTML image map editor.

%files -n kimagemapeditor
%{_kde_bindir}/kimagemapeditor
%{_kde_applicationsdir}/kimagemapeditor.desktop
%{_kde_appsdir}/kimagemapeditor
%{_kde_iconsdir}/hicolor/*/apps/kimagemapeditor.png
%{_kde_services}/kimagemapeditorpart.desktop
%{_kde_libdir}/kde4/libkimagemapeditor.so
%{_kde_docdir}/*/*/kimagemapeditor

#--------------------------------------------------------------------

%package -n klinkstatus
Summary:	Link checker tool
Group:		Graphical desktop/KDE
Requires:	tidy
Conflicts:	kdewebdev4-devel < 1:4.11.0

%description -n klinkstatus
Link checker tool. It features:
* Support several protocols (allowing fast checking of
  local documents): http, ftp, ssh (fish or sftp) and file.
* Proxy support
* Allows authentication when checking restricted documents
* Supports the latest Web standards-- HTML 4.0, HTTP 1.1
* Server-Side Includes (SSI, aka SHTML) are supported and checked
* Regular expressions to restrict which URLs are searched
* Show link results as they are checked
* Tree like view (that reflects the file structure of the documents) or
  flat view
* Limit the search depth
* Fragment identifiers ("#" anchor links that point to a specific
  section in a document) are supported and checked
* Pause/Resume of checking session
* History of checked URLs
* Tabbed checking (allow multiple sessions at the same time)
* Filter checked links (good, broken, malformed and undetermined)
* Configurable number of simultaneous connections (performance tunning)
* Other configurable options like "check external links",
  "check parent folders", "timeout"
* Good integration with Quanta+

%files -n klinkstatus
%{_kde_bindir}/klinkstatus
%{_kde_libdir}/kde4/klinkstatuspart.so
%{_kde_libdir}/kde4/automationklinkstatus.so
%{_kde_libdir}/kde4/krossmoduleklinkstatus.so
%{_kde_applicationsdir}/klinkstatus.desktop
%{_kde_appsdir}/klinkstatus
%{_kde_appsdir}/klinkstatuspart
%{_kde_iconsdir}/*/*/apps/klinkstatus.png
%{_kde_services}/klinkstatus_part.desktop
%{_kde_services}/klinkstatus_automation.desktop
%{_kde_services}/krossmoduleklinkstatus.desktop
%{_kde_configdir}/klinkstatus.knsrc
%{_kde_docdir}/HTML/en/klinkstatus
%{_datadir}/dbus-1/interfaces/org.kde.kdewebdev.klinkstatus.SearchManager.xml

#--------------------------------------------------------------------------

%package -n kommander
Summary:	Visual dialog building tool
Group:		Graphical desktop/KDE

%description -n kommander
Kommander is a visual dialog building tool which may be expanded to create
full mainwindow applications. The primary objective is to create as much
functionality as possible without using any scripting language. This is
provided by the following features:
* Specials - these are prefaced with an "@" like @widgetText. The offer
  special features like the value of a widget, functions, aliases, global
  variables and such.
* DCOP integration - this allows Kommander dialogs to control and be
  controled in interactions with other KDE applicatins. It is a very powerful
  feature!
* Signals and Slots - this is a little less intuitive to a new user. It is
  under review for how we process things in the first major release. These
  offer a limited event model for when a button is pushed or a widget is
  changed. Combined with "Population Text" it is rather powerful.

%files -n kommander
%{_kde_bindir}/kommander
%{_kde_datadir}/applnk/.hidden/kommander.desktop

#--------------------------------------------------------------------------

%define klinkstatuscommon_major 4
%define libklinkstatuscommon %mklibname klinkstatuscommon %{klinkstatuscommon_major}

%package -n %{libklinkstatuscommon}
Summary:	KDE4 shared library
Group:		System/Libraries

%description -n %{libklinkstatuscommon}
KDE4 shared library.

%files -n %{libklinkstatuscommon}
%{_kde_libdir}/libklinkstatuscommon.so.%{klinkstatuscommon_major}*

#--------------------------------------------------------------------------

%define kommanderwidgets_major 4
%define libkommanderwidgets %mklibname kommanderwidgets %{kommanderwidgets_major}

%package -n %{libkommanderwidgets}
Summary:	KDE4 shared library
Group:		System/Libraries

%description -n %{libkommanderwidgets}
KDE4 shared library.

%files -n %{libkommanderwidgets}
%{_kde_libdir}/libkommanderwidgets.so.%{kommanderwidgets_major}*

#--------------------------------------------------------------------------

%define kommandercore_major 4
%define libkommandercore %mklibname kommandercore %{kommandercore_major}

%package -n %{libkommandercore}
Summary:	KDE4 shared library
Group:		System/Libraries

%description -n %{libkommandercore}
KDE4 shared library.

%files -n %{libkommandercore}
%{_kde_libdir}/libkommandercore.so.%{kommandercore_major}*

#--------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	kde4-macros
Requires:	kdelibs4-devel
Requires:	%{libklinkstatuscommon} = %{EVRD}
Requires:	%{libkommandercore} = %{EVRD}
Requires:	%{libkommanderwidgets} = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_includedir}/*
%{_kde_libdir}/*.so

#--------------------------------------------------------------------------

%prep
%setup -q -n kdewebdev-%{version}
# required for cmake now
sed -i '1s/^/cmake_minimum_required(VERSION 2.4)\n/' CMakeLists.txt

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.3-1
- New version 4.14.3

* Wed Oct 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.2-1
- New version 4.14.2

* Mon Sep 29 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.14.1-1
- New version 4.14.1
- Fix descriptions

* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0
- Move dbus files out of devel package

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Tue Jul 17 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97

* Sat Jun 30 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.1mib2010.2
+ Revision: 762522
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762522
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758111
- New upstream tarball

* Sun Jan 01 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 748619
- New version

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-1
+ Revision: 739376
- New upstream tarball

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.80-1
+ Revision: 732346
- Add Automoc4 as buildrequires ( to workaround a rpm5/iurt bug)
- New upstream tarball 4.7.80

* Fri Aug 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.41-1
+ Revision: 697178
- New version 4.7.41

* Mon Aug 01 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.40-1
+ Revision: 692647
- New release 4.7.40

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-1
+ Revision: 684413
- New version 4.6.4

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 1:4.6.3-1
+ Revision: 674038
- new version 4.6.3

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.2-1
+ Revision: 650784
- Remove mkrel
- New version 4.6.2

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.1-1
+ Revision: 640736
- New version 4.6.1

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.0-1
+ Revision: 632973
- New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.95-1mdv2011.0
+ Revision: 629129
- New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.90-1mdv2011.0
+ Revision: 624073
- New upstream tarball

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.85-1mdv2011.0
+ Revision: 616354
- New upstream tarball

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 1:4.5.80-1mdv2011.0
+ Revision: 601498
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 1:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599145
- new snapshot 4.5.77

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 1:4.5.74-1mdv2011.0
+ Revision: 591175
- new snapshot 4.5.74

* Fri Sep 17 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-1mdv2011.0
+ Revision: 579201
- new snapshot 4.5.68

* Sat Sep 11 2010 Funda Wang <fwang@mandriva.org> 1:4.5.67-1mdv2011.0
+ Revision: 577148
- new version 4.5.67

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.0-1mdv2011.0
+ Revision: 566578
- New upstream tarball
- Update to version 4.5.0

* Thu Jul 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.95-1mdv2011.0
+ Revision: 562878
- KDE 4.5 RC3

* Sat May 08 2010 Funda Wang <fwang@mandriva.org> 1:4.4.3-2mdv2010.1
+ Revision: 543555
- add missing requires on actural libfile

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-1mdv2010.1
+ Revision: 542111
- Update to version 4.4.3

* Sun Mar 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-1mdv2010.1
+ Revision: 528326
- Update to version 4.4.2

* Tue Mar 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-1mdv2010.1
+ Revision: 513419
- Update to version 4.4.1

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-1mdv2010.1
+ Revision: 502620
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-1mdv2010.1
+ Revision: 498951
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.95-1mdv2010.1
+ Revision: 495989
- Update to version 4.3.95 aka "kde 4.4 RC2"

* Mon Jan 11 2010 Funda Wang <fwang@mandriva.org> 1:4.3.90-1mdv2010.1
+ Revision: 489628
- New version 4.3.90

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.85-1mdv2010.1
+ Revision: 480709
- Update to kde 4.4 beta2

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 1:4.3.80-1mdv2010.1
+ Revision: 473697
- kxsldbg has been moved into extragear

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to kde 4.4 Beta1
      Add branch switch

* Sun Nov 29 2009 Funda Wang <fwang@mandriva.org> 1:4.3.77-1mdv2010.1
+ Revision: 471356
- new version 4.3.77

* Thu Nov 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.75-1mdv2010.1
+ Revision: 467355
- Update to kde 4.3.75

* Fri Nov 13 2009 Funda Wang <fwang@mandriva.org> 1:4.3.73-1mdv2010.1
+ Revision: 465798
- New version 4.3.73

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.2-1mdv2010.0
+ Revision: 454673
- New upstream release 4.3.2.

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-2mdv2010.0
+ Revision: 444680
- Add ruby-devel as BuildRequires ( tks MIB )

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-1mdv2010.0
+ Revision: 423224
- New upstream release 4.3.1.

* Tue Aug 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.0-2mdv2010.0
+ Revision: 415217
- Add obsoletes to help to remove kde3

  + Funda Wang <fwang@mandriva.org>
    - add qt4-qtdbus BR as it requires xml2cpp binary

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream release 4.3.0.
    - Update to KDE 4.3 RC3

* Tue Jul 14 2009 Funda Wang <fwang@mandriva.org> 1:4.2.96-1mdv2010.0
+ Revision: 395747
- new version 4.2.96

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-1mdv2010.0
+ Revision: 389494
- Update to kde 4.3Rc1

* Fri Jun 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.90-1mdv2010.0
+ Revision: 383154
- Update to beta2

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 1:4.2.88-1mdv2010.0
+ Revision: 380823
- New version 4.2.88

* Mon May 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.87-2mdv2010.0
+ Revision: 379540
- Disable quanta doc as there is not quanta binary for the moment
- handle branches

* Sun May 24 2009 Funda Wang <fwang@mandriva.org> 1:4.2.87-1mdv2010.0
+ Revision: 379130
- New version 4.2.87

* Sat May 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-1mdv2010.0
+ Revision: 373657
- Update to kde 4.2.85

* Sun May 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371265
- Update to kde 4.2.71
- Update to kde 4.2.70

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.2-1mdv2009.1
+ Revision: 361734
- Update with 4.2.2 try#1 packages

* Tue Mar 03 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-1mdv2009.1
+ Revision: 347743
- KDE 4.2.1 try#1 upstream release

* Wed Jan 28 2009 Funda Wang <fwang@mandriva.org> 1:4.2.0-1mdv2009.1
+ Revision: 334821
- New version 4.2.0

* Wed Jan 07 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.96-1mdv2009.1
+ Revision: 326838
- Update with Release Candidate 1 - 4.1.96

* Tue Dec 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-1mdv2009.1
+ Revision: 314911
- Update to kde 4.1.85

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.82-2mdv2009.1
+ Revision: 313489
- Update to kde 4.1.82

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 1:4.1.81-2mdv2009.1
+ Revision: 308434
- fix file list
- add main meta pacakge to ease installing all the subpackages
- fix conflicts with kfilereplace and kxsldbg

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 1:4.1.81-1mdv2009.1
+ Revision: 308362
- New version 4.1.81

* Wed Nov 19 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.80-1mdv2009.1
+ Revision: 304573
- Update with Beta 1 - 4.1.80

* Fri Nov 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.73-1mdv2009.1
+ Revision: 303198
- Update to jde 4.1.73

* Sun Nov 09 2008 Funda Wang <fwang@mandriva.org> 1:4.1.72-1mdv2009.1
+ Revision: 301275
- New version 4.1.72

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.71-1mdv2009.1
+ Revision: 297100
- New version 4.1.71

* Tue Oct 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.70-1mdv2009.1
+ Revision: 296169
- Update to kde 4.1.70
- Do not package quanta, still empty, will be enable back later

* Sat Sep 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.2-1mdv2009.0
+ Revision: 288848
- KDE 4.1.2 arriving.

* Fri Sep 05 2008 Funda Wang <fwang@mandriva.org> 1:4.1.1-1mdv2009.0
+ Revision: 280989
- New version 4.1.1
- patch0 merged upstream

* Mon Jul 28 2008 Funda Wang <fwang@mandriva.org> 1:4.1.0-2mdv2009.0
+ Revision: 251469
- Patch0 updated with svn r838725 and svn r838730
- re-enalbe tidy build
- clearify the license
- rediff tidy detection patch, but disable tidy, because it fails to build

* Fri Jul 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-1mdv2009.0
+ Revision: 247630
- Update with Release Candidate 1 - 4.1.0

* Tue Jul 15 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.98-1mdv2009.0
+ Revision: 236105
- Update with Release Candidate 1 - 4.0.98

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.85-1mdv2009.0
+ Revision: 232551
- New version kde 4.0.85

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.84-1mdv2009.0
+ Revision: 229409
- Update with new snapshot tarballs 4.0.84

* Fri Jun 20 2008 Pixel <pixel@mandriva.com> 1:4.0.83-2mdv2009.0
+ Revision: 227426
- rebuild for fixed %%update_icon_cache/%%clean_icon_cache/%%post_install_gconf_schemas
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jun 19 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-1mdv2009.0
+ Revision: 226106
- Update with new snapshot tarballs 4.0.83

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.82-1mdv2009.0
+ Revision: 218530
- Kommander is back, ksxldbg as well
- Update with new snapshot tarballs 4.0.82
- Update with new snapshot tarballs 4.0.81
- New upstream kde4 4.1 beta1

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 1:4.0.74-1mdv2009.0
+ Revision: 208050
- find our own tidy lib
- New version 4.0.74

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to kde 4.0.73
    - Update to 4.0.70
      Comment some files ( will be added soon when ported )

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1
    - Update for last stable release 4.0.3

* Tue Mar 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-5mdv2008.1
+ Revision: 190113
- Fix Requires

* Sat Mar 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-4mdv2008.1
+ Revision: 188106
- Remove kde4-quanta

* Sat Mar 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-3mdv2008.1
+ Revision: 188026
- Fix File list
- remove kde4-kxsldbg instead of shipping and empty one (it will come back for kde 4.1)

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-2mdv2008.1
+ Revision: 182308
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.2-1mdv2008.1
+ Revision: 177467
- New upstream bugfix release 4.0.2

* Tue Feb 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-1mdv2008.1
+ Revision: 166330
- Updating for stable KDE 4.0.1
- No more branches. From now, we will be using the monthly official KDE tarballs, as discussed by Mandriva KDE team
- Removed old documentation from package
- Obsoleted core package, as not needed anymore
- excluded invaliud documentation installed ( xsldbg )

  + Thierry Vignaud <tv@mandriva.org>
    - fix case in kde4-quanta's description
    - fix description-line-too-long
    - fix spacing at top of description

* Wed Jan 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-1mdv2008.1
+ Revision: 157074
- Update to kde 4.0.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-0.751978.1mdv2008.1
+ Revision: 137596
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-0.746427.1mdv2008.1
+ Revision: 117790
- New snapshot
  Add patch0 to fix build
- New snapshot

  + Thierry Vignaud <tv@mandriva.org>
    - fix description

* Sun Nov 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.739968.1mdv2008.1
+ Revision: 111820
- New snapshot

* Sun Nov 18 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.0-0.736231.1mdv2008.1
+ Revision: 109740
- KDE4 RC1
  klinkstatus is back
- New snapshot post Rc1

* Wed Oct 31 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.730716.3mdv2008.1
+ Revision: 104116
- New snapshot

* Sun Oct 21 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.727328.3mdv2008.1
+ Revision: 100753
- Kde 4 Beta 3
- [BUGFIX] Fix Requires (Bug #31916)

* Wed Sep 26 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:3.93.0-0.711694.2mdv2008.0
+ Revision: 93127
- Disable klinkstatus
- New snapshot from KDE svn
- Spec cleanup

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove patch0: not needed anymore
    - Add BuildRequires ( kdevplatform4-devel)

* Sun Jul 01 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.91-0.682032.1mdv2008.0
+ Revision: 46406
- Fix File list
- New version 3.91

  + Laurent Montel <lmontel@mandriva.org>
    - Fix release version
    - new snapshot


* Thu Jan 18 2007 Laurent Montel <lmontel@mandriva.com> 3.80.2-0.20070117.2mdv2007.0
+ Revision: 110505
- Remove buildrequires
- Update

* Thu Jan 11 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070109.2mdv2007.1
+ Revision: 107441
- Import kdewebdev4

