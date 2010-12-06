%define name	mgtools
%define version	2.2.1
%define release	%mkrel 2

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

