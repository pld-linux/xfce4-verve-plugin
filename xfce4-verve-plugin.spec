Summary:	Verve plugin for Xfce panel
Summary(pl.UTF-8):	Wtyczka Verve dla panelu Xfce
Name:		xfce4-verve-plugin
Version:	2.1.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-verve-plugin/2.1/%{name}-%{version}.tar.xz
# Source0-md5:	06527afc8e81d0354761f48ca1aab074
URL:		https://goodies.xfce.org/projects/panel-plugins/verve-plugin
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	exo-devel >= 0.10.4
BuildRequires:	glib2-devel >= 2.50.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.16.0
BuildRequires:	libxfce4util-devel >= 4.16.0
BuildRequires:	pcre2-8-devel >= 10.00
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.16.0
BuildRequires:	xfce4-panel-devel >= 4.16.0
Requires:	xfce4-panel >= 4.16.0
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
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hye,ie,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS THANKS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libverve.so
%{_datadir}/xfce4/panel/plugins/xfce4-verve-plugin.desktop
