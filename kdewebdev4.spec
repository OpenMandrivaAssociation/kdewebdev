%define revision 727328

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define compile_apidox 1
%{?_no_apidox: %{expand: %%global compile_apidox 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif

%define with_klinkstatus 0

%define lib_name_orig lib%name
%define lib_major 0
%define lib_name %mklibname %name %lib_major


Name: kdewebdev4
Version: 3.94.0
Release: %mkrel 0.%revision.3
License: GPL
Summary: A web editor for the KDE Desktop Environment
Epoch: 1
URL: http://kdewebdev.org/
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdewebdev-%version.%revision.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdewebdev-%version.tar.bz2
%endif
Source1: css.tar.bz2
Source2: html.tar.bz2
Source3: javascript.tar.bz2
Source4: mysql5-quanta-doc-20051117.tar.bz2
Source5: php.tar.bz2
Group: Graphical desktop/KDE
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: pam
BuildRequires: diffutils
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: kdelibs4-devel
BuildRequires: freetype2 
BuildRequires: kdevplatform4-devel
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

%package -n %name-core
Summary: Common files needed by %name
Group: Graphical desktop/KDE
Provides: quanta4
%description -n %name-core

Common files needed by %name

%post -n %name-core
%update_icon_cache hicolor

%postun -n %name-core
%clean_icon_cache hicolor

%files -n %name-core
%defattr(-,root,root)
%_kde_iconsdir/hicolor/16x16/actions/1downarrow.png
%_kde_iconsdir/hicolor/16x16/actions/configure.png
%_kde_iconsdir/hicolor/16x16/actions/exit.png
%_kde_iconsdir/hicolor/16x16/actions/hash.png
%_kde_iconsdir/hicolor/16x16/actions/mark.png
%_kde_iconsdir/hicolor/16x16/actions/next.png
%_kde_iconsdir/hicolor/16x16/actions/run.png
%_kde_iconsdir/hicolor/16x16/actions/step.png
%_kde_iconsdir/hicolor/22x22/actions/1downarrow.png
%_kde_iconsdir/hicolor/22x22/actions/addpoint.png
%_kde_iconsdir/hicolor/22x22/actions/arrow.png
%_kde_iconsdir/hicolor/22x22/actions/circle.png
%_kde_iconsdir/hicolor/22x22/actions/circle2.png
%_kde_iconsdir/hicolor/22x22/actions/configure.png
%_kde_iconsdir/hicolor/22x22/actions/exit.png
%_kde_iconsdir/hicolor/22x22/actions/freehand.png
%_kde_iconsdir/hicolor/22x22/actions/lower.png
%_kde_iconsdir/hicolor/22x22/actions/next.png
%_kde_iconsdir/hicolor/22x22/actions/polygon.png
%_kde_iconsdir/hicolor/22x22/actions/raise.png
%_kde_iconsdir/hicolor/22x22/actions/rectangle.png
%_kde_iconsdir/hicolor/22x22/actions/removepoint.png
%_kde_iconsdir/hicolor/22x22/actions/run.png
%_kde_iconsdir/hicolor/22x22/actions/step.png

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
Requires: %name-core
%description -n kde4-quanta

A html editor for the K Desktop Environment.

%files -n kde4-quanta
%defattr(-,root,root)
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

%dir %_kde_docdir/HTML/en/quanta
%doc %_kde_docdir/HTML/en/quanta/*.docbook
%doc %_kde_docdir/HTML/en/quanta/*.png
%doc %_kde_docdir/HTML/en/quanta/index.cache.bz2

#--------------------------------------------------------------------------
#
#%package        kde4-quanta-doc
#Summary:        Documentation about Quanta
#Group:          Books/Computer books
#
#Provides:       quanta4-doc
#%description    kde4-quanta-doc
#
#Documentation for Quanta
#
#%files kde4-quanta-doc
#%dir %_kde_docdir/quanta
#%dir %_kde_docdir/quanta/css
#%doc %_kde_docdir/quanta/css/*
#%dir %_kde_docdir/quanta/html
#%doc %_kde_docdir/quanta/html/*
#%dir %_kde_docdir/quanta/javascript
#%doc %_kde_docdir/quanta/javascript/*
#%dir %_kde_docdir/quanta/mysql5
#%doc %_kde_docdir/quanta/mysql5/*
#%dir %_kde_docdir/quanta/php
#%doc %_kde_docdir/quanta/php/*
#
#--------------------------------------------------------------------------

%if %with_klinkstatus
%package -n kde4-klinkstatus
Summary: klinkstatus
Group: Graphical desktop/KDE
Provides: klinkstatus4
Requires: %name-core
%description -n kde4-klinkstatus

    * Support several protocols (allowing fast checking of 
	local documents): http, ftp, ssh (fish or sftp) and file.
    * Proxy support
    * Allows authentication when checking restricted documents
    * Supports the latest Web standards-- HTML 4.0, HTTP 1.1
    * Server-Side Includes (SSI, aka SHTML) are supported and checked
    * Regular expressions to restrict which URLs are searched
    * Show link results as they are checked
    * Tree like view (that reflects the file structure of the documents) or flat view
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
%dir %_kde_docdir/HTML/en/klinkstatus
%doc %_kde_docdir/HTML/en/klinkstatus/*.docbook
%doc %_kde_docdir/HTML/en/klinkstatus/*.png
%doc %_kde_docdir/HTML/en/klinkstatus/index.cache.bz2
%endif
#--------------------------------------------------------------------------

%package -n kde4-kfilereplace
Summary: kfilereplace
Group: Graphical desktop/KDE
Provides: kfilereplace4
Requires: %name-core

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
%doc %_kde_docdir/HTML/en/kfilereplace/*.png
%doc %_kde_docdir/HTML/en/kfilereplace/index.cache.bz2
%doc %_kde_docdir/HTML/en/kfilereplace/index.docbook
%_kde_iconsdir/hicolor/*/apps/kfilereplace.png
%_kde_datadir/kde4/services/kfilereplacepart.desktop
%_datadir/dbus-1/interfaces/org.kde.kfilereplace.xml
%_kde_libdir/kde4/libkfilereplacepart.so

#--------------------------------------------------------------------------

%package -n kde4-kommander
Summary: Kommander
Group: Graphical desktop/KDE
Provides: kommander4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: %name-core

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
Requires: %name-core

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
%dir %_kde_docdir/HTML/en/kimagemapeditor
%doc %_kde_docdir/HTML/en/kimagemapeditor/index.cache.bz2
%doc %_kde_docdir/HTML/en/kimagemapeditor/index.docbook
%_kde_datadir/icons/locolor/*/apps/kimagemapeditor.png
%_kde_datadir/icons/hicolor/*/apps/kimagemapeditor.png
%_kde_datadir/kde4/services/kimagemapeditorpart.desktop
%_kde_libdir/kde4/libkimagemapeditor.so

#--------------------------------------------------------------------------

%package -n kde4-kxsldbg
Summary: Kxsldbg
Group: Graphical desktop/KDE
Provides: kxsldbg4
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: %name-core

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
%doc %_kde_docdir/HTML/en/kxsldbg/*.png
%doc %_kde_docdir/HTML/en/kxsldbg/index.cache.bz2
%doc %_kde_docdir/HTML/en/kxsldbg/*.docbook
%doc %_kde_docdir/HTML/en/xsldbg/index.cache.bz2
%doc %_kde_docdir/HTML/en/xsldbg/*.docbook
%_kde_datadir/icons/hicolor/*/actions/xsldbg_*
%_kde_datadir/kde4/services/kxsldbg_part.desktop
%_datadir/dbus-1/interfaces/org.kde.kxsldbg.kxsldbg.xml
%_kde_libdir/kde4/libkxsldbgpart.so

#--------------------------------------------------------------------------

%prep
%setup -q -n kdewebdev-%version 
#TODO Readd
#-a 1 -a 2 -a 3 -a 4 -a 5

%build
%cmake_kde4

%install
rm -fr %buildroot
cd build

make DESTDIR=%buildroot install

# TODO Readd
#%__mkdir -p %buildroot%_kde_datadir/doc/quanta
#cp -r css/ %buildroot%_kde_datadir/doc/quanta
#cp -r html/ %buildroot%_kde_datadir/doc/quanta
#cp -r javascript/ %buildroot%_kde_datadir/doc/quanta
#cp -r mysql5/ %buildroot%_kde_datadir/doc/quanta
#cp -r php/ %buildroot%_kde_datadir/doc/quanta

rm -f %buildroot%_kde_libdir/libkdev*.so

%clean
rm -rf $RPM_BUILD_ROOT

