%define	modname	Time-Piece
%define modver 1.3204

Summary:	Object Oriented time objects
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Time/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
This module replaces the standard localtime and gmtime functions with
implementations that return objects. It does so in a backwards compatible
manner, so that using localtime/gmtime in the way documented in perlfunc will
still return what you expect.

The module actually implements most of an interface described by Larry Wall on
the perl5-porters mailing list here:
http://www.xray.mpe.mpg.de/mailing-lists/perl5-porters/2000-01/msg00241.html

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/Time
%{perl_vendorarch}/auto/Time
%{_mandir}/man3/*
