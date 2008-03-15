%define with_klinkstatus 1

%define lib_name_orig lib%name
%define lib_major 0
%define lib_name %mklibname %name %lib_major

Name: kdewebdev4
Version: 4.0.2
License: GPL
Summary: A web editor for the KDE Desktop Environment
Epoch: 1
URL: http://kdewebdev.org/
Release: %mkrel 3
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdewebdev-%version.tar.bz2
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: pam
BuildRequires: diffutils
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: kdelibs4-devel
BuildRequires: freetype2 
# Add back for kde 4.1
#BuildRequires: kdevplatform4-devel
%if %with_klinkstatus
BuildRequires: tidy-devel
Requires: tidy
%endif
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

Requires: kde4-quanta
Requires: kde4-kimagemapeditor
%if %with_klinkstatus
Requires: kde4-klinkstatus
%endif
Requires: kde4-kfilereplace
Requires: kde4-kommander

%description
A web editor for the KDE Desktop Environment

#--------------------------------------------------------------------

%package -n kde4-quanta
Summary: Quanta
Group: Graphical desktop/KDE
Provides: quanta4
Requires: kde4-kimagemapeditor
%if %with_klinkstatus
Requires: kde4-klinkstatus
%endif
Requires: kde4-kfilereplace
Requires: kde4-kommander
Requires: tidy
Obsoletes: %name-core
%description -n kde4-quanta
A HTML editor for the K Desktop Environment.

%files -n kde4-quanta
%defattr(-,root,root)
%if 0
%_kde_bindir/quanta
%_kde_libdir/kde4/libkdev*
%_kde_libdir/kde4/quanta*
%_kde_libdir/libkdevquanta.so.*
%_kde_datadir/applications/kde4/quanta.desktop
%_kde_datadir/config.kcfg/quanta.kcfg
%_kde_datadir/kde4/services/kdev*
%_kde_datadir/kde4/services/quanta*
%_kde_datadir/kde4/servicetypes/kdev*
%_kde_appsdir/kdev*/*
%_kde_appsdir/quanta*/*
%_kde_iconsdir/*/*/apps/quanta*
%_kde_docdir/HTML/en/quanta
%endif

%if %with_klinkstatus
%package -n kde4-klinkstatus
Summary: klinkstatus
Group: Graphical desktop/KDE
Provides: klinkstatus4
Obsoletes: %name-core
%description -n kde4-klinkstatus
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


%files -n kde4-klinkstatus
%defattr(-,root,root)
%{_kde_bindir}/klinkstatus
%{_kde_libdir}/kde4/klinkstatuspart.so
%{_kde_datadir}/applications/kde4/klinkstatus.desktop
%dir %{_kde_appsdir}/klinkstatus
%{_kde_appsdir}/klinkstatus/klinkstatus_shell.rc
%dir %{_kde_appsdir}/klinkstatus/styles
%{_kde_appsdir}/klinkstatus/styles/results_stylesheet.xsl
%dir %{_kde_appsdir}/klinkstatuspart
%{_kde_appsdir}/klinkstatuspart/klinkstatus_part.rc
%{_kde_appsdir}/klinkstatuspart/pics/304.png
%{_kde_iconsdir}/*/*/apps/klinkstatus.png
%{_kde_datadir}/kde4/services/klinkstatus_part.desktop
%{_datadir}/dbus-1/interfaces/org.kdewebdev.klinkstatus.ISearchManager.xml
%_kde_docdir/HTML/en/klinkstatus
%endif

#--------------------------------------------------------------------------

%package -n kde4-kfilereplace
Summary: kfilereplace
Group: Graphical desktop/KDE
Provides: kfilereplace4
Obsoletes: %name-core

%description -n kde4-kfilereplace
Kfilereplace program

%post -n kde4-kfilereplace
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun -n kde4-kfilereplace
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files -n kde4-kfilereplace
%defattr(-,root,root)
%_kde_bindir/kfilereplace
%_kde_datadir/applications/kde4/kfilereplace.desktop
%_kde_appsdir/kfilereplace/kfilereplaceui.rc
%_kde_appsdir/kfilereplacepart/icons/crystalsvg/22x22/actions/*
%_kde_appsdir/kfilereplacepart/kfilereplacepartui.rc
%_kde_iconsdir/*/*/apps/kfilereplace.png
%_kde_datadir/kde4/services/kfilereplacepart.desktop
%_datadir/dbus-1/interfaces/org.kde.kfilereplace.xml
%_kde_libdir/kde4/libkfilereplacepart.so
%_kde_docdir/HTML/en/kfilereplace
%_kde_iconsdir/*/*/actions/*

#--------------------------------------------------------------------------

%package -n kde4-kommander
Summary: Kommander
Group: Graphical desktop/KDE
Provides: kommander4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: %name-core

%description -n kde4-kommander
Kommander program

%post -n kde4-kommander
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun -n kde4-kommander
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files -n kde4-kommander
%defattr(-,root,root)


#--------------------------------------------------------------------------

%package -n kde4-kimagemapeditor
Summary: Kimagemapeditor
Group: Graphical desktop/KDE
Provides: kimagemapeditor4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: %name-core

%description -n kde4-kimagemapeditor
kimagemapeditor program

%post -n kde4-kimagemapeditor
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun -n kde4-kimagemapeditor
%{clean_desktop_database}
%clean_icon_cache locolor 
%clean_icon_cache hicolor

%files -n kde4-kimagemapeditor
%defattr(-,root,root)
%_kde_bindir/kimagemapeditor
%_kde_datadir/applications/kde4/kimagemapeditor.desktop
%_kde_appsdir/kimagemapeditor/*.rc
%_kde_appsdir/kimagemapeditor/*.png
%_kde_datadir/icons/hicolor/*/apps/kimagemapeditor.png
%_kde_datadir/kde4/services/kimagemapeditorpart.desktop
%_kde_libdir/kde4/libkimagemapeditor.so
%_kde_docdir/*/*/kimagemapeditor

%exclude %_kde_docdir/HTML/en/xsldbg

#--------------------------------------------------------------------------
%if 0
%package -n kde4-kxsldbg
Summary: Kxsldbg
Group: Graphical desktop/KDE
Provides: kxsldbg4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Obsoletes: %name-core

%description -n kde4-kxsldbg
kxsldbg program

%post -n kde4-kxsldbg
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun -n kde4-kxsldbg
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files -n kde4-kxsldbg
%defattr(-,root,root)
%_kde_bindir/kxsldbg
%_kde_bindir/xsldbg
%_kde_datadir/applications/kde4/kxsldbg.desktop
%dir %_kde_appsdir/kxsldbg
%_kde_appsdir/kxsldbg/*.xml
%_kde_appsdir/kxsldbg/*.xsl
%_kde_appsdir/kxsldbg/*.dtd
%_kde_appsdir/kxsldbg/kxsldbg_shell.rc
%_kde_appsdir/kxsldbgpart/kxsldbg_part.rc
%dir %_kde_appsdir/xsldbg
%_kde_appsdir/xsldbg/*.xml
%_kde_appsdir/xsldbg/*.xsl
%_kde_appsdir/xsldbg/*.dtd
%_kde_datadir/icons/hicolor/*/actions/xsldbg_*
%_kde_datadir/kde4/services/kxsldbg_part.desktop
%_datadir/dbus-1/interfaces/org.kde.kxsldbg.kxsldbg.xml
%_kde_libdir/kde4/libkxsldbgpart.so
%_kde_docdir/HTML/en/kxsldbg
# Invalid for now
%exclude %_kde_docdir/HTML/en/xsldbg
%endif
#--------------------------------------------------------------------------

%prep
%setup -q -n kdewebdev-%version 

%build

%cmake_kde4

%make

%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

rm -f %buildroot%_kde_libdir/libkdev*.so

%clean
rm -rf $RPM_BUILD_ROOT

