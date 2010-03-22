%define upstream_name	 Time-Piece
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Object Oriented time objects
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Time/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
This module replaces the standard localtime and gmtime functions with
implementations that return objects. It does so in a backwards compatible
manner, so that using localtime/gmtime in the way documented in perlfunc will
still return what you expect.

The module actually implements most of an interface described by Larry Wall on
the perl5-porters mailing list here:
http://www.xray.mpe.mpg.de/mailing-lists/perl5-porters/2000-01/msg00241.html

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
