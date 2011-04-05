%define branch 0
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define kde_snapshot svn1198704
%endif

Name: kdewebdev4
Version: 4.6.2
License: GPLv2+
Summary: A web editor for the KDE Desktop Environment
Epoch: 1
URL: http://kdewebdev.org/
%if %branch
Release: 0.%kde_snapshot.1
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdewebdev-%version%kde_snapshot.tar.bz2
%else
Release: 1
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdewebdev-%version.tar.bz2
%endif
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: boost-devel
BuildRequires: ruby-devel
BuildRequires: tidy-devel
Requires: kimagemapeditor
Requires: klinkstatus
Requires: kfilereplace
Requires: kommander
%if %mdkversion >= 201000
Obsoletes:      kdewebdev < 3.5.10-2
%endif

%description
A web editor for the KDE Desktop Environment

%files
%defattr(-,root,root)
%doc README

#--------------------------------------------------------------------

%package -n klinkstatus
Summary: klinkstatus
Group: Graphical desktop/KDE
Provides: klinkstatus4
Obsoletes: %name-core
Obsoletes:      kde4-klinkstatus < 4.0.68
Provides:       kde4-klinkstatus = %version
Requires: tidy

%description -n klinkstatus
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
%defattr(-,root,root)
%{_kde_bindir}/klinkstatus
%{_kde_libdir}/kde4/klinkstatuspart.so
%{_kde_libdir}/kde4/automationklinkstatus.so
%{_kde_libdir}/kde4/krossmoduleklinkstatus.so
%{_kde_datadir}/applications/kde4/klinkstatus.desktop
%{_kde_appsdir}/klinkstatus
%{_kde_appsdir}/klinkstatuspart
%{_kde_iconsdir}/*/*/apps/klinkstatus.png
%{_kde_datadir}/kde4/services/klinkstatus_part.desktop
%{_kde_datadir}/config/klinkstatus.knsrc
%{_kde_datadir}/kde4/services/klinkstatus_automation.desktop
%{_kde_datadir}/kde4/services/krossmoduleklinkstatus.desktop
%_kde_docdir/HTML/en/klinkstatus

#--------------------------------------------------------------------------

%define klinkstatuscommon_major 4
%define libklinkstatuscommon %mklibname klinkstatuscommon %klinkstatuscommon_major

%package -n %libklinkstatuscommon
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libklinkstatuscommon
KDE 4 core library.

%files -n %libklinkstatuscommon
%defattr(-,root,root)
%_kde_libdir/libklinkstatuscommon.so.%{klinkstatuscommon_major}*


#--------------------------------------------------------------------------

%package -n kfilereplace
Summary: kfilereplace
Group: Graphical desktop/KDE
Provides: kfilereplace4
Obsoletes: %name-core
Obsoletes:      kde4-kfilereplace < 4.0.68
Provides:       kde4-kfilereplace = %version

%description -n kfilereplace
Kfilereplace program

%files -n kfilereplace
%defattr(-,root,root)
%_kde_bindir/kfilereplace
%_kde_datadir/applications/kde4/kfilereplace.desktop
%_kde_appsdir/kfilereplace
%_kde_appsdir/kfilereplacepart
%_kde_iconsdir/*/*/apps/kfilereplace.png
%_kde_datadir/kde4/services/kfilereplacepart.desktop
%_kde_libdir/kde4/libkfilereplacepart.so
%_kde_docdir/HTML/en/kfilereplace
%_kde_iconsdir/*/*/actions/*

#--------------------------------------------------------------------------

%define kommanderwidgets_major 4
%define libkommanderwidgets %mklibname kommanderwidgets %kommanderwidgets_major

%package -n %libkommanderwidgets
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkommanderwidgets
KDE 4 core library.

%files -n %libkommanderwidgets
%defattr(-,root,root)
%_kde_libdir/libkommanderwidgets.so.%{kommanderwidgets_major}*

#--------------------------------------------------------------------------

%define kommandercore_major 4
%define libkommandercore %mklibname kommandercore %kommandercore_major

%package -n %libkommandercore
Summary: KDE 4 core library
Group: System/Libraries

%description -n %libkommandercore
KDE 4 core library.

%files -n %libkommandercore
%defattr(-,root,root)
%_kde_libdir/libkommandercore.so.%{kommandercore_major}*

#--------------------------------------------------------------------------

%package -n kommander
Summary: Kommander
Group: Graphical desktop/KDE
Provides: kommander4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: %name-core
Obsoletes:      kde4-kommander < 4.0.68
Provides:       kde4-kommander = %version

%description -n kommander
Kommander program

%files -n kommander
%defattr(-,root,root)
%_kde_bindir/kommander
%_kde_datadir/applnk/.hidden/kommander.desktop

#--------------------------------------------------------------------------

%package -n kimagemapeditor
Summary: Kimagemapeditor
Group: Graphical desktop/KDE
Provides: kimagemapeditor4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: %name-core
Obsoletes:      kde4-kimagemapeditor < 4.0.68
Provides:       kde4-kimagemapeditor = %version

%description -n kimagemapeditor
kimagemapeditor program

%files -n kimagemapeditor
%defattr(-,root,root)
%_kde_bindir/kimagemapeditor
%_kde_datadir/applications/kde4/kimagemapeditor.desktop
%_kde_appsdir/kimagemapeditor
%_kde_datadir/icons/hicolor/*/apps/kimagemapeditor.png
%_kde_datadir/kde4/services/kimagemapeditorpart.desktop
%_kde_libdir/kde4/libkimagemapeditor.so
%_kde_docdir/*/*/kimagemapeditor

#--------------------------------------------------------------------------

%if 0
%package -n kxsldbg
Summary: Kxsldbg
Group: Graphical desktop/KDE
Provides: kxsldbg4
Conflicts: kfilereplace < 1:4.1.81-2
Obsoletes: %name-core
Obsoletes:      kde4-kxsldbg < 4.0.68
Provides:       kde4-kxsldbg = %version

%description -n kxsldbg
kxsldbg program

%files -n kxsldbg
%defattr(-,root,root)
%_kde_bindir/kxsldbg
%_kde_bindir/xsldbg
%_kde_datadir/applications/kde4/kxsldbg.desktop
%_kde_datadir/applications/kde4/xsldbg.desktop
%dir %_kde_appsdir/kxsldbg
%_kde_appsdir/kxsldbg/*
%dir %_kde_appsdir/xsldbg
%_kde_appsdir/xsldbg/*
%dir %_kde_appsdir/kxsldbgpart
%_kde_appsdir/kxsldbgpart/*
%_kde_iconsdir/hicolor/*/apps/kxsldbg.*
%_kde_iconsdir/hicolor/*/actions/xsldbg*
%_kde_datadir/kde4/services/kxsldbg_part.desktop
%_kde_libdir/kde4/libkxsldbgpart.so
%_kde_docdir/HTML/en/kxsldbg
%_kde_docdir/HTML/en/xsldbg
%_kde_mandir/man1/xsldbg.1*
%endif

#--------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %{libkommandercore} = %{epoch}:%{version}
Requires: %{libkommanderwidgets} = %{epoch}:%{version}
Requires: %{libklinkstatuscommon} = %{epoch}:%{version}

%description  devel
This package contains header files needed if you wish to build applications
based on %name.

%files devel
%defattr(-,root,root)
%_kde_datadir/dbus-1/interfaces/*
%{_kde_includedir}/*
%{_kde_libdir}/*.so

#--------------------------------------------------------------------------

%prep
%if %branch
%setup -q -n kdewebdev-%version%kde_snapshot
%else
%setup -q -n kdewebdev-%version
%endif

%build
%cmake_kde4

%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

