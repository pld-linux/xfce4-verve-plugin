#
%define		srcname		verve-plugin
#
Summary:	Verve plugin for Xfce panel
Name:		xfce4-%{srcname}
Version:	0.3.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/verve-plugin/%{srcname}-%{version}.tar.bz2
# Source0-md5:	85701b960da6bb10762b460c23b84c15
URL:		http://goodies.xfce.org/projects/panel-plugins/verve-plugin
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	intltool
BuildRequires:	libexo-devel >= 0.3.2
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Verve plugin is a comfortable command line plugin for the Xfce panel.
It supports several nice features, such as:
- command history
- auto-completion (including command history)
- open URLs and e-mail addresses in your favourite applications
- focus grabbing via D-BUS
- custom input field width

%prep
%setup -q -n %{srcname}-%{version}

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

%find_lang %{srcname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{srcname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/verve-focus
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-verve-plugin
%{_datadir}/xfce4/panel-plugins/verve.desktop
