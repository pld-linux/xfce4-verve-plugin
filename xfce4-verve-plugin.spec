Summary:	Verve plugin for Xfce panel
Summary(pl.UTF-8):	Wtyczka Verve dla panelu Xfce
Name:		xfce4-verve-plugin
Version:	2.0.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-verve-plugin/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	94429b1be9d66ba9b31e4aafb726a8c7
URL:		http://goodies.xfce.org/projects/panel-plugins/verve-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	exo-devel >= 0.10.4
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRequires:	xfce4-panel-devel >= 4.14.0
Requires:	xfce4-panel >= 4.14.0
Obsoletes:	xfce4-minicmd-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Verve plugin is a comfortable command line plugin for the Xfce panel.
It supports several nice features, such as:
- command history
- auto-completion (including command history)
- open URLs and e-mail addresses in your favourite applications
- focus grabbing via D-BUS
- custom input field width

%description -l pl.UTF-8
Wtyczka Verve to wtyczka wygodnej linii poleceń dla panelu Xfce.
Obsługuje kilka przyjemnych elementów, takich jak:
- historię poleceń
- automatyczne dopełnianie (wraz z historią poleceń)
- otwieranie URL-i i adresów e-mail w ulubionych aplikacjach
- przechwytywanie ogniska poprzez D-BUS
- ustawialną szerokość pola wprowadzania

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libverve.so
%{_datadir}/xfce4/panel/plugins/xfce4-verve-plugin.desktop
