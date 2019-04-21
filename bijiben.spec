Summary:	Bijiben - notes editor
Summary(pl.UTF-8):	Bijiben - edytor notatek
Name:		bijiben
Version:	3.30.3
Release:	2
License:	GPL v3+
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/bijiben/3.30/%{name}-%{version}.tar.xz
# Source0-md5:	5bea00a03622b23319c953b46625e0a5
URL:		https://wiki.gnome.org/Apps/Bijiben
BuildRequires:	appstream-glib-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	evolution-data-server-devel >= 3.13.90
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	gtk-webkit4-devel >= 2.10.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libuuid-devel
BuildRequires:	meson >= 0.43.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 1.0
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildRequires:	zeitgeist-devel >= 0.9
Requires(post,postun):	glib2 >= 1:2.28
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	evolution-data-server >= 3.13.90
Requires:	glib2 >= 1:2.54.0
Requires:	gtk+3 >= 3.20.0
Requires:	gtk-webkit4 >= 2.10.0
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
Requires:	tracker-libs >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bijiben is an attempt to design an intuitive note editor with strong
desktop integration.

%description -l pl.UTF-8
Bijiben to próba zaprojektowania intuicyjnego edytora notatek znacząco
zintegrowanego z pulpitem.

%prep
%setup -q

%build
%meson build
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor
%update_mime_database

%postun
%glib_compile_schemas
%update_icon_cache hicolor
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/bijiben
%attr(755,root,root) %{_libexecdir}/bijiben-shell-search-provider
%{_datadir}/bijiben
%{_datadir}/metainfo/org.gnome.bijiben.appdata.xml
%{_desktopdir}/org.gnome.bijiben.desktop
%{_datadir}/dbus-1/services/org.gnome.bijiben.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.bijiben.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.bijiben.enums.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.bijiben-search-provider.ini
%{_iconsdir}/hicolor/*x*/apps/org.gnome.bijiben.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.bijiben-symbolic.svg
%{_datadir}/mime/packages/org.gnome.bijiben.xml
