#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	ListDetector
Summary:	Mail::ListDetector - Perl extension for detecting mailing list messages
Summary(pl.UTF-8):	Mail::ListDetector - rozszerzenie Perla do wykrywania poczty z list dyskusyjnych
Name:		perl-Mail-ListDetector
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab3554c5bd87cf22dc720b0847780c77
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Abstract
BuildRequires:	perl-Email-Valid
%endif
Requires:	perl-Email-Valid
Requires:	perl-URI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module analyzes Mail::Internet objects.  It returns a
Mail::ListDetector::List object representing the mailing list.

The RFC2369 mailing list detector is also capable of matching some
Mailman and Ezmlm messages.

%description -l pl.UTF-8
Ten moduł analizuje obiekty Mail::Internet.  Zwraca obiekt
Mail::ListDetector::List, reprezentujący listę dyskusyjną.

Zgodny z RFC2369 kod do rozpoznawania list jest także zdolny do
wyłapywania części wiadomości, produkowanych przez programy Mailman
i Ezmlm.

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
