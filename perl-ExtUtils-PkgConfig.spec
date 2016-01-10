#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	ExtUtils
%define		pnam	PkgConfig
Summary:	ExtUtils::PkgConfig - simplistic interface to pkg-config
Summary(pl.UTF-8):	ExtUtils::PkgConfig - prosty interfejs do pkg-config
Name:		perl-ExtUtils-PkgConfig
Version:	1.15
Release:	1
License:	LGPL v2+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1872e659cf2bb0b2471d75fce735e622
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	pkgconfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::PkgConfig is a very simplistic interface to pkg-config
utility.

%description -l pl.UTF-8
ExtUtils::PkgConfig jest bardzo prostym interfejsem do narzędzia
pkg-config.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/ExtUtils/PkgConfig.pm
%{_mandir}/man3/ExtUtils::PkgConfig.3pm*
