Summary:	Bijiben - notes editor
Summary(pl.UTF-8):	Bijiben - edytor notatek
Name:		bijiben
Version:	3.34.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/bijiben/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	b38ecaa7c14cf09d646568b92b8e6530
URL:		https://wiki.gnome.org/Apps/Bijiben
BuildRequires:	appstream-glib-devel
BuildRequires:	clutter-gtk-devel
BuildRequires:	evolution-data-server-devel >= 3.33.2
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	gtk-webkit4-devel >= 2.10.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libuuid-devel
BuildRequires:	meson >= 0.43.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 2.0
BuildRequires:	xz
BuildRequires:	yelp-tools
BuildRequires:	zeitgeist-devel >= 0.9
Requires(post,postun):	glib2 >= 1:2.54.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires:	evolution-data-server >= 3.33.2
Requires:	glib2 >= 1:2.54.0
Requires:	gtk+3 >= 3.20.0
Requires:	gtk-webkit4 >= 2.10.0
Requires:	hicolor-icon-theme
Requires:	shared-mime-info
Requires:	tracker-libs >= 2.0
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
%meson build \
	-Dupdate_mimedb=false \
	-Dzeitgeist=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%doc AUTHORS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/bijiben
%attr(755,root,root) %{_libexecdir}/bijiben-shell-search-provider
%{_datadir}/bijiben
%{_datadir}/dbus-1/services/org.gnome.Notes.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.Notes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.bijiben.enums.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Notes-search-provider.ini
%{_datadir}/metainfo/org.gnome.Notes.appdata.xml
%{_datadir}/mime/packages/org.gnome.Notes.xml
%{_desktopdir}/org.gnome.Notes.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Notes.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Notes-symbolic.svg
