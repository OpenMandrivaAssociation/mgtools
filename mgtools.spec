%define name	mgtools
%define version	1.0.1
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Tools and scripts to edit and visualize Meta Grammars
License:	GPL
Group:		Sciences/Computer science
Source:		ftp://ftp.inria.fr/INRIA/Projects/Atoll/Eric.Clergerie/TAG/%{name}-%{version}.tar.bz2
Url:		http://atoll.inria.fr/packages/packages.html#mgtools
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
%configure
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
%{_datadir}/aclocal/%{name}.m4
%{_datadir}/emacs/site-lisp/mg.el
%{_datadir}/xslt

