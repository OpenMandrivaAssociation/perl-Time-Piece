%define module	Time-Piece
%define name	perl-%{module}
%define version 1.12
%define release %mkrel 2

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    Object Oriented time objects
License:	    GPL
Group:		    Development/Perl
URL:		    http://search.cpan.org/dist/%{module}
Source:		    http://www.cpan.org/modules/by-module/Time/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This module replaces the standard localtime and gmtime functions with
implementations that return objects. It does so in a backwards compatible
manner, so that using localtime/gmtime in the way documented in perlfunc will
still return what you expect.

The module actually implements most of an interface described by Larry Wall on
the perl5-porters mailing list here:
http://www.xray.mpe.mpg.de/mailing-lists/perl5-porters/2000-01/msg00241.html

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Time
%{perl_vendorarch}/auto/Time
%{_mandir}/*/*


