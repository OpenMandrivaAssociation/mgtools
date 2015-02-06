%define name	mgtools
%define version	2.2.1
%define release	3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Tools and scripts to edit and visualize Meta Grammars
License:	GPL
Group:		Sciences/Computer science
Source:		https://gforge.inria.fr/frs/download.php/5683/%{name}-%{version}.tar.gz
Url:		http://alpage.inria.fr/catalogue.en.html#mgtools
Buildrequires:	libxml2-devel
Buildrequires:	bison
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
mgtools collects several useful tools and scripts to edit and visualize Meta
Grammars

    * smg2xml to convert MG from a simple format (smg) to XML format
    * mg.el an Emacs mode to edit MG (in both XML and SMG formats)
    * mg2smg.xsl an XSLT stylesheet to convert from XML to SMG
    * mgviewer.pl a graphical viewer/editor for MG
    * mg*2html.xsl several XSLT stylesheets to get HTML views on MG
    * mg2*.xsl several XSLT stylesheets to convert to other formats

%prep
%setup -q

%build
export LDFLAGS=-L%{_libdir}/DyAlog
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL README
%{_bindir}/*
%{_libdir}/pkgconfig/mgtools.pc
%{_datadir}/emacs/site-lisp/mg.el
%{_datadir}/mgtools



%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-2mdv2011.0
+ Revision: 612865
- the mass rebuild of 2010.1 packages

* Sat Jan 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.1-1mdv2010.1
+ Revision: 492189
- new version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-5mdv2010.0
+ Revision: 430025
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2009.0
+ Revision: 252387
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.0.1-2mdv2008.1
+ Revision: 140953
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import mgtools


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-2mdv2007.0
- Rebuild

* Tue Mar 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdk
- new version
- drop patch (merged upstream)

* Mon Nov 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.0.1-3mdk 
- buildrequires bison instead of byacc, as generated code has problems otherwise

* Mon Nov 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.0.1-2mdk 
- fix buildrequires

* Tue Nov 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.0.1-1mdk 
- first mdk release
