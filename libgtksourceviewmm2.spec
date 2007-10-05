#
# Conditional build:
%bcond_without	apidocs		# don't generate documentation with doxygen
#
Summary:	A C++ binding of GtkSourceView2
Summary(pl.UTF-8):	Wiązania C++ dla GtkSourceView2
Name:		libgtksourceviewmm2
Version:	1.9.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgtksourceviewmm/1.9/libgtksourceviewmm-%{version}.tar.bz2
# Source0-md5:	bdd4586b3dbddd00a475d5569a36b391
URL:		http://home.gna.org/gtksourceviewmm/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	gtkmm-devel >= 2.12.1
BuildRequires:	gtksourceview2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSourceViewMM2 is a C++ binding of GtkSourceView2, an extension to
the text widget included in GTK+ 2.x adding syntax highlighting and
other features typical for a source file editor.

%description -l pl.UTF-8
GtkSourceViewMM2 to wiązania C++ dla GtkSourceView2 - rozszerzenia
tekstowego widgetu będącego częścią GTK+ 2.x, dodającego kolorowanie
składni oraz inne właściwości typowe dla edytora kodu źródłowego.

%package devel
Summary:	Header files for libgtksourceviewmm2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgtksourceviewmm2
Group:		Development/Libraries
Requires:	gtkmm-devel >= 2.12.1
Requires:	gtksourceview2-devel >= 2.0.0
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgtksourceviewmm2 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgtksourceviewmm2.

%package static
Summary:	Static libgtksourceviewmm2 library
Summary(pl.UTF-8):	Statyczna biblioteka libgtksourceviewmm2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgtksourceviewmm2 library.

%description static -l pl.UTF-8
Statyczna biblioteka libgtksourceviewmm2.

%package apidocs
Summary:	libgtksourceviewmm2 API documentation
Summary(pl.UTF-8):	Dokumentacja API libgtksourceviewmm2
Group:		Documentation

%description apidocs
libgtksourceviewmm2 API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libgtksourceviewmm2.

%prep
%setup -q -n libgtksourceviewmm-%{version}

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-docs \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with apidocs}
rm -rf $RPM_BUILD_ROOT%{_docdir}/libgtksourceviewmm-1.0
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgtksourceviewmm-2.0.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceviewmm-2.0.so
%{_libdir}/libgtksourceviewmm-2.0.la
%{_libdir}/gtksourceviewmm-2.0
%{_includedir}/gtksourceviewmm-2.0
%{_pkgconfigdir}/gtksourceviewmm-2.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtksourceviewmm-2.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/reference/html
%endif
