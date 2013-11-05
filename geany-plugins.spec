Summary:	Plugins for Geany
Name:		geany-plugins
Version:	1.23
Release:	2
License:	GPL v2+
Group:		Development/Tools
Source0:	http://plugins.geany.org/geany-plugins/%{name}-%{version}.tar.bz2
# Source0-md5:	d851dbdaf95fb8b74ece43c0a973b748
URL:		http://www.geany.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ctpl-devel
BuildRequires:	enchant-devel
BuildRequires:	geany-devel
BuildRequires:	gtk+-webkit-devel
BuildRequires:	gtkspell-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	lua-devel
BuildRequires:	pkg-config
BuildRequires:	vte2-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	enchant-hunspell
Requires:	geany
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugins for Geany.

%prep
%setup -q

%build
export CONFIG_SHELL=/bin/bash
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I build -I build/cache
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/geany/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/geany-plugins/*/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/geanylua
%attr(755,root,root) %{_libdir}/geany/*.so
%attr(755,root,root) %{_libdir}/geany-plugins/geanylua/*.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/geanygendoc
%{_datadir}/%{name}/debugger
%{_datadir}/%{name}/geanygendoc/filetypes
%{_datadir}/%{name}/geanylua
%{_datadir}/%{name}/scope
%{_iconsdir}/hicolor/*/apps/gproject-*.png

