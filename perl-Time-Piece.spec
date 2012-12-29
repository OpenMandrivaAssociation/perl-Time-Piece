%define	modname	Time-Piece
%define	modver	1.20

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	9

Summary:	Object Oriented time objects
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Time/%{modname}-%{modver}.tar.gz

BuildRequires:	perl-devel

%description
This module replaces the standard localtime and gmtime functions with
implementations that return objects. It does so in a backwards compatible
manner, so that using localtime/gmtime in the way documented in perlfunc will
still return what you expect.

The module actually implements most of an interface described by Larry Wall on
the perl5-porters mailing list here:
http://www.xray.mpe.mpg.de/mailing-lists/perl5-porters/2000-01/msg00241.html

%prep
%setup -q -n %{modname}-%{modver}

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
%{_mandir}/*/*

%changelog
* Thu Dec 20 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.200.0-9
- rebuild for new perl-5.16.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-7mdv2012.0
+ Revision: 765791
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-6
+ Revision: 764296
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-5
+ Revision: 763286
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.200.0-4
+ Revision: 667400
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.200.0-3mdv2011.0
+ Revision: 564586
- rebuild for perl 5.12.1

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.1
+ Revision: 526458
- update to 1.20

* Thu Feb 11 2010 Jérôme Quelin <jquelin@mandriva.org> 1.190.0-1mdv2010.1
+ Revision: 504074
- update to 1.19

* Tue Feb 02 2010 Jérôme Quelin <jquelin@mandriva.org> 1.170.0-1mdv2010.1
+ Revision: 499487
- update to 1.17

* Tue Jan 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.1
+ Revision: 490070
- update to 1.16

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.150.0-1mdv2010.0
+ Revision: 405766
- rebuild using %%perl_convert_version

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2010.0
+ Revision: 390366
- update to new version 1.15

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdv2010.0
+ Revision: 373752
- update to new version 1.14

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.13-2mdv2009.0
+ Revision: 224570
- rebuild

* Mon Mar 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdv2008.1
+ Revision: 177899
- update to new version 1.13

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.12-2mdv2008.1
+ Revision: 151404
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2008.1
+ Revision: 110281
- update to new version 1.12


* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2007.0
+ Revision: 111256
- fix build dependencies
- Import perl-Time-Piece

* Sun Jan 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2007.1
- first mdv release

