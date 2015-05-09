Summary:	Bijiben - notes editor
Summary(pl.UTF-8):	Bijiben - edytor notatek
Name:		bijiben
Version:	3.16.1
Release:	1
License:	GPL v3+
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/bijiben/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	f08f87770a6878a76d7f87fbf1d459e8
URL:		https://wiki.gnome.org/Apps/Bijiben
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	clutter-gtk-devel
BuildRequires:	evolution-data-server-devel >= 3.13.90
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	gnome-common
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gtk+3-devel >= 3.11.4
BuildRequires:	gtk-webkit3-devel
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	libuuid-devel
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
Requires:	glib2 >= 1:2.28
Requires:	gtk+3 >= 3.11.4
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

# outdated macro
%{__sed} -i -e '/^GNOME_DOC_PREPARE/d' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-update-mimedb

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor
%update_mime_database

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/bijiben
%attr(755,root,root) %{_libexecdir}/bijiben-shell-search-provider
%{_datadir}/bijiben
%{_datadir}/appdata/bijiben.appdata.xml
%{_desktopdir}/bijiben.desktop
%{_datadir}/dbus-1/services/org.gnome.Bijiben.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.bijiben.gschema.xml
%{_datadir}/gnome-shell/search-providers/bijiben-search-provider.ini
%{_iconsdir}/HighContrast/scalable/apps/bijiben.svg
%{_iconsdir}/hicolor/*/apps/bijiben.png
%{_datadir}/mime/packages/bijiben.xml
