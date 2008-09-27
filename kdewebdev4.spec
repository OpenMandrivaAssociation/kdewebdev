%define with_klinkstatus 1

%define lib_name_orig lib%name
%define lib_major 0
%define lib_name %mklibname %name %lib_major

Name: kdewebdev4
Version: 4.1.2
License: GPLv2+
Summary: A web editor for the KDE Desktop Environment
Epoch: 1
URL: http://kdewebdev.org/
Release: %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdewebdev-%version.tar.bz2
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: pam
BuildRequires: diffutils
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: boost-devel
BuildRequires: freetype2 
BuildRequires: xft2-devel
BuildRequires: xpm-devel
# Not yet
# BuildRequires: kdevplatform4-devel
%if %with_klinkstatus
BuildRequires: tidy-devel
%endif
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

Requires: quanta
Requires: kxsldbg
Requires: kimagemapeditor
%if %with_klinkstatus
Requires: klinkstatus
%endif
Requires: kfilereplace
Requires: kommander

%description
A web editor for the KDE Desktop Environment

#--------------------------------------------------------------------

%package -n quanta
Summary: Quanta
Group: Graphical desktop/KDE
Provides: quanta4
Requires: kimagemapeditor
%if %with_klinkstatus
Requires: klinkstatus
%endif
Requires: kfilereplace
Requires: kommander
Requires: tidy
Obsoletes: %name-core
Obsoletes:      kde4-quanta < 4.0.68
Provides:       kde4-quanta = %version

%description -n quanta
A HTML editor for the K Desktop Environment.

%files -n quanta
%defattr(-,root,root)
#%_kde_bindir/quanta
#%_kde_libdir/kde4/libkdev*
#%_kde_libdir/kde4/quanta*
#%_kde_libdir/libkdevquanta.so.*
#%_kde_datadir/applications/kde4/quanta.desktop
#%_kde_datadir/config.kcfg/quanta.kcfg
#%_kde_datadir/kde4/services/kdev*
#%_kde_datadir/kde4/services/quanta*
#%_kde_datadir/kde4/servicetypes/kdev*
#%_kde_appsdir/kdev*/*
#%_kde_appsdir/quanta*/*
#%_kde_iconsdir/*/*/apps/quanta*
#%_kde_docdir/HTML/en/quanta

#--------------------------------------------------------------------

%if %with_klinkstatus
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
%endif

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

%if %mdkversion < 200900
%post -n %libklinkstatuscommon -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libklinkstatuscommon -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n kfilereplace
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun -n kfilereplace
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor
%endif

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

%if %mdkversion < 200900
%post -n %libkommanderwidgets -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkommanderwidgets -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libkommandercore -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libkommandercore -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n kommander
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun -n kommander
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor
%endif

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

%if %mdkversion < 200900
%post -n kimagemapeditor
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun -n kimagemapeditor
%{clean_desktop_database}
%clean_icon_cache locolor 
%clean_icon_cache hicolor
%endif

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

%package -n kxsldbg
Summary: Kxsldbg
Group: Graphical desktop/KDE
Provides: kxsldbg4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: %name-core
Obsoletes:      kde4-kxsldbg < 4.0.68
Provides:       kde4-kxsldbg = %version

%description -n kxsldbg
kxsldbg program

%if %mdkversion < 200900
%post -n kxsldbg
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun -n kxsldbg
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor
%endif

%files -n kxsldbg
%defattr(-,root,root)
%_kde_bindir/kxsldbg
%_kde_bindir/xsldbg
%_kde_datadir/applications/kde4/kxsldbg.desktop
%dir %_kde_appsdir/kxsldbg
%_kde_appsdir/kxsldbg/*
%dir %_kde_appsdir/xsldbg
%_kde_appsdir/xsldbg/*
%dir %_kde_appsdir/kxsldbgpart
%_kde_appsdir/kxsldbgpart/*
%_kde_iconsdir/*/*/*/*xsldbg*
%_kde_datadir/kde4/services/kxsldbg_part.desktop
%_kde_libdir/kde4/libkxsldbgpart.so
%_kde_docdir/HTML/en/kxsldbg
%_kde_docdir/HTML/en/xsldbg
%_kde_mandir/man1/xsldbg.1.lzma

#--------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: kde4-macros
Requires: kdelibs4-devel
Requires: %{libkommandercore}
Requires: %{libkommanderwidgets}

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
%setup -q -n kdewebdev-%version

%build
%cmake_kde4

%make

%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

%clean
rm -rf $RPM_BUILD_ROOT

