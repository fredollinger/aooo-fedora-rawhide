%define libo_version 3.4.1
%define libo_prerelease r1435053
%define libo_python3 %{nil}

Summary:        Free Software Productivity Suite
Name:           aoo 
Epoch:          1
Version:        %{libo_version}
Release:        %{?libo_prerelease}%{?dist}
License:        (MPLv1.1 or LGPLv3+) and LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and Public Domain and ASL 2.0 and Artistic and MPLv2.0
Group:          Applications/Productivity
URL:            http://apache.org/dyn/aoo-closer.cgi/incubator/ooo/

Source0:        %{source_url}/%{version}%/source/aoo-%{version}-incubating-%{libo_prerelease}-src.tar.bz2

# build tools
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bc
BuildRequires: binutils
BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: findutils
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: gperf
BuildRequires: icu
BuildRequires: make
BuildRequires: perl(Archive::Zip)
BuildRequires: perl(Digest::MD5)
BuildRequires: zip

# libs / headers
BuildRequires: GConf2-devel
BuildRequires: bluez-libs-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: boost-devel
BuildRequires: clucene-core-devel
%endif
BuildRequires: cppunit-devel
BuildRequires: cups-devel
BuildRequires: evolution-data-server-devel
BuildRequires: expat-devel
BuildRequires: fontpackages-devel
BuildRequires: freetype-devel
BuildRequires: gecko-devel
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
%else
BuildRequires: graphite2-devel
BuildRequires: gstreamer1-devel
BuildRequires: gstreamer1-plugins-base-devel
%endif
BuildRequires: gtk2-devel
BuildRequires: hunspell-devel
BuildRequires: hyphen-devel
%if 0%{?fedora}
BuildRequires: kdelibs4-devel
%endif
BuildRequires: libICE-devel
BuildRequires: libXext-devel
BuildRequires: libXinerama-devel
BuildRequires: libXt-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: libcdr-devel
BuildRequires: libcmis-devel >= 0.3.0
%endif
BuildRequires: libcurl-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: libexttextcat-devel
%endif
BuildRequires: libicu-devel
BuildRequires: libidn-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: libjpeg-turbo-devel
BuildRequires: liblangtag-devel >= 0.4.0
BuildRequires: libmspub-devel
BuildRequires: liborcus-devel >= 0.3.0
BuildRequires: libvisio-devel
BuildRequires: libwpd-devel
BuildRequires: libwpg-devel
BuildRequires: libwps-devel
%else
BuildRequires: libjpeg-devel
%endif
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: lpsolve-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: mdds-devel
%endif
BuildRequires: mesa-libGLU-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: mysql-connector-c++-devel
BuildRequires: mythes-devel
%endif
BuildRequires: neon-devel
BuildRequires: nss-devel
BuildRequires: openldap-devel
BuildRequires: openssl-devel
BuildRequires: pam-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: poppler-cpp-devel
%endif
BuildRequires: poppler-devel
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: postgresql-devel
%endif
%if 0%{libo_python3}
BuildRequires: python3-devel >= 3.3.0
%else
BuildRequires: python-devel
%endif
BuildRequires: redland-devel
BuildRequires: sane-backends-devel
BuildRequires: unixODBC-devel
BuildRequires: vigra-devel
BuildRequires: zlib-devel

# java stuff
BuildRequires: ant
BuildRequires: ant-apache-regexp
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-lang
BuildRequires: apache-tomcat-apis
%else
BuildRequires: apache-commons-codec
BuildRequires: apache-commons-lang
BuildRequires: tomcat-servlet-3.0-api
%endif
BuildRequires: bsh
%if 0%{?rhel} && 0%{?rhel} < 7
BuildRequires: hsqldb
%endif
BuildRequires: java-devel
BuildRequires: jakarta-commons-httpclient
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: junit
%endif
BuildRequires: pentaho-reporting-flow-engine

# fonts needed for unit tests
BuildRequires: liberation-mono-fonts >= 1.0
BuildRequires: liberation-sans-fonts >= 1.0
BuildRequires: liberation-serif-fonts >= 1.0

Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
Requires: %{name}-draw = %{epoch}:%{version}-%{release}
Requires: %{name}-math = %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: %{name}-emailmerge = %{epoch}:%{version}-%{release}

%define instdir %{_libdir}
%define baseinstdir %{instdir}/openoffice
%define ureinstdir %{baseinstdir}/ure
%define sdkinstdir %{baseinstdir}/sdk
%define fontname opensymbol

%description
Apache Open Office 
is an Open Source, community-developed, office productivity suite.
It includes the key desktop applications, such as a word processor,
spreadsheet, presentation manager, formula editor and drawing program, with a
user interface and feature set similar to other office suites.  Sophisticated
and flexible, OpenOffice also works transparently with a variety of file
formats, including Microsoft Office File Formats.

%package core
Summary: Core modules for OpenOffice
Group: Applications/Productivity
Requires: %{name}-%{fontname}-fonts = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: liberation-sans-fonts >= 1.0, liberation-serif-fonts >= 1.0, liberation-mono-fonts >= 1.0
Requires: dejavu-sans-fonts, dejavu-serif-fonts, dejavu-sans-mono-fonts
Requires: hyphen-en, hyphen >= 2.4, autocorr-en
%if 0%{?rhel} && 0%{?rhel} < 7
Requires: hunspell-en
%else
Requires: hunspell-en-US
%endif
Requires(pre):    gtk2 >= 2.9.4
Requires(post):   gtk2 >= 2.9.4
Requires(preun):  gtk2 >= 2.9.4
Requires(postun): gtk2 >= 2.9.4
Obsoletes: openoffice-binfilter < 1:4.0.0.0
Obsoletes: openoffice-testtools < 1:3.4.99.1
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-brand%{?_isa} = 1:3.3.0, broffice.org-brand%{?_isa} = 1:3.3.0
%endif

%description core
The shared core libraries and support files for OpenOffice.

%package pyuno
Summary: Python support for OpenOffice
Group: Development/Libraries
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
%if 0%{libo_python3}
Requires: python3
%else
Requires: python
%endif
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-pyuno%{?_isa} = 1:3.3.0
%endif

%description pyuno
Python bindings for the OpenOffice UNO component model. Allows scripts both
external to OpenOffice and within the internal OpenOffice scripting framework
to be written in python.

%package base
Summary: Database front-end for OpenOffice
Group: Applications/Productivity
Requires: postgresql-jdbc
%if 0%{?rhel} && 0%{?rhel} < 7
Requires:  hsqldb
%endif
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-base-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-base%{?_isa} = 1:3.3.0, broffice.org-base%{?_isa} = 1:3.3.0
%endif

%description base
GUI database front-end for OpenOffice. Allows creation and management of 
databases through a GUI.

%package report-builder
Summary: Create database reports from OpenOffice
Group: Applications/Productivity
Requires: pentaho-reporting-flow-engine
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-base = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-report-builder%{?_isa} = 1:3.3.0
%endif

%description report-builder
Creates database reports from OpenOffice databases. The report builder can
define group and page headers as well as group, page footers and calculation
fields to accomplish complex database reports.

%package bsh
Summary: BeanShell support for OpenOffice
Group: Development/Libraries
Requires: bsh
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-bsh%{?_isa} = 1:3.3.0
%endif

%description bsh
Support BeanShell scripts in OpenOffice.

%package rhino
Summary: JavaScript support for OpenOffice
Group: Development/Libraries
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-rhino%{?_isa} = 1:3.3.0
%endif

%description rhino
Support JavaScript scripts in OpenOffice.

%package wiki-publisher
Summary: Create Wiki articles on MediaWiki servers with OpenOffice
Group: Applications/Productivity
%if 0%{?rhel} && 0%{?rhel} < 7
Requires: jakarta-commons-codec, jakarta-commons-httpclient
Requires: jakarta-commons-lang, jakarta-commons-logging
%else
Requires: apache-commons-codec, jakarta-commons-httpclient
Requires: apache-commons-lang, apache-commons-logging
%endif
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-wiki-publisher%{?_isa} = 1:3.3.0
%endif

%description wiki-publisher
The Wiki Publisher enables you to create Wiki articles on MediaWiki servers
without having to know the syntax of the MediaWiki markup language. Publish
your new and existing documents transparently with writer to a wiki page.

%package nlpsolver
Summary: Non-linear solver engine for OpenOffice Calc
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-calc = %{epoch}:%{version}-%{release}

%description nlpsolver
A non-linear solver engine for Calc as an alternative to the default linear
programming model when more complex, nonlinear programming is required.

%package ogltrans
Summary: 3D OpenGL slide transitions for OpenOffice
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-ogltrans%{?_isa} = 1:3.3.0
%endif

%description ogltrans
OpenGL Transitions enable 3D slide transitions to be used in OpenOffice.
Requires good quality 3D support for your graphics card for best experience.

%package presentation-minimizer
Summary: Shrink OpenOffice presentations
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-impress = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-presentation-minimizer%{?_isa} = 1:3.3.0
%endif

%description presentation-minimizer
The Presentation Minimizer is used to reduce the file size of the current
presentation. Images will be compressed, and data that is no longer needed will
be removed.

%package pdfimport
Summary: PDF Importer for OpenOffice Draw
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-draw = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-pdfimport%{?_isa} = 1:3.3.0
%endif

%description pdfimport
The PDF Importer imports PDF into drawing documents to preserve layout
and enable basic editing of PDF documents.

%package %{fontname}-fonts
Summary: OpenOffice dingbats font
Group: User Interface/X
Requires: fontpackages-filesystem
BuildArch: noarch
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-fonts = 1:3.3.0
Provides: openoffice.org-opensymbol-fonts = 1:3.3.0
%endif

%description %{fontname}-fonts
A dingbats font, OpenSymbol, suitable for use by OpenOffice for bullets and
mathematical symbols. 

%package writer
Summary: OpenOffice Word Processor Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-writer-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-writer%{?_isa} = 1:3.3.0, broffice.org-writer%{?_isa} = 1:3.3.0
%endif

%description writer
The OpenOffice Word Processor application.

%package emailmerge
Summary: Email mail-merge component for OpenOffice 
Group: Applications/Productivity
Requires: %{name}-writer = %{epoch}:%{version}-%{release}
Requires: %{name}-pyuno = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-emailmerge%{?_isa} = 1:3.3.0
%endif

%description emailmerge
Enables the OpenOffice writer module to mail-merge to email.

%package calc
Summary: OpenOffice Spreadsheet Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-calc-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-calc%{?_isa} = 1:3.3.0, broffice.org-calc%{?_isa} = 1:3.3.0
%endif

%description calc
The OpenOffice Spreadsheet application.

%package draw
Summary: OpenOffice Drawing Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-pdfimport = %{epoch}:%{version}-%{release}
Requires: %{name}-graphicfilter = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-draw-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-draw%{?_isa} = 1:3.3.0, broffice.org-draw%{?_isa} = 1:3.3.0
%endif

%description draw
The OpenOffice Drawing Application.

%package impress
Summary: OpenOffice Presentation Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-presenter-screen < 2:4.0.0.0-1.beta1
Provides: %{name}-presenter-screen%{?_isa} = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-impress-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-impress%{?_isa} = 1:3.3.0, broffice.org-impress%{?_isa} = 1:3.3.0
Provides: openoffice.org-presenter-screen%{?_isa} = 1:3.3.0
%endif

%description impress
The OpenOffice Presentation Application.

%package math
Summary: OpenOffice Equation Editor Application
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-math-core%{?_isa} = 1:3.3.0
Provides: openoffice.org-math%{?_isa} = 1:3.3.0, broffice.org-math%{?_isa} = 1:3.3.0
%endif

%description math 
The OpenOffice Equation Editor Application.

%package graphicfilter
Summary: OpenOffice Extra Graphic filters
Group: Applications/Productivity
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-graphicfilter%{?_isa} = 1:3.3.0
%endif

%description graphicfilter
The graphicfilter module for OpenOffice provides graphic filters, e.g. svg and
flash filters.

%package xsltfilter
Summary: Optional xsltfilter module for OpenOffice
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-xsltfilter%{?_isa} = 1:3.3.0
%endif

%description xsltfilter
The xsltfilter module for OpenOffice, provides additional docbook and
xhtml export transforms. Install this to enable docbook export.

%package javafilter
Summary: Optional javafilter module for OpenOffice
Group: Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-javafilter%{?_isa} = 1:3.3.0
%endif

%description javafilter
The javafilter module for OpenOffice, provides additional AportisDoc,
Pocket Excel and Pocket Word import filters.

%post javafilter
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun javafilter
update-desktop-database %{_datadir}/applications &> /dev/null || :

%if 0%{?fedora} || 0%{?rhel} >= 7
%package postgresql
Summary: PostgreSQL connector for OpenOffice
Group: Applications/Productivity
Requires: %{name}-base = %{epoch}:%{version}-%{release}
Requires: postgresql-libs

%description postgresql
A PostgreSQL connector for the database front-end for OpenOffice. Allows
creation and management of PostgreSQL databases through a GUI.
%endif

%package ure
Summary: UNO Runtime Environment
Group: Development/Libraries
Requires: unzip, jre >= 1.5.0
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-ure%{?_isa} = 1:3.3.0
%endif

%description ure
UNO is the component model of OpenOffice. UNO offers interoperability between
programming languages, other components models and hardware architectures,
either in process or over process boundaries, in the Intranet as well as in the
Internet. UNO components may be implemented in and accessed from any
programming language for which a UNO implementation (AKA language binding) and
an appropriate bridge or adapter exists

%package sdk
Summary: Software Development Kit for OpenOffice
Group: Development/Libraries
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
Requires: unzip, java-devel
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-sdk%{?_isa} = 1:3.3.0, openoffice.org-devel%{?_isa} = 1:3.3.0
%endif

%description sdk
The OpenOffice SDK is an add-on for the OpenOffice office suite. It provides
the necessary tools for programming using the OpenOffice APIs and for creating
extensions (UNO components) for OpenOffice.  To set the build environment for
building against the sdk use %{sdkinstdir}/setsdkenv_unix.sh.

%package sdk-doc
Summary: Software Development Kit documentation for OpenOffice
Group: Documentation
Requires: %{name}-sdk = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-sdk-doc%{?_isa} = 1:3.3.0
%endif

%description sdk-doc
This provides documentation for programming using the OpenOffice APIs
and examples of creating extensions (UNO components) for OpenOffice.

%package headless
Summary: OpenOffice Headless plug-in
Group: Development/Libraries
Requires: %{name}-ure = %{epoch}:%{version}-%{release}
Requires: %{name}-core = %{epoch}:%{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 7
Provides: openoffice.org-headless%{?_isa} = 1:3.3.0
%endif

%description headless
A plug-in for OpenOffice that enables it to function without an X server. 
It implements the -headless command line option and allows OpenOffice to be
used as a backend server for e.g. document conversion.

%if 0%{?fedora}
%package kde
Summary: OpenOffice KDE integration plug-in
Group:   Applications/Productivity
Requires: %{name}-core = %{epoch}:%{version}-%{release}

%description kde
A plug-in for OpenOffice that enables integration into the KDE desktop environment.
%endif

%if 0%{?_enable_debug_packages}

%define debug_package %{nil}
%global __debug_package 1

%package debuginfo
Summary: Debug information for package %{name}
Group: Development/Debug
AutoReqProv: 0
Requires: openoffice-core = %{epoch}:%{version}-%{release}
Requires: openoffice-gdb-debug-support = %{epoch}:%{version}-%{release}

%description debuginfo
This package provides debug information for package %{name}.
Debug information is useful when developing applications that use this
package or when debugging this package.

%files debuginfo -f debugfiles.list

%package gdb-debug-support
Summary: Additional support for debugging with gdb
Group: Development/Debug
Requires: gdb
AutoReqProv: 0

%description gdb-debug-support
This package provides gdb pretty printers for package %{name}.

%files gdb-debug-support
%{_datadir}/gdb/auto-load%{baseinstdir}
%{_datadir}/openoffice/gdb

%endif

%define _langpack_common() \
%{baseinstdir}/program/resource/*%{1}.res  \
%{baseinstdir}/share/config/soffice.cfg/modules/*/ui/res/%{1} \
%{baseinstdir}/share/config/soffice.cfg/*/ui/res/%{1} \
%{baseinstdir}/share/template/%{1} \
%{baseinstdir}/share/registry/Langpack-%{1}.xcd \
%{baseinstdir}/share/registry/res/registry_%{1}.xcd \
%{baseinstdir}/share/registry/res/fcfg_langpack_%{1}.xcd \
%{nil}

# Defines a language pack subpackage.
#
# It's necessary to define language code (-l) and language name (-n).
# Additionally, it's possible
# * to require autocorr, hunspell, hyphen or mythes package or font for
#   given language,
# * to provide openoffice-langpack-loc package, where loc is glibc
#   locale--this is necessary for yum to pick it automatically,
# * to require other, unrelated, packages,
# * to specify file serving as file list.
# For these, lower case character argument takes an argument specifying
# language, upper case character argument uses language from -l.
#
# All remaining arguments are considered to be files and added to the file
# list.
#
# Aa:  autocorr dependency
# c:   additional config file (just the name stem)
# E    the package does not contain any files (i.e., has empty filelist)
# Ff:  font language dependency
# Hh:  hunspell dependency
# i:   additional language added to this package
# L:   language code for files
# l:   language code, e.g., cs
# Mm:  mythes dependency
# n:   language name, e.g., Czech
# p:   Provides: of openoffice-langpack
# r:   comma-separated list of additional requires
# S:s: script classification (cjk, ctl). -S is only a marker, as it does
#      not add any .xcd into the package (the file does not exist for at
#      least one CTL-using locale, si)
# T    has help files
# Xx:  has autotext definitions
# Yy:  hyphen dependency
#
# Example:
# openoffice-langpack-cs: langpack for Czech lang. requiring hyphen-cs,
# autocorr-cs, mythes-cs-CZ and suitable font:
# %%langpack -l cs -n Czech -H -A -m cs-CZ
#  b de g  jk   o q  tuvw  z BCD  G IJK  NOPQR  UVW  Z0123456789
%define langpack(Aa:c:EFf:Hh:iL:l:Mm:n:p:r:S:s:TXx:Yy:) \
%define project OpenOffice \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname langpack-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary: %{langname} language pack for %{project} \
Group: Applications/Productivity \
Requires: %{name}-core = %{epoch}:%{version}-%{release} \
%{-a:Requires: autocorr-%{-a*}}%{!-a:%{-A:Requires: autocorr-%{lang}}} \
%{-f:Requires: font(:lang=%{-f*})}%{!-f:%{-F:Requires: font(:lang=%{lang})}} \
%{-h:Requires: hunspell-%{-h*}}%{!-h:%{-H:Requires: hunspell-%{lang}}} \
%{-m:Requires: mythes-%{-m*}}%{!-m:%{-M:Requires: mythes-%{lang}}} \
%{-y:Requires: hyphen-%{-y*}}%{!-y:%{-Y:Requires: hyphen-%{lang}}} \
%{-r:Requires: %{-r*}} \
%{-p:Provides: %{name}-langpack-%{-p*}} \
\
%description %{pkgname} \
Provides additional %{langname} translations and resources for %{project}. \
\
%files %{pkgname} \
%{!-E: \
%define _langpack_lang %{-L:%{-L*}}%{!-L:%{-l*}} \
%define autotextdir %{baseinstdir}/share/autotext \
%{expand:%%_langpack_common %{_langpack_lang}} \
%{-x:%{autotextdir}/%{-x*}}%{!-x:%{-X:%{autotextdir}/%{_langpack_lang}}} \
%{-c:%{baseinstdir}/share/registry/%{-c*}.xcd} \
%{-s:%{baseinstdir}/share/registry/%{-s*}_%{_langpack_lang}.xcd} \
%{-T: \
%docdir %{baseinstdir}/help/%{_langpack_lang} \
%{baseinstdir}/help/%{_langpack_lang} \
} \
%{-i:%{expand:%%_langpack_common %{-i*}}} \
} \
%{nil}

# Defines an auto-correction subpackage.
#
# i: add autocorrections from additional language
# l: language code
# n: language name
# L  the filename does not contain country code
#
# All remaining arguments are considered to be files and added to the file
# list.
%define autocorr(i:Ll:n:) \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define pkgname autocorr-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package -n %{pkgname} \
Summary: %{langname} auto-correction rules \
Group: Applications/Text \
BuildArch: noarch \
\
%description -n %{pkgname} \
Rules for auto-correcting common %{langname} typing errors. \
\
%files -n %{pkgname} \
%doc solver/unxlng*/bin/ure/LICENSE \
%dir %{_datadir}/autocorr \
%{-L:%{_datadir}/autocorr/acor_%{lang}.dat} \
%{!-L:%{_datadir}/autocorr/acor_%{lang}-*.dat} \
%{-i:%{_datadir}/autocorr/acor_%{-i*}-*.dat} \
%{nil}

%if %{with langpacks}

%langpack -l af -n Afrikaans -F -H -Y -A
%langpack -l ar -n Arabic -F -H -s ctl
%langpack -l as -n Assamese -F -H -Y
%langpack -l bg -n Bulgarian -F -H -Y -M -A -T -X
%langpack -l bn -n Bengali -F -H -Y -T
%langpack -l ca -n Catalan -F -H -Y -M -T
%langpack -l cs -n Czech -F -H -Y -M -A -T -X
%langpack -l cy -n Welsh -F -H -Y
%langpack -l da -n Danish -F -H -Y -M -A -T -X
%langpack -l de -n German -F -H -Y -M -A -T -X
%langpack -l dz -n Dzongkha -F -s ctl -T
%langpack -l el -n Greek -F -H -Y -M -T
%langpack -l en -n English -F -H -Y -M -A -E
%langpack -l es -n Spanish -F -H -Y -M -A -T -X
%langpack -l et -n Estonian -F -H -Y -T
%langpack -l eu -n Basque -F -H -Y -A -T -X
%if 0%{?fedora} || 0%{?rhel} >= 7
%langpack -l fa -n Farsi -A -H -Y -s ctl
%endif
%if 0%{?rhel} && 0%{?rhel} < 7
%langpack -l fi -n Finnish -F -A -T
%else
%langpack -l fi -n Finnish -F -r openoffice-voikko -A -T
%endif
%langpack -l fr -n French -F -H -Y -M -A -T -X
%langpack -l ga -n Irish -F -H -Y -M -A
%langpack -l gl -n Galician -F -H -Y -T
%langpack -l gu -n Gujarati -F -H -Y -s ctl
%langpack -l he -n Hebrew -F -H -s ctl
%langpack -l hi -n Hindi -F -H -Y -s ctl -T
%langpack -l hr -n Croatian -F -H -Y -A
%langpack -l hu -n Hungarian -F -H -Y -M -A -T -X
%langpack -l it -n Italian -F -H -Y -M -A -T -X
%langpack -l ja -n Japanese -F -A -s cjk -T -X
%if 0%{?fedora} || 0%{?rhel} >= 7
%langpack -l kk -n Kazakh -F -H
%endif
%langpack -l kn -n Kannada -F -H -Y
%langpack -l ko -n Korean -F -H -A -s cjk -T -c korea -X
%langpack -l lt -n Lithuanian -F -H -Y -A
%if 0%{?fedora} || 0%{?rhel} >= 7
%langpack -l lv -n Latvian -F -H -Y -M
%endif
%langpack -l mai -n Maithili -F
%if 0%{?rhel} && 0%{?rhel} < 7
%langpack -l ms -n Malay -F -H
%endif
%langpack -l ml -n Malayalam -F -H -Y
%langpack -l mr -n Marathi -F -H -Y
%langpack -l nb -n Bokmal -F -H -Y -M -T
%langpack -l nl -n Dutch -F -H -Y -M -A -T -X
%langpack -l nn -n Nynorsk -F -H -Y -M -T
%define langpack_lang Southern Ndebele
%langpack -l nr -n %{langpack_lang} -F -H
%define langpack_lang Northern Sotho
%langpack -l nso -n %{langpack_lang} -F -H
%langpack -l or -n Oriya -F -H -Y -s ctl
%langpack -l pa -n Punjabi -F -H -Y -s ctl -L pa-IN
%langpack -l pl -n Polish -F -H -Y -M -A -T -X
%define langpack_lang Brazilian Portuguese
%langpack -l pt-BR -n %{langpack_lang} -f pt -h pt -y pt -m pt -a pt -p pt_BR -T -X
%langpack -l pt-PT -n Portuguese -f pt -h pt -y pt -m pt -a pt -p pt_PT -T -L pt -x pt
%langpack -l ro -n Romanian -F -H -Y -M -T
%langpack -l ru -n Russian -F -H -Y -M -A -T -X
%if 0%{?fedora} || 0%{?rhel} >= 7
%langpack -l si -n Sinhalese -F -H -S ctl -T
%endif
%langpack -l sk -n Slovak -F -H -Y -M -A -T -X
%langpack -l sl -n Slovenian -F -H -Y -M -A -T -X
#rhbz#452379 clump serbian translations together
%langpack -l sr -n Serbian -F -H -Y -A -i sh
%langpack -l ss -n Swati -F -H
%define langpack_lang Southern Sotho
%langpack -l st -n %{langpack_lang} -F -H
%langpack -l sv -n Swedish -F -H -Y -M -A -T -X
%langpack -l ta -n Tamil -F -H -Y -s ctl
%langpack -l te -n Telugu -F -H -Y
%langpack -l th -n Thai -F -H -s ctl -c ctlseqcheck_th
%langpack -l tn -n Tswana -F -H
%langpack -l tr -n Turkish -F -A -T -X
%langpack -l ts -n Tsonga -F -H
%langpack -l uk -n Ukrainian -F -H -Y -M -T
%if 0%{?rhel} && 0%{?rhel} < 7
%langpack -l ur -n Urdu -F -H
%endif
%langpack -l ve -n Venda -F -H
%langpack -l xh -n Xhosa -F -H
%define langpack_lang Simplified Chinese
%langpack -l zh-Hans -n %{langpack_lang} -f zh-cn -a zh -p zh_CN -s cjk -T -L zh-CN -x zh-CN
%define langpack_lang Traditional Chinese
%langpack -l zh-Hant -n %{langpack_lang} -f zh-tw -a zh -p zh_TW -s cjk -T -L zh-TW -x zh-TW
%langpack -l zu -n Zulu -F -H -Y
%undefine langpack_lang

%endif

%autocorr -l en -n English

%if %{with langpacks}

%autocorr -l af -n Afrikaans
%autocorr -l bg -n Bulgarian
%autocorr -l cs -n Czech
%autocorr -l da -n Danish
%autocorr -l de -n German
%autocorr -l es -n Spanish
%autocorr -l eu -n Basque -L
%autocorr -l fa -n Farsi
%autocorr -l fi -n Finnish
%autocorr -l fr -n French
%autocorr -l ga -n Irish
%autocorr -l hr -n Croatian
%autocorr -l hu -n Hungarian
%autocorr -l it -n Italian
%autocorr -l ja -n Japanese
%autocorr -l ko -n Korean
%autocorr -l lb -n Luxembourgish
%autocorr -l lt -n Lithuanian
%autocorr -l mn -n Mongolian
%autocorr -l nl -n Dutch
%autocorr -l pl -n Polish
%autocorr -l pt -n Portuguese
%autocorr -l ru -n Russian
%autocorr -l sk -n Slovak
%autocorr -l sl -n Slovenian
#rhbz#452379 clump serbian autocorrections together
%autocorr -l sr -n Serbian -i sh
%autocorr -l sv -n Swedish
%autocorr -l tr -n Turkish
%autocorr -l vi -n Vietnamese
%autocorr -l zh -n Chinese

%endif

%define make_autocorr_aliases(l:) \
%{?-l: \
for lang in %{*}; do \
    ln -sf acor_%{-l*}.dat acor_$lang.dat \
done \
} \
%{!?-l:%{error:-l must be present}}

%prep
#%setup -q -n %{name}-%{version}%{?libo_prerelease} -b 1 -b 2
%setup -q 

%build
echo build start time is `date`, diskspace: `df -h . | tail -n 1`
#don't build localized helps which aren't translated
POORHELPS=`ls -d translations/source/*/helpcontent2 translations/source/*|cut -f 3 -d /|sort|uniq -u|xargs`
#don't build localized helps which are poorly translated
POORHELPS="$POORHELPS `grep 'msgstr .Working with Documents' translations/source/*/helpcontent2/source/text/swriter/guide.po| cut -f 3 -d / | xargs`"
# path to external tarballs
EXTSRCDIR=`dirname %{SOURCE0}`

%if 0%{?fedora}
# KDE bits
export QT4DIR=%{_qt4_prefix}
export KDE4DIR=%{_kde4_prefix}
export PATH=$QT4DIR/bin:$PATH
%endif

#use the RPM_OPT_FLAGS but remove the OOo overridden ones
for i in $RPM_OPT_FLAGS; do
        case "$i" in
                -pipe|-Wall|-g|-fexceptions) continue;;
        esac
        ARCH_FLAGS="$ARCH_FLAGS $i"
done
export ARCH_FLAGS
export CFLAGS=$ARCH_FLAGS
export CXXFLAGS=$ARCH_FLAGS

%if 0%{?rhel}
%if 0%{?rhel} < 7
%define distrooptions --disable-graphite --without-system-mythes --without-system-mdds --without-junit --without-system-redland --disable-ext-mysql-connector --without-system-libexttextcat --without-system-libcdr --without-system-libwps --without-system-libwpd --without-system-libwpg --without-system-libcmis --without-system-clucene --without-system-libvisio --without-system-lcms2 --without-system-libmspub --without-system-orcus --without-system-liblangtag --without-system-boost --enable-gstreamer-0-10 --disable-gstreamer --disable-postgresql-sdbc --with-servlet-api-jar=/usr/share/java/apache-tomcat-apis/tomcat-servlet2.5-api.jar --enable-python=system --with-system-hsqldb
%else
%define distrooptions --without-system-hsqldb --disable-gstreamer-0-10 --enable-gstreamer --with-system-mythes --enable-python=system --with-servlet-api-jar=/usr/share/java/tomcat-servlet-api.jar
%endif
%else
%define distrooptions --without-system-hsqldb --enable-kde4 --disable-gstreamer-0-10 --enable-gstreamer --with-system-mythes --with-servlet-api-jar=/usr/share/java/tomcat-servlet-api.jar
%endif

%if ! 0%{libo_python3}
export PYTHON=%{_bindir}/python
export PYTHON_CFLAGS=`pkg-config --cflags python`
export PYTHON_LIBS=`pkg-config --libs python`
%endif

%aclocal -I m4
autoconf
# avoid running autogen.sh on make
touch autogen.lastrun
%configure \
 %vendoroption %{?_smp_flags:--with-parallelism=%{_smp_flags}} \
 --with-build-version="%{version}-%{release}" --with-unix-wrapper=%{name} \
 --enable-release-build --disable-epm --disable-mathmldtd \
 --disable-gnome-vfs --enable-gio --enable-symbols --enable-lockdown \
 --enable-evolution2 --enable-dbus --enable-opengl --enable-vba \
 --enable-ext-presenter-minimizer --enable-ext-nlpsolver \
 --enable-ext-wiki-publisher --enable-ext-report-builder \
 --enable-scripting-beanshell --enable-scripting-javascript \
 --with-system-jars --with-vba-package-format="builtin" \
 --with-system-libs --with-system-headers --with-system-mozilla \
 --without-system-npapi-headers --with-system-dicts \
 --with-external-dict-dir=/usr/share/myspell \
 --without-myspell-dicts --without-fonts --without-ppds --without-afms \
 %{?with_lang} --with-poor-help-localizations="$POORHELPS" \
 --with-external-tar="$EXTSRCDIR" --with-java-target-version=1.5 \
 %{distrooptions} \
 --disable-fetch-external

if ! make VERBOSE=true; then
    # TODO Do we still need this? I think parallel build is reliable
    # enough these days...
    make VERBOSE=true PARALLELISM=1
fi

#generate the icons and mime type stuff
export DESTDIR=../../../output
export KDEMAINDIR=/usr
export GNOMEDIR=/usr
export GNOME_MIME_THEME=hicolor
# TODO use empty variables? Should make the renaming hacks in %%install
# unnecessary.
. ./bin/get_config_variables PRODUCTVERSIONSHORT PRODUCTVERSION
cd sysui/unxlng*/misc/openoffice
./create_tree.sh

echo build end time is `date`, diskspace: `df -h . | tail -n 1`


%install
# TODO investigate use of make distro-pack-install
. ./bin/get_config_variables `sed -n -e '/^export/s/^export \([A-Z0-9_]\+\).*/\1/p' config_host.mk`
#figure out the icon version
export `grep "^PRODUCTVERSIONSHORT =" solenv/inc/productversion.mk | sed -e "s/ //g"`
export `grep "PRODUCTVERSION[ ]*=[ ]*" solenv/inc/productversion.mk | sed -e "s/ //g"`
#install
cd instsetoo_native/util
#direct install
mkdir -p $RPM_BUILD_ROOT/%{instdir}
export PKGFORMAT=installed
#don't duplicate english helpcontent about the place
unset DEFAULT_TO_ENGLISH_FOR_PACKING
if dmake openoffice_en-US; then
    ok=true
    break
else
    echo - ---dump log start---
    cat ../unx*.pro/OpenOffice/installed/logging/en-US/log_*_en-US.log
    echo - ---dump log end---
    ok=false
fi
if [ $ok == "false" ]; then
    exit 1
fi
mkdir -p $RPM_BUILD_ROOT/%{baseinstdir}
mv ../unxlng*.pro/OpenOffice/installed/install/en-US/* $RPM_BUILD_ROOT/%{baseinstdir}
chmod -R +w $RPM_BUILD_ROOT/%{baseinstdir}
# The installer currently sets UserInstallation to
# $ORIGIN/../openoffice/4, which is of course total nonsense. Because I
# have no inclination to crawl through mountains of perl code to figure out
# where it comes from, I am just going to replace it by a sensible
# value here.
sed -i -e '/UserInstallation/s@\$ORIGIN/..@$SYSUSERCONFIG@' $RPM_BUILD_ROOT/%{baseinstdir}/program/bootstraprc
%if %{with langpacks}
dmake ooolanguagepack
rm -rf ../unxlng*.pro/OpenOffice_languagepack/installed/install/log
for langpack in ../unxlng*.pro/OpenOffice_languagepack/installed/install/*; do
  cp -rp $langpack/* $RPM_BUILD_ROOT/%{baseinstdir}
  rm -rf $langpack
done
%endif
export WITH_LANG_LIST="en-US"
dmake sdkoo
mv ../unxlng*.pro/OpenOffice_SDK/installed/install/en-US/sdk $RPM_BUILD_ROOT/%{sdkinstdir}
cd ../../

#configure sdk
pushd $RPM_BUILD_ROOT/%{sdkinstdir}
    for file in setsdkenv_unix.csh setsdkenv_unix.sh ; do
        sed -e "s,@OO_SDK_NAME@,sdk," \
            -e "s,@OO_SDK_HOME@,%{sdkinstdir}," \
            -e "s,@OFFICE_HOME@,%{baseinstdir}," \
            -e "s,@OO_SDK_URE_HOME@,%{ureinstdir}," \
            -e "s,@OO_SDK_MAKE_HOME@,/usr/bin," \
            -e "s,@OO_SDK_ZIP_HOME@,/usr/bin," \
            -e "s,@OO_SDK_CPP_HOME@,/usr/bin," \
            -e "s,@OO_SDK_CC_55_OR_HIGHER@,," \
            -e "s,@OO_SDK_JAVA_HOME@,$JAVA_HOME," \
            -e "s,@OO_SDK_OUTPUT_DIR@,\$HOME," \
            -e "s,@SDK_AUTO_DEPLOYMENT@,NO," \
            $file.in > $file
        chmod 755 $file
    done
    # we don't want to install the input files
    rm -f setsdkenv_unix.csh.in setsdkenv_unix.sh.in
#fix permissions
    find examples -type f -exec chmod -x {} \;
popd

#ensure a template dir for each lang
pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/template
for I in %{langpack_langs}; do
    mkdir -p $I
done
popd

#Set some aliases to canonical autocorrect language files for locales with matching languages
pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/autocorr

%make_autocorr_aliases -l en-GB en-AG en-AU en-BS en-BW en-BZ en-CA en-DK en-GH en-HK en-IE en-IN en-JM en-NG en-NZ en-SG en-TT
%make_autocorr_aliases -l en-US en-PH
#en-ZA exists and has a good autocorrect file with two or three extras that make sense for 
#neighbouring english speaking territories
%make_autocorr_aliases -l en-ZA en-NA en-ZW
%if %{with langpacks}
%make_autocorr_aliases -l af-ZA af-NA
%make_autocorr_aliases -l de-DE de-AT de-BE de-CH de-LI de-LU
%make_autocorr_aliases -l es-ES es-AR es-BO es-CL es-CO es-CR es-CU es-DO es-EC es-GT es-HN es-MX es-NI es-PA es-PE es-PR es-PY es-SV es-US es-UY es-VE
%make_autocorr_aliases -l fr-FR fr-BE fr-CA fr-CH fr-LU fr-MC
%make_autocorr_aliases -l it-IT it-CH
%make_autocorr_aliases -l nl-NL nl-AW
%make_autocorr_aliases -l sv-SE sv-FI
%else
rm -f acor_[a-df-z]*.dat acor_e[su]*.dat
%endif
popd
#rhbz#484055 make these shared across multiple applications
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv -f $RPM_BUILD_ROOT/%{baseinstdir}/share/autocorr $RPM_BUILD_ROOT/%{_datadir}/autocorr
chmod 755 $RPM_BUILD_ROOT/%{_datadir}/autocorr

#remove it in case we didn't build with gcj
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/classes/sandbox.jar

#remove dummy .dat files
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/root?.dat

#set standard permissions for rpmlint
find $RPM_BUILD_ROOT/%{baseinstdir} -exec chmod +w {} \;
find $RPM_BUILD_ROOT/%{baseinstdir} -type d -exec chmod 0755 {} \;

# move python bits into site-packages
mkdir -p $RPM_BUILD_ROOT/%{libo_python_sitearch}
pushd $RPM_BUILD_ROOT/%{libo_python_sitearch}
echo "import sys, os" > uno.py
echo "sys.path.append('%{baseinstdir}/program')" >> uno.py
echo "os.putenv('URE_BOOTSTRAP', 'vnd.sun.star.pathname:%{baseinstdir}/program/fundamentalrc')" >> uno.py
cat $RPM_BUILD_ROOT/%{baseinstdir}/program/uno.py >> uno.py
rm -f $RPM_BUILD_ROOT/%{baseinstdir}/program/uno.py*
mv -f $RPM_BUILD_ROOT/%{baseinstdir}/program/unohelper.py* .
popd

# rhbz#477435 package opensymbol separately
pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/fonts/truetype
install -d -m 0755 %{buildroot}%{_fontdir}
install -p -m 0644 *.ttf %{buildroot}%{_fontdir}
popd
rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/share/fonts

#ensure that no sneaky un-prelinkable, un-fpic or non executable shared libs 
#have snuck through
pic=0
executable=0
for foo in `find $RPM_BUILD_ROOT/%{instdir} -name "*" -exec file {} \;| grep ": ELF" | cut -d: -f 1` ; do
    chmod +wx $foo
    ls -asl $foo
    result=`readelf -d $foo | grep TEXTREL` || true
    if [ "$result" != "" ]; then
        echo "TEXTREL Warning: $foo is b0rked (-fpic missing)"
        pic=1
    fi
    result=`readelf -l $foo | grep GNU_STACK | grep RWE` || true
    if [ "$result" != "" ]; then
        echo "GNU_STACK Warning: $foo is b0rked (-noexecstack missing)"
        executable=1
    fi
done
if [ $pic == 1 ]; then false; fi
if [ $executable == 1 ]; then false; fi

#make up some /usr/bin scripts
mkdir -p $RPM_BUILD_ROOT/%{_bindir}

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooffice
echo exec openoffice \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooffice
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooffice

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc
echo exec openoffice --view \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooviewdoc

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oowriter
echo exec openoffice --writer \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oowriter
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oowriter

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oocalc
echo exec openoffice --calc \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oocalc
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oocalc

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/ooimpress
echo exec openoffice --impress \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/ooimpress
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/ooimpress

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oodraw
echo exec openoffice --draw \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oodraw
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oodraw

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oomath
echo exec openoffice --math \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oomath
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oomath

echo \#\!/bin/sh > $RPM_BUILD_ROOT/%{_bindir}/oobase
echo exec openoffice --base \"\$@\" >> $RPM_BUILD_ROOT/%{_bindir}/oobase
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/oobase

cp -f %{SOURCE4} $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/LAUNCHER/unopkg/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
sed -i -e "s/BRAND/openoffice/g" $RPM_BUILD_ROOT/%{_bindir}/unopkg
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/unopkg

cp -f %{SOURCE4} $RPM_BUILD_ROOT/%{_bindir}/openoffice
sed -i -e "s/LAUNCHER/soffice/g" $RPM_BUILD_ROOT/%{_bindir}/openoffice
sed -i -e "s/BRAND/openoffice/g" $RPM_BUILD_ROOT/%{_bindir}/openoffice
chmod a+x $RPM_BUILD_ROOT/%{_bindir}/openoffice

pushd $RPM_BUILD_ROOT/%{_bindir}
# rhbz#499474 provide a /usr/bin/soffice for .recently-used.xbel
ln -s %{baseinstdir}/program/soffice soffice
# rhbz#499474 provide a /usr/bin/openoffice.org for backwards compat
ln -s openoffice openoffice.org
popd

pushd $RPM_BUILD_ROOT/%{baseinstdir}/share/xdg/
chmod u+w *.desktop
rm -rf printeradmin.desktop
ICONVERSION=`echo $PRODUCTVERSION | sed -e 's/\.//'`
for file in *.desktop; do
    # rhbz#156677 remove the version from Name=
    # rhbz#156067 don't version the icons
    sed -i -e "s/ *$PRODUCTVERSION//g" \
        -e "s/$ICONVERSION//g" \
        -e "s/$PRODUCTVERSIONSHORT//g" \
        $file
    # add X-GIO-NoFuse so we get url:// instead of file://~.gvfs/
    echo X-GIO-NoFuse=true >> $file
done
for app in base calc draw impress math writer; do
    echo "StartupNotify=true" >> $app.desktop
    echo "TryExec=oo$app" >> $app.desktop
done
# rhbz#156677# / rhbz#186515#
echo "NoDisplay=true" >> startcenter.desktop
# rhbz#491159 temporarily remove NoDisplay=true from qstart.desktop
sed -i -e "/NoDisplay=true/d" qstart.desktop
# relocate the .desktop and icon files
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
for app in base calc draw impress javafilter math startcenter writer xsltfilter; do
    desktop-file-validate $app.desktop
    cp -p $app.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/openoffice-$app.desktop
done
popd

pushd sysui/output/usr/share/
#get rid of the gnome icons and other unneeded files
rm -rf icons/gnome applications application-registry

#relocate the rest of them
# rhbz#901346 512x512 icons are not used by anything
for icon in `find icons -path '*/512x512' -prune -o -type f -print`; do
    mkdir -p $RPM_BUILD_ROOT/%{_datadir}/`dirname $icon`
    cp -p $icon $RPM_BUILD_ROOT/%{_datadir}/`echo $icon | sed -e s@office$ICONVERSION@office@ | sed -e s@office$PRODUCTVERSION@office@`
done
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mime-info
cp -p mime-info/openoffice$PRODUCTVERSION.keys $RPM_BUILD_ROOT/%{_datadir}/mime-info/openoffice.keys
cp -p mime-info/openoffice$PRODUCTVERSION.mime $RPM_BUILD_ROOT/%{_datadir}/mime-info/openoffice.mime
#add our mime-types, e.g. for .oxt extensions
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mime/packages
cp -p mime/packages/openoffice$PRODUCTVERSION.xml $RPM_BUILD_ROOT/%{_datadir}/mime/packages/openoffice.xml
popd

rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/readmes
rm -rf $RPM_BUILD_ROOT/%{baseinstdir}/licenses

mkdir -p $RPM_BUILD_ROOT/%{baseinstdir}/share/psprint/driver
cp -p psprint_config/configuration/ppds/SGENPRT.PS $RPM_BUILD_ROOT/%{baseinstdir}/share/psprint/driver/SGENPRT.PS

# rhbz#452385 to auto have postgres in classpath if subsequently installed
sed -i -e "s#URE_MORE_JAVA_CLASSPATH_URLS.*#& file:///usr/share/java/postgresql-jdbc.jar#" $RPM_BUILD_ROOT/%{baseinstdir}/program/fundamentalrc

export DESTDIR=$RPM_BUILD_ROOT
install-gdb-printers -a %{_datadir}/gdb/auto-load%{baseinstdir} -c -i %{baseinstdir} -p %{_datadir}/openoffice/gdb


#%check
#unset WITH_LANG
## work around flawed accessibility check
#export JFW_PLUGIN_DO_NOT_CHECK_ACCESSIBILITY="1"
#%if 0%{?rhel} && 0%{?rhel} < 7
#timeout 2h make smoketest.subsequentcheck
#%else
#timeout -k 2m 2h make smoketest.subsequentcheck
#%endif

%files

%files core
%dir %{baseinstdir}
%dir %{baseinstdir}/help
%docdir %{baseinstdir}/help/en
%dir %{baseinstdir}/help/en
%{baseinstdir}/help/en/default.css
%{baseinstdir}/help/en/err.html
%{baseinstdir}/help/en/highcontrast1.css
%{baseinstdir}/help/en/highcontrast2.css
%{baseinstdir}/help/en/highcontrastblack.css
%{baseinstdir}/help/en/highcontrastwhite.css
%{baseinstdir}/help/en/sbasic.*
%{baseinstdir}/help/en/schart.*
%{baseinstdir}/help/en/shared.*
%{baseinstdir}/help/idxcaption.xsl
%{baseinstdir}/help/idxcontent.xsl
%{baseinstdir}/help/main_transform.xsl
%{baseinstdir}/presets
%dir %{baseinstdir}/program
%{baseinstdir}/program/addin
%{baseinstdir}/program/basprov.uno.so
%{baseinstdir}/program/cairocanvas.uno.so
%{baseinstdir}/program/canvasfactory.uno.so
%{baseinstdir}/program/cde-open-url
%dir %{baseinstdir}/program/classes
%{baseinstdir}/program/classes/agenda.jar
%{baseinstdir}/program/classes/commonwizards.jar
%{baseinstdir}/program/classes/form.jar
%{baseinstdir}/program/classes/query.jar
%{baseinstdir}/program/classes/officebean.jar
%{baseinstdir}/program/classes/report.jar
%{baseinstdir}/program/classes/ScriptFramework.jar
%{baseinstdir}/program/classes/ScriptProviderForJava.jar
%{baseinstdir}/program/classes/table.jar
%{baseinstdir}/program/classes/unoil.jar
%{baseinstdir}/program/classes/web.jar
%{baseinstdir}/program/classes/XMergeBridge.jar
%{baseinstdir}/program/classes/xmerge.jar
%{baseinstdir}/program/cmdmail.uno.so
%{baseinstdir}/program/libdeployment.so
%{baseinstdir}/program/libdeploymentgui.so
%{baseinstdir}/program/dlgprov.uno.so
%{baseinstdir}/program/expwrap.uno.so
%{baseinstdir}/program/fastsax.uno.so
%{baseinstdir}/program/flat_logo.svg
%{baseinstdir}/program/fpicker.uno.so
%{baseinstdir}/program/fps_office.uno.so
%{baseinstdir}/program/gdbtrace
%{baseinstdir}/program/gengal
%{baseinstdir}/program/gengal.bin
%{baseinstdir}/program/gnome-open-url
%{baseinstdir}/program/gnome-open-url.bin
%{baseinstdir}/program/hatchwindowfactory.uno.so
%{baseinstdir}/program/kde-open-url
%{baseinstdir}/program/i18nsearch.uno.so
%{baseinstdir}/program/ldapbe2.uno.so
%{baseinstdir}/program/libacclo.so
%{baseinstdir}/program/libavmedia*.so
%{baseinstdir}/program/libbasctllo.so
%{baseinstdir}/program/libbiblo.so
%{baseinstdir}/program/libcached1.so
%{baseinstdir}/program/libcanvastoolslo.so
%{baseinstdir}/program/libchart*lo.so
%{baseinstdir}/program/libcollator_data.so
%{baseinstdir}/program/libcppcanvaslo.so
%{baseinstdir}/program/libctllo.so
%{baseinstdir}/program/libcuilo.so
%{baseinstdir}/program/libdbalo.so
%{baseinstdir}/program/libdbaselo.so
%{baseinstdir}/program/libdbaxmllo.so
%{baseinstdir}/program/libdbmmlo.so
%{baseinstdir}/program/libdbpool2.so
%{baseinstdir}/program/libdbtoolslo.so
%{baseinstdir}/program/libdbulo.so
%{baseinstdir}/program/libdeploymentmisclo.so
%{baseinstdir}/program/libdesktop_detectorlo.so
%{baseinstdir}/program/libdict_ja.so
%{baseinstdir}/program/libdict_zh.so
%{baseinstdir}/program/libdrawinglayerlo.so
%{baseinstdir}/program/libeditenglo.so
%{baseinstdir}/program/libembobj.so
%{baseinstdir}/program/libemboleobj.so
%{baseinstdir}/program/libevoab*.so
%{baseinstdir}/program/libevtattlo.so
%{baseinstdir}/program/libegilo.so
%{baseinstdir}/program/libemelo.so
%{baseinstdir}/program/libepblo.so
%{baseinstdir}/program/libepglo.so
%{baseinstdir}/program/libepplo.so
%{baseinstdir}/program/libepslo.so
%{baseinstdir}/program/libeptlo.so
%{baseinstdir}/program/liberalo.so
%{baseinstdir}/program/libetilo.so
%{baseinstdir}/program/libexplo.so
%{baseinstdir}/program/libicdlo.so
%{baseinstdir}/program/libicglo.so
%{baseinstdir}/program/libidxlo.so
%{baseinstdir}/program/libimelo.so
%{baseinstdir}/program/libindex_data.so
%{baseinstdir}/program/libipblo.so
%{baseinstdir}/program/libipdlo.so
%{baseinstdir}/program/libipslo.so
%{baseinstdir}/program/libiptlo.so
%{baseinstdir}/program/libipxlo.so
%{baseinstdir}/program/libiralo.so
%{baseinstdir}/program/libitglo.so
%{baseinstdir}/program/libitilo.so
%{baseinstdir}/program/libofficebean.so
%{baseinstdir}/program/libfilelo.so
%{baseinstdir}/program/libfilterconfiglo.so
%{baseinstdir}/program/libflatlo.so
%{baseinstdir}/program/libfrmlo.so
%{baseinstdir}/program/libguesslanglo.so
%{baseinstdir}/program/libhelplinkerlo.so
%{baseinstdir}/program/libhyphenlo.so
%{baseinstdir}/program/libjdbclo.so
%{baseinstdir}/program/liblnglo.so
%{baseinstdir}/program/libloglo.so
%{baseinstdir}/program/liblocaledata_en.so
%{baseinstdir}/program/liblocaledata_es.so
%{baseinstdir}/program/liblocaledata_euro.so
%{baseinstdir}/program/liblocaledata_others.so
%{baseinstdir}/program/libmcnttype.so
%{baseinstdir}/program/libmorklo.so
%{baseinstdir}/program/libmozbootstrap.so
%{baseinstdir}/program/libmsfilterlo.so
%{baseinstdir}/program/mtfrenderer.uno.so
%{baseinstdir}/program/libmysqllo.so
%{baseinstdir}/program/libodbclo.so
%{baseinstdir}/program/libodbcbaselo.so
%{baseinstdir}/program/liboffacclo.so
%{baseinstdir}/program/libooxlo.so
%{baseinstdir}/program/libpcrlo.so
%{baseinstdir}/program/libpdffilterlo.so
%{baseinstdir}/program/libpllo.so
%{baseinstdir}/program/libprotocolhandlerlo.so
%{baseinstdir}/program/libqstart_gtklo.so
%{baseinstdir}/program/opencentfile.so
%{baseinstdir}/program/openslo.so
%{baseinstdir}/program/libsaxlo.so
%{baseinstdir}/program/libscnlo.so
%{baseinstdir}/program/libscriptframe.so
%{baseinstdir}/program/libsdlo.so
%{baseinstdir}/program/libsdfiltlo.so
%{baseinstdir}/program/libsdbc2.so
%{baseinstdir}/program/libsdbtlo.so
%{baseinstdir}/program/libsddlo.so
%{baseinstdir}/program/libsduilo.so
%{baseinstdir}/program/libspalo.so
%{baseinstdir}/program/libspelllo.so
%{baseinstdir}/program/libsrtrs1.so
%{baseinstdir}/program/libsvgiolo.so
%{baseinstdir}/program/libsvxlo.so
%{baseinstdir}/program/libsvxcorelo.so
%{baseinstdir}/program/libswlo.so
%{baseinstdir}/program/libtextconv_dict.so
%{baseinstdir}/program/libtextconversiondlgslo.so
%{baseinstdir}/program/libtextfdlo.so
%{baseinstdir}/program/libtvhlp1.so
%{baseinstdir}/program/libodfflatxmllo.so
%{baseinstdir}/program/libucbhelper4gcc3.so
%{baseinstdir}/program/libucpchelp1.so
%{baseinstdir}/program/libucpdav1.so
%{baseinstdir}/program/libucpftp1.so
%{baseinstdir}/program/libucphier1.so
%{baseinstdir}/program/libucppkg1.so
%{baseinstdir}/program/libunordflo.so
%{baseinstdir}/program/libunopkgapp.so
%{baseinstdir}/program/libunoxmllo.so
%{baseinstdir}/program/libuuilo.so
%{baseinstdir}/program/libvbahelperlo.so
%{baseinstdir}/program/libvclplug_genlo.so
%{baseinstdir}/program/libvclplug_gtklo.so
%{baseinstdir}/program/libwpftdrawlo.so
%{baseinstdir}/program/libxmlfalo.so
%{baseinstdir}/program/libxmlfdlo.so
%{baseinstdir}/program/libxoflo.so
%{baseinstdir}/program/libxsec_fw.so
%{baseinstdir}/program/libxsec_xmlsec.so
%{baseinstdir}/program/libxsltdlglo.so
%{baseinstdir}/program/libxsltfilterlo.so
%{baseinstdir}/program/libxstor.so
%if 0%{?fedora} || 0%{?rhel} >= 7
# TODO how useful this is in Fedora?
%{baseinstdir}/program/losessioninstall.uno.so
%endif
%{baseinstdir}/program/migrationoo2.uno.so
%{baseinstdir}/program/migrationoo3.uno.so
%{baseinstdir}/program/msforms.uno.so
%{baseinstdir}/program/nsplugin
%{baseinstdir}/program/open-url
%{baseinstdir}/program/types/offapi.rdb
%{baseinstdir}/program/passwordcontainer.uno.so
%{baseinstdir}/program/pagein-common
%{baseinstdir}/program/plugin
%{baseinstdir}/program/pluginapp.bin
%dir %{baseinstdir}/program/resource
%{baseinstdir}/program/resource/avmediaen-US.res
%{baseinstdir}/program/resource/accen-US.res
%{baseinstdir}/program/resource/basctlen-US.res
%{baseinstdir}/program/resource/biben-US.res
%{baseinstdir}/program/resource/chartcontrolleren-US.res
%{baseinstdir}/program/resource/cuien-US.res
%{baseinstdir}/program/resource/dbaen-US.res
%{baseinstdir}/program/resource/dbmmen-US.res
%{baseinstdir}/program/resource/dbuen-US.res
%{baseinstdir}/program/resource/dbwen-US.res
%{baseinstdir}/program/resource/deploymenten-US.res
%{baseinstdir}/program/resource/deploymentguien-US.res
%{baseinstdir}/program/resource/dkten-US.res
%{baseinstdir}/program/resource/editengen-US.res
%{baseinstdir}/program/resource/epsen-US.res
%{baseinstdir}/program/resource/euren-US.res
%{baseinstdir}/program/resource/fps_officeen-US.res
%{baseinstdir}/program/resource/frmen-US.res
%{baseinstdir}/program/resource/fween-US.res
%{baseinstdir}/program/resource/galen-US.res
%{baseinstdir}/program/resource/impen-US.res
%{baseinstdir}/program/resource/ofaen-US.res
%{baseinstdir}/program/resource/pcren-US.res
%{baseinstdir}/program/resource/pdffilteren-US.res
%{baseinstdir}/program/resource/sben-US.res
%{baseinstdir}/program/resource/scnen-US.res
%{baseinstdir}/program/resource/sden-US.res
%{baseinstdir}/program/resource/sfxen-US.res
%{baseinstdir}/program/resource/spaen-US.res
%{baseinstdir}/program/resource/sdbten-US.res
%{baseinstdir}/program/resource/svlen-US.res
%{baseinstdir}/program/resource/svten-US.res
%{baseinstdir}/program/resource/svxen-US.res
%{baseinstdir}/program/resource/swen-US.res
%{baseinstdir}/program/resource/textconversiondlgsen-US.res
%{baseinstdir}/program/resource/tken-US.res
%{baseinstdir}/program/resource/tplen-US.res
%{baseinstdir}/program/resource/uuien-US.res
%{baseinstdir}/program/resource/upden-US.res
%{baseinstdir}/program/resource/vclen-US.res
%{baseinstdir}/program/resource/wzien-US.res
%{baseinstdir}/program/resource/xmlsecen-US.res
%{baseinstdir}/program/resource/xsltdlgen-US.res
%{baseinstdir}/program/senddoc
%dir %{baseinstdir}/program/services
%{baseinstdir}/program/services/services.rdb
%{baseinstdir}/program/simplecanvas.uno.so
%{baseinstdir}/program/slideshow.uno.so
%{baseinstdir}/program/libsofficeapp.so
%{baseinstdir}/program/spadmin.bin
%{baseinstdir}/program/stringresource.uno.so
%{baseinstdir}/program/syssh.uno.so
%{baseinstdir}/program/tde-open-url
%{baseinstdir}/program/ucpcmis1.uno.so
%{baseinstdir}/program/ucpexpand1.uno.so
%{baseinstdir}/program/ucpext.uno.so
%{baseinstdir}/program/ucptdoc1.uno.so
%{baseinstdir}/program/unorc
%{baseinstdir}/program/updatefeed.uno.so
# TODO do we need this?
%{baseinstdir}/program/ui-previewer
%{baseinstdir}/ure-link
%{baseinstdir}/program/uri-encode
%{baseinstdir}/program/vbaevents.uno.so
%{baseinstdir}/program/vclcanvas.uno.so
%{baseinstdir}/program/versionrc
%dir %{baseinstdir}/share
%dir %{baseinstdir}/share/Scripts
%{baseinstdir}/share/Scripts/java
%dir %{baseinstdir}/share/autotext
%{baseinstdir}/share/autotext/en-US
%{baseinstdir}/share/basic
%dir %{baseinstdir}/share/config
%{baseinstdir}/share/config/images.zip
%{baseinstdir}/share/config/images_crystal.zip
%{baseinstdir}/share/config/images_hicontrast.zip
%{baseinstdir}/share/config/images_oxygen.zip
%{baseinstdir}/share/config/images_tango.zip
%{baseinstdir}/share/config/psetup.xpm
%{baseinstdir}/share/config/psetupl.xpm
%dir %{baseinstdir}/share/config/soffice.cfg
%{baseinstdir}/share/config/soffice.cfg/modules
# UI translations go into langpacks
%exclude %{baseinstdir}/share/config/soffice.cfg/modules/*/ui/res
%{baseinstdir}/share/config/soffice.cfg/*/ui
# UI translations go into langpacks
%exclude %{baseinstdir}/share/config/soffice.cfg/*/ui/res
%{baseinstdir}/share/config/webcast
%{baseinstdir}/share/config/wizard
%dir %{baseinstdir}/share/dtd
%{baseinstdir}/share/dtd/officedocument
%{baseinstdir}/share/gallery
%if 0%{?rhel} && 0%{?rhel} < 7
%{baseinstdir}/share/liblangtag
%endif
%dir %{baseinstdir}/share/psprint
%config %{baseinstdir}/share/psprint/psprint.conf
%{baseinstdir}/share/psprint/driver
%dir %{baseinstdir}/share/registry
%{baseinstdir}/share/registry/gnome.xcd
%{baseinstdir}/share/registry/lingucomponent.xcd
%{baseinstdir}/share/registry/main.xcd
%{baseinstdir}/share/registry/oo-ad-ldap.xcd.sample
%{baseinstdir}/share/registry/oo-ldap.xcd.sample
%{baseinstdir}/share/registry/Langpack-en-US.xcd
%dir %{baseinstdir}/share/registry/res
%{baseinstdir}/share/registry/res/fcfg_langpack_en-US.xcd
%dir %{baseinstdir}/share/template
%{baseinstdir}/share/template/en-US
%dir %{baseinstdir}/share/template/common
%{baseinstdir}/share/template/common/internal
%{baseinstdir}/share/template/common/layout
%{baseinstdir}/share/template/common/wizard
%{baseinstdir}/share/template/wizard
%dir %{baseinstdir}/share/wordbook
%{baseinstdir}/share/wordbook/en-GB.dic
%{baseinstdir}/share/wordbook/en-US.dic
%{baseinstdir}/share/wordbook/sl.dic
%{baseinstdir}/share/wordbook/technical.dic
%dir %{baseinstdir}/share/xslt
%{baseinstdir}/share/xslt/common
%dir %{baseinstdir}/share/xslt/export
%{baseinstdir}/share/xslt/export/common
%{baseinstdir}/share/xslt/export/spreadsheetml
%{baseinstdir}/share/xslt/export/wordml
%dir %{baseinstdir}/share/xslt/import
%{baseinstdir}/share/xslt/import/common
%{baseinstdir}/share/xslt/import/spreadsheetml
%{baseinstdir}/share/xslt/import/wordml
%{baseinstdir}/program/liblnthlo.so
%{_bindir}/unopkg
#icons and mime
%{_datadir}/icons/*/*/*/openoffice*
%{_datadir}/mime-info/openoffice.*
%{baseinstdir}/program/libxmlsecurity.so
%{_datadir}/mime/packages/openoffice.xml
%{baseinstdir}/program/configmgr.uno.so
%{baseinstdir}/program/desktopbe1.uno.so
%{baseinstdir}/program/fsstorage.uno.so
%{baseinstdir}/program/gconfbe1.uno.so
%{baseinstdir}/program/i18npool.uno.so
%{baseinstdir}/program/libbasegfxlo.so
%{baseinstdir}/program/libcomphelpgcc3.so
%{baseinstdir}/program/libfileacc.so
%{baseinstdir}/program/libfwelo.so
%{baseinstdir}/program/libfwilo.so
%{baseinstdir}/program/libfwklo.so
%{baseinstdir}/program/libfwllo.so
%{baseinstdir}/program/libfwmlo.so
%{baseinstdir}/program/libi18nisolang*.so
%{baseinstdir}/program/libi18nutilgcc3.so
%{baseinstdir}/program/libpackage2.so
%{baseinstdir}/program/libsblo.so
%{baseinstdir}/program/libsfxlo.so
%{baseinstdir}/program/libsotlo.so
%{baseinstdir}/program/libspllo.so
%{baseinstdir}/program/libspl_unxlo.so
%{baseinstdir}/program/libsvllo.so
%{baseinstdir}/program/libsvtlo.so
%{baseinstdir}/program/libtklo.so
%{baseinstdir}/program/libtllo.so
%{baseinstdir}/program/libucb1.so
%{baseinstdir}/program/libucpfile1.so
%{baseinstdir}/program/libutllo.so
%{baseinstdir}/program/libvcllo.so
%{baseinstdir}/program/libxmlscriptlo.so
%{baseinstdir}/program/libxolo.so
%{baseinstdir}/program/localebe1.uno.so
%{baseinstdir}/program/ucpgio1.uno.so
%{baseinstdir}/program/types/oovbaapi.rdb
#share unopkg
%dir %{baseinstdir}/share/extensions
%{baseinstdir}/share/extensions/package.txt
%{baseinstdir}/program/unopkg
%{baseinstdir}/program/unopkg.bin
%{baseinstdir}/program/bootstraprc
%{baseinstdir}/program/fundamentalrc
%{baseinstdir}/program/setuprc
%doc %{baseinstdir}/CREDITS.odt
%doc %{baseinstdir}/LICENSE
%doc %{baseinstdir}/LICENSE.html
%doc %{baseinstdir}/LICENSE.odt
%doc %{baseinstdir}/NOTICE
%{baseinstdir}/program/intro.*
%{baseinstdir}/program/soffice
%{baseinstdir}/program/soffice.bin
%{baseinstdir}/program/sofficerc
%{baseinstdir}/program/spadmin
%{baseinstdir}/program/unoinfo
%{baseinstdir}/program/libnpsoplugin.so
%{baseinstdir}/program/oosplash
%{baseinstdir}/program/shell/
%{baseinstdir}/share/config/images_brand.zip
%{baseinstdir}/share/xdg/
%{baseinstdir}/program/redirectrc
%{_datadir}/applications/openoffice-startcenter.desktop
#launchers
%{_bindir}/openoffice
%{_bindir}/openoffice.org
%{_bindir}/soffice
%{_bindir}/ooffice
%{_bindir}/ooviewdoc
%if 0%{?rhel} && 0%{?rhel} < 7
%{baseinstdir}/program/libraptor-lo.so.1
%{baseinstdir}/program/librasqal-lo.so.1
%{baseinstdir}/program/librdf-lo.so.0
%{baseinstdir}/program/libclucene.so
%{baseinstdir}/program/liblcms2.so.2
%{baseinstdir}/share/fingerprint
%endif

%post core
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :
for theme in hicolor locolor; do
    touch --no-create %{_datadir}/icons/$theme &>/dev/null || :
done

%postun core
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ $1 -eq 0 ] ; then
    for theme in hicolor locolor; do
        touch --no-create %{_datadir}/icons/$theme &>/dev/null || :
        gtk-update-icon-cache -q %{_datadir}/icons/$theme &>/dev/null || :
    done
fi

%posttrans core
for theme in hicolor locolor; do
    gtk-update-icon-cache -q %{_datadir}/icons/$theme &>/dev/null || :
done


%files base
%{baseinstdir}/help/en/sdatabase.*
%if 0%{?fedora} || 0%{?rhel} >= 7
%{baseinstdir}/program/classes/hsqldb.jar
%endif
%{baseinstdir}/program/classes/sdbc_hsqldb.jar
%{baseinstdir}/program/libabplo.so
%{baseinstdir}/program/libdbplo.so
%{baseinstdir}/program/libhsqldb.so
%{baseinstdir}/program/librptlo.so
%{baseinstdir}/program/librptuilo.so
%{baseinstdir}/program/librptxmllo.so
%{baseinstdir}/program/resource/abpen-US.res
%{baseinstdir}/program/resource/cnren-US.res
%{baseinstdir}/program/resource/dbpen-US.res
%{baseinstdir}/program/resource/rpten-US.res
%{baseinstdir}/program/resource/rptuien-US.res
%{baseinstdir}/program/resource/sdbclen-US.res
%{baseinstdir}/program/resource/sdberren-US.res
%{baseinstdir}/share/registry/base.xcd
%{baseinstdir}/program/sbase
%{_datadir}/applications/openoffice-base.desktop
%{_bindir}/oobase

%post base
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun base
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files report-builder
%docdir %{baseinstdir}/share/extensions/report-builder/help
%{baseinstdir}/share/extensions/report-builder

%files bsh
%{baseinstdir}/program/classes/ScriptProviderForBeanShell.jar
%{baseinstdir}/program/services/scriptproviderforbeanshell.rdb
%{baseinstdir}/share/Scripts/beanshell

%files rhino
%{baseinstdir}/program/classes/js.jar
%{baseinstdir}/program/classes/ScriptProviderForJavaScript.jar
%{baseinstdir}/program/services/scriptproviderforjavascript.rdb
%{baseinstdir}/share/Scripts/javascript

%files wiki-publisher
%docdir %{baseinstdir}/share/extensions/wiki-publisher/license
%{baseinstdir}/share/extensions/wiki-publisher

%files nlpsolver
%docdir %{baseinstdir}/share/extensions/nlpsolver/help
%{baseinstdir}/share/extensions/nlpsolver

%files ogltrans
%{baseinstdir}/program/OGLTrans.uno.so
%{baseinstdir}/share/config/soffice.cfg/simpress/transitions-ogl.xml
%{baseinstdir}/share/registry/ogltrans.xcd

%files presentation-minimizer
%docdir %{baseinstdir}/share/extensions/presentation-minimizer/help
%{baseinstdir}/share/extensions/presentation-minimizer

%files pdfimport
%{baseinstdir}/program/pdfimport.uno.so
%{baseinstdir}/program/xpdfimport
%{baseinstdir}/share/registry/pdfimport.xcd
%dir %{baseinstdir}/share/xpdfimport
%{baseinstdir}/share/xpdfimport/xpdfimport_err.pdf

%_font_pkg -n %{fontname} opens___.ttf
%doc solver/unxlng*/bin/ure/LICENSE

%files calc
%{baseinstdir}/help/en/scalc.*
%{baseinstdir}/program/libanalysislo.so
%{baseinstdir}/program/libcalclo.so
%{baseinstdir}/program/libdatelo.so
%{baseinstdir}/program/libforlo.so
%{baseinstdir}/program/libforuilo.so
%{baseinstdir}/program/libpricinglo.so
%{baseinstdir}/program/libsclo.so
%{baseinstdir}/program/libscdlo.so
%{baseinstdir}/program/libscfiltlo.so
%{baseinstdir}/program/libscuilo.so
%{baseinstdir}/program/libsolverlo.so
%{baseinstdir}/program/resource/analysisen-US.res
%{baseinstdir}/program/resource/dateen-US.res
%{baseinstdir}/program/resource/foren-US.res
%{baseinstdir}/program/resource/foruien-US.res
%{baseinstdir}/program/resource/pricingen-US.res
%{baseinstdir}/program/resource/scen-US.res
%{baseinstdir}/program/resource/solveren-US.res
%{baseinstdir}/program/vbaobj.uno.so
%{baseinstdir}/share/registry/calc.xcd
%{baseinstdir}/program/pagein-calc
%{baseinstdir}/program/scalc
%{_datadir}/applications/openoffice-calc.desktop
%{_bindir}/oocalc

%post calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun calc
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files draw
%{baseinstdir}/help/en/sdraw.*
%{baseinstdir}/share/registry/draw.xcd
%{baseinstdir}/program/pagein-draw
%{baseinstdir}/program/sdraw
%{_datadir}/applications/openoffice-draw.desktop
%{_bindir}/oodraw

%post draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun draw
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files emailmerge
%{baseinstdir}/program/mailmerge.py*
%{baseinstdir}/program/msgbox.py*
%{baseinstdir}/program/officehelper.py*

%files writer
%{baseinstdir}/help/en/swriter.*
%{baseinstdir}/program/libhwplo.so
%{baseinstdir}/program/liblwpftlo.so
%{baseinstdir}/program/libmswordlo.so
%{baseinstdir}/program/libswdlo.so
%{baseinstdir}/program/libswuilo.so
%{baseinstdir}/program/libt602filterlo.so
%{baseinstdir}/program/libwpftwriterlo.so
%{baseinstdir}/program/libwriterfilterlo.so
%{baseinstdir}/program/vbaswobj.uno.so
%{baseinstdir}/program/resource/t602filteren-US.res
%{baseinstdir}/share/registry/writer.xcd
%{baseinstdir}/program/pagein-writer
%{baseinstdir}/program/swriter
%{_datadir}/applications/openoffice-writer.desktop
%{_bindir}/oowriter

%post writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun writer
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files impress
%{baseinstdir}/help/en/simpress.*
%{baseinstdir}/program/libanimcorelo.so
%{baseinstdir}/program/libplacewarelo.so
%{baseinstdir}/program/PresenterScreen.uno.so
%dir %{baseinstdir}/share/config/soffice.cfg/simpress
%{baseinstdir}/share/config/soffice.cfg/simpress/effects.xml
%{baseinstdir}/share/config/soffice.cfg/simpress/transitions.xml
%{baseinstdir}/share/registry/impress.xcd
%{baseinstdir}/program/pagein-impress
%{baseinstdir}/program/simpress
%{_datadir}/applications/openoffice-impress.desktop
%{_bindir}/ooimpress

%post impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun impress
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files math
%{baseinstdir}/help/en/smath.*
%{baseinstdir}/program/libsmlo.so
%{baseinstdir}/program/libsmdlo.so
%{baseinstdir}/program/resource/smen-US.res
%{baseinstdir}/share/registry/math.xcd
%{baseinstdir}/program/smath
%{_datadir}/applications/openoffice-math.desktop
%{_bindir}/oomath

%post math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%postun math
update-desktop-database %{_datadir}/applications &> /dev/null || :

%files graphicfilter
%{baseinstdir}/program/libflashlo.so
%{baseinstdir}/program/libsvgfilterlo.so
%{baseinstdir}/share/registry/graphicfilter.xcd

%files xsltfilter
%{baseinstdir}/share/xslt/docbook
%{baseinstdir}/share/xslt/export/uof
%{baseinstdir}/share/xslt/export/xhtml
%{baseinstdir}/share/xslt/import/uof
%{baseinstdir}/share/registry/xsltfilter.xcd
%{_datadir}/applications/openoffice-xsltfilter.desktop

%files javafilter
%{baseinstdir}/program/classes/aportisdoc.jar
%{baseinstdir}/program/classes/pexcel.jar
%{baseinstdir}/program/classes/pocketword.jar
%{_datadir}/applications/openoffice-javafilter.desktop
%{baseinstdir}/share/registry/palm.xcd
%{baseinstdir}/share/registry/pocketexcel.xcd
%{baseinstdir}/share/registry/pocketword.xcd

%if 0%{?fedora} || 0%{?rhel} >= 7
%files postgresql
%{baseinstdir}/program/postgresql-sdbc.uno.so
%{baseinstdir}/program/postgresql-sdbc-impl.uno.so
%{baseinstdir}/program/postgresql-sdbc.ini
%{baseinstdir}/program/services/postgresql-sdbc.rdb
%{baseinstdir}/share/registry/postgresqlsdbc.xcd
%endif

%files ure
%doc solver/unxlng*/bin/ure/LICENSE
%{ureinstdir}

%files sdk
%{sdkinstdir}/
%exclude %{sdkinstdir}/docs/
%exclude %{sdkinstdir}/examples/

%files sdk-doc
%docdir %{sdkinstdir}/docs
%{sdkinstdir}/docs/
%{sdkinstdir}/examples/

%files headless
%{baseinstdir}/program/libbasebmplo.so
%{baseinstdir}/program/libvclplug_svplo.so

%files pyuno
%{baseinstdir}/program/libpyuno.so
%{baseinstdir}/program/pythonloader.py*
%{baseinstdir}/program/pythonloader.uno.so
%{baseinstdir}/program/pythonloader.unorc
%{baseinstdir}/program/pythonscript.py*
%{baseinstdir}/program/pyuno.so
%{baseinstdir}/program/services/scriptproviderforpython.rdb
%{baseinstdir}/program/wizards
%{baseinstdir}/share/Scripts/python
%{libo_python_sitearch}/uno.py*
%{libo_python_sitearch}/unohelper.py*
%if 0%{libo_python3}
%{libo_python_sitearch}/__pycache__/uno.cpython-*
%{libo_python_sitearch}/__pycache__/unohelper.cpython-*
%endif
%{baseinstdir}/share/registry/openlogo.xcd
%{baseinstdir}/share/registry/pyuno.xcd

%if 0%{?fedora}
%files kde
%{baseinstdir}/program/kde4be1.uno.so
%{baseinstdir}/program/libvclplug_kde4lo.so
%endif

%changelog
*  Mon Mar 4 2013 Fred Ollinger <follinge@gmail.com>
- Initial build of new release.

