%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	ListDetector
Summary:	%{pdir}::%{pnam} -- Perl extension for detecting mailing list messages
Summary(pl):	%{pdir}::%{pnam} -- rozszerzenie Perla do wykrywania poczty z list dyskusyjnych
Name:		perl-%{pdir}-%{pnam}
Version:	0.22
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -D examples/sample.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/sample.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* AUTHORS BUGS README TODO
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
