Name:		kdewebdev4
Version: 4.9.3
Release: 1
Epoch:		1
Summary:	A web editor for the KDE Desktop Environment
Group:		Graphical desktop/KDE
License:	GPLv2+
URL:		http://kdewebdev.org/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdewebdev-%{version}.tar.xz
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	boost-devel
BuildRequires:	ruby-devel
BuildRequires:	tidy-devel
BuildRequires:	automoc4
Requires:	kimagemapeditor
Requires:	klinkstatus
Requires:	kfilereplace
Requires:	kommander

%description
A web editor for the KDE Desktop Environment

%files
%doc README

#--------------------------------------------------------------------

%package -n klinkstatus
Summary:	klinkstatus
Group:		Graphical desktop/KDE
Requires:	tidy

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

#--------------------------------------------------------------------------

%define klinkstatuscommon_major 4
%define libklinkstatuscommon %mklibname klinkstatuscommon %{klinkstatuscommon_major}

%package -n %{libklinkstatuscommon}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libklinkstatuscommon}
KDE 4 core library.

%files -n %{libklinkstatuscommon}
%{_kde_libdir}/libklinkstatuscommon.so.%{klinkstatuscommon_major}*


#--------------------------------------------------------------------------

%package -n kfilereplace
Summary:	kfilereplace
Group:		Graphical desktop/KDE

%description -n kfilereplace
Kfilereplace program

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

#--------------------------------------------------------------------------

%define kommanderwidgets_major 4
%define libkommanderwidgets %mklibname kommanderwidgets %{kommanderwidgets_major}

%package -n %{libkommanderwidgets}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkommanderwidgets}
KDE 4 core library.

%files -n %{libkommanderwidgets}
%{_kde_libdir}/libkommanderwidgets.so.%{kommanderwidgets_major}*

#--------------------------------------------------------------------------

%define kommandercore_major 4
%define libkommandercore %mklibname kommandercore %{kommandercore_major}

%package -n %{libkommandercore}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkommandercore}
KDE 4 core library.

%files -n %{libkommandercore}
%{_kde_libdir}/libkommandercore.so.%{kommandercore_major}*

#--------------------------------------------------------------------------

%package -n kommander
Summary:	Kommander
Group:		Graphical desktop/KDE

%description -n kommander
Kommander program

%files -n kommander
%{_kde_bindir}/kommander
%{_kde_datadir}/applnk/.hidden/kommander.desktop

#--------------------------------------------------------------------------

%package -n kimagemapeditor
Summary:	Kimagemapeditor
Group:		Graphical desktop/KDE

%description -n kimagemapeditor
kimagemapeditor program

%files -n kimagemapeditor
%{_kde_bindir}/kimagemapeditor
%{_kde_applicationsdir}/kimagemapeditor.desktop
%{_kde_appsdir}/kimagemapeditor
%{_kde_iconsdir}/hicolor/*/apps/kimagemapeditor.png
%{_kde_services}/kimagemapeditorpart.desktop
%{_kde_libdir}/kde4/libkimagemapeditor.so
%{_kde_docdir}/*/*/kimagemapeditor

#--------------------------------------------------------------------------

%if 0
%package -n kxsldbg
Summary:	Kxsldbg
Group:		Graphical desktop/KDE

%description -n kxsldbg
kxsldbg program

%files -n kxsldbg
%{_kde_bindir}/kxsldbg
%{_kde_bindir}/xsldbg
%{_kde_applicationsdir}/kxsldbg.desktop
%{_kde_applicationsdir}/xsldbg.desktop
%{_kde_appsdir}/kxsldbg
%{_kde_appsdir}/xsldbg
%{_kde_appsdir}/kxsldbgpart
%{_kde_iconsdir}/hicolor/*/apps/kxsldbg.*
%{_kde_iconsdir}/hicolor/*/actions/xsldbg*
%{_kde_services}/kxsldbg_part.desktop
%{_kde_libdir}/kde4/libkxsldbgpart.so
%{_kde_docdir}/HTML/en/kxsldbg
%{_kde_docdir}/HTML/en/xsldbg
%{_kde_mandir}/man1/xsldbg.1*
%endif

#--------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kde4-macros
Requires:	kdelibs4-devel
Requires:	%{libkommandercore} = %{EVRD}
Requires:	%{libkommanderwidgets} = %{EVRD}
Requires:	%{libklinkstatuscommon} = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_datadir}/dbus-1/interfaces/*
%{_kde_includedir}/*
%{_kde_libdir}/*.so

#--------------------------------------------------------------------------

%prep
%setup -q -n kdewebdev-%{version}

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

