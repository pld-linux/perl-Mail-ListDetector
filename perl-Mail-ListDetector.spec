#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	ListDetector
Summary:	Mail::ListDetector - Perl extension for detecting mailing list messages
Summary(pl):	Mail::ListDetector - rozszerzenie Perla do wykrywania poczty z list dyskusyjnych
Name:		perl-Mail-ListDetector
Version:	0.29
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ffbc9a98dedd77682dc2b63d5c212d9
BuildRequires:	perl-devel >= 5
BuildRequires:	rpm-perlprov >= 4.1-13
%{!?_without_tests:BuildRequires:	perl-Email-Valid}
Requires:	perl-Email-Valid
Requires:	perl-URI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module analyzes Mail::Internet objects.  It returns a
Mail::ListDetector::List object representing the mailing list.

The RFC2369 mailing list detector is also capable of matching some
Mailman and Ezmlm messages.

%description -l pl
Ten modu³ analizuje obiekty Mail::Internet.  Zwraca obiekt
Mail::ListDetector::List, reprezentuj±cy listê dyskusyjn±.

Zgodny z RFC2369 kod do rozpoznawania list jest tak¿e zdolny do
wy³apywania czê¶ci wiadomo¶ci, produkowanych przez programy Mailman
i Ezmlm.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -D examples/sample.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/sample.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* AUTHORS BUGS README TODO
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/ListDetector
# empty autosplit.ix
%{perl_vendorlib}/auto/Mail/ListDetector
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
