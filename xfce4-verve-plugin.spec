Summary:	Verve plugin for Xfce panel
Summary(pl.UTF-8):	Wtyczka Verve dla panelu Xfce
Name:		xfce4-verve-plugin
Version:	0.3.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/verve-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	1dee60c7c4e11130226cab381fcb945c
URL:		http://goodies.xfce.org/projects/panel-plugins/verve-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	exo-devel >= 0.3.2
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
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
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}
mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/verve-focus
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-verve-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-verve-plugin.desktop
