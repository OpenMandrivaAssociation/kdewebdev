# remove it when kde4 will be official kde package
%define _prefix /opt/kde4/
%define _libdir %_prefix/%_lib
%define _datadir %_prefix/share/
%define _bindir %_prefix/bin
%define _includedir %_prefix/include/
%define _iconsdir %_datadir/icons/
%define _sysconfdir %_prefix/etc/
%define _docdir %_datadir/doc/

%define branch_date 20070117

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

%define lib_name_orig lib%name
%define lib_major 0
%define lib_name %mklibname %name %lib_major


Name:		kdewebdev4
Version: 	3.80.2
Release:    	%mkrel 0.%branch_date.2
License:	GPL
Packager:       Mandriva Linux KDE Team <kde@mandriva.com>
Summary:	A web editor for the KDE Desktop Environment
Epoch:		1
URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/
%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdewebdev-%version-%branch_date.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdewebdev-%version.tar.bz2
%endif
Group:		Graphical desktop/KDE
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:  pam
BuildRequires:  diffutils
BuildRequires: jpeg-devel
BuildRequires:	png-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
%define mini_release %mkrel 0.%branch_date.1
BuildRequires: kdelibs4-devel >= %version-%mini_release
BuildRequires:	freetype2 
BuildRequires:	kdevelop4-devel
Requires:		tidy
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
A html editor for the K Desktop Environment.

%post
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files
%defattr(-,root,root)
%_bindir/quanta
%_bindir/kxsldbg
%_bindir/xsldbg

%_bindir/kimagemapeditor
%_bindir/klinkstatus
%dir %_datadir/apps/quanta
%_datadir/apps/quanta/*
%dir %_datadir/apps/kimagemapeditor/
%_datadir/apps/kimagemapeditor/*
%_iconsdir/*/*/*/kimagemap*
%_datadir/services/kimagemapeditorpart.desktop
%_libdir/kde4/libkimagemapeditor.*
%_datadir/applications/kde/kimagemapeditor.desktop
%_datadir/applications/kde/klinkstatus.desktop
%_datadir/applications/kde/kxsldbg.desktop
%_datadir/applications/kde/quanta.desktop
%_datadir/services/klinkstatus_part.desktop
%dir %_datadir/apps/klinkstatus
%_datadir/apps/klinkstatus/*
%dir %_datadir/apps/klinkstatuspart/
%_datadir/apps/klinkstatuspart/*.rc
%dir %_datadir/apps/klinkstatuspart/pics/
%_datadir/apps/klinkstatuspart/pics/*.png
%_libdir/kde4/libklinkstatuspart.*
%_libdir/kde4/libkdevcreatequantaproject.so
%_libdir/kde4/libkdevhtmlpreview.so
%_libdir/kde4/libkdevprojecttree.so
%_libdir/kde4/libkdevquantacore.so
%_libdir/kde4/libkdevquantafilestree.so
%_libdir/kde4/libkdevquantaproject.so
%_libdir/kde4/libkdevstructuretree.so
%_libdir/kde4/libkdevtagdialogs.so
%_libdir/kde4/libkdevtemplatestree.so
%_libdir/kde4/libkdevusertoolbars.so


%_iconsdir/*/*/*/klinkstat*
%_iconsdir/*/*/actions/*
%_iconsdir/*/*/*/quanta*
%dir %_datadir/apps/kxsldbg/
%_datadir/apps/kxsldbg/*
%dir %_datadir/apps/kxsldbgpart/
%_datadir/apps/kxsldbgpart/*
%_libdir/kde4/libkxsldbgpart.*
%_datadir/services/kxsldbg_part.desktop

%_datadir/apps/kdevusertoolbars/pics/*.png
%_datadir/apps/xsldbg/*.xml
%_datadir/apps/xsldbg/*.xsl
%_datadir/apps/xsldbg/testdoc.dtd
%_datadir/apps/xsldbg/testdoc.xml
%_datadir/apps/xsldbg/testdoc.xsl
%_datadir/apps/xsldbg/xsldbghelp.xsl
%_datadir/config.kcfg/quanta.kcfg
%_datadir/mimelnk/application/x-quanta.desktop
%_datadir/services/kdevcreatequantaproject.desktop
%_datadir/services/kdevhtmlpreview.desktop
%_datadir/services/kdevprojecttree.desktop
%_datadir/services/kdevquantacore.desktop
%_datadir/services/kdevquantafilestree.desktop
%_datadir/services/kdevquantaproject.desktop
%_datadir/services/kdevstructuretree.desktop
%_datadir/services/kdevtagdialogs.desktop
%_datadir/services/kdevtemplatestree.desktop
%_datadir/services/kdevusertoolbars.desktop
%_datadir/servicetypes/kdevelopquanta.desktop

%_datadir/apps/kdevcreatequantaproject/kdevcreatequantaproject.rc
%_datadir/apps/kdevcreatequantaproject/pics/*.png
%_datadir/apps/kdevcreatequantaproject/quanta-project.template
%_datadir/apps/kdevelop/profiles/IDE/quanta/profile.config
%_datadir/apps/kdevelop/profiles/IDE/quanta/quanta.appwizard
%_datadir/apps/kdevhtmlpreview/kdevhtmlpreview.rc
%_datadir/apps/kdevprojecttree/kdevprojecttree.rc
%_datadir/apps/kdevquantacore/kdevquantacore.rc
%_datadir/apps/kdevquantafilestree/kdevquantafilestree.rc
%_datadir/apps/kdevquantaproject/kdevquantaproject.rc
%_datadir/apps/kdevstructuretree/kdevstructuretree.rc
%_datadir/apps/kdevtagdialogs/kdevtagdialogs.rc
%_datadir/apps/kdevtemplatestree/kdevtemplatestree.rc
%_datadir/apps/kdevusertoolbars/global
%_datadir/apps/kdevusertoolbars/kdevusertoolbars.rc

#--------------------------------------------------------------------------

%package kfilereplace
Summary:	Kfilereplace
Group:		Graphical desktop/KDE
Provides:	kfilereplace4

%description kfilereplace
Kfilereplace program

%post kfilereplace
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun kfilereplace
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files kfilereplace
%defattr(-,root,root)
%_bindir/kfilereplace
%dir %_datadir/apps/kfilereplacepart
%_datadir/apps/kfilereplacepart/*
%dir %_datadir/apps/kfilereplace/
%_datadir/apps/kfilereplace/*
%_datadir/services/kfilereplacepart.desktop
%_datadir/applications/kde/kfilereplace.desktop
%_libdir/kde4/libkfilereplacepart.*
%_iconsdir/*/*/*/kfilerep*

#--------------------------------------------------------------------------

%package kommander
Summary:	Kommander
Group:		Graphical desktop/KDE
Provides:	kommander4
Requires:	%lib_name-kommander = %epoch:%version-%release
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description kommander
Kommander program

%post kommander
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun kommander
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%files kommander
%defattr(-,root,root)
#--------------------------------------------------------------------------

%package -n %lib_name-kommander
Summary:	Library for Kommander
Group:		Graphical desktop/KDE

%description -n %lib_name-kommander
Kommander program

%post -n %lib_name-kommander -p /sbin/ldconfig
%postun -n %lib_name-kommander -p /sbin/ldconfig

%files -n %lib_name-kommander
%defattr(-,root,root)
#--------------------------------------------------------------------------

%package -n %lib_name-kommander-devel
Summary:	Header for kommander
Group:		Development/KDE and Qt
Requires:	%lib_name-kommander = %epoch:%version-%release

%description -n %lib_name-kommander-devel
Header for Kommander

%files -n %lib_name-kommander-devel
%defattr(-,root,root)
#--------------------------------------------------------------------------

%package -n %lib_name
Summary:    Library for kdewebdev
Group:      Graphical desktop/KDE

%description -n %lib_name
Library files for kdewebdev.

%files -n %lib_name
%defattr(-,root,root)
%_libdir/libkdevquanta.so.*
#--------------------------------------------------------------------------

%package -n %lib_name-devel
Summary:    Development library for kdewebdev
Group:      Development/KDE and Qt

%description -n %lib_name-devel
Development library files for quanta.
%files -n %lib_name-devel
%defattr(-,root,root)
%_datadir/dbus-1/interfaces/org.kde.kfilereplace.xml
%_datadir/dbus-1/interfaces/org.kde.kxsldbg.kxsldbg.xml
%_libdir/libkdevquanta.so
#--------------------------------------------------------------------------

%prep
%setup -q -nkdewebdev-%version-%branch_date


%build
cd $RPM_BUILD_DIR/kdewebdev-%version-%branch_date
mkdir build
cd build
export QTDIR=/usr/lib/qt4/
export PATH=$QTDIR/bin:$PATH

cmake -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=Debug \
%endif
%if "%{_lib}" != "lib"
      -DLIB_SUFFIX=64 \
%endif
        ../

%make


%install
rm -fr %buildroot
cd $RPM_BUILD_DIR/kdewebdev-%version-%branch_date
cd build

make DESTDIR=%buildroot install


#kdedesktop2mdkmenu.pl kdewebdev "Internet/Web editors" $RPM_BUILD_ROOT/%_datadir/applications/kde/quanta.desktop $RPM_BUILD_ROOT/%_menudir/quanta

#kdedesktop2mdkmenu.pl kdewebdev-kommander "More applications/Development/Development Environments" $RPM_BUILD_ROOT/%_datadir/applications/kde/kmdr-editor.desktop $RPM_BUILD_ROOT/%_menudir/kdewebdev-kmdr-editor

#kdedesktop2mdkmenu.pl kdewebdev "More applications/Development/Development Environments" $RPM_BUILD_ROOT/%_datadir/applications/kde/kxsldbg.desktop $RPM_BUILD_ROOT/%_menudir/kdewebdev-kxsldbg

#kdedesktop2mdkmenu.pl kdewebdev "More applications/Development/Development Environments" $RPM_BUILD_ROOT/%_datadir/applications/kde/klinkstatus.desktop $RPM_BUILD_ROOT/%_menudir/kdewebdev-klinkstatus

#kdedesktop2mdkmenu.pl kdewebdev-kfilereplace "More applications/Development/Development environments" $RPM_BUILD_ROOT/%_datadir/applications/kde/kfilereplace.desktop $RPM_BUILD_ROOT/%_menudir/kdewebdev-kfilereplace

#kdedesktop2mdkmenu.pl kdewebdev-kommander "More applications/Development/Development Environments" $RPM_BUILD_ROOT/%_datadir/applications/kde/kimagemapeditor.desktop $RPM_BUILD_ROOT/%_menudir/kdewebdev-kimagemapeditor



%clean
rm -rf $RPM_BUILD_ROOT



