%define dmake_version 4.12.2
#%define source_url http://dmake.apache-extras.org.codespot.com/files/dmake-4.12.2.tar.bz2
%define source_url http://dmake.apache-extras.org.codespot.com/files/dmake-4.12.2.tar.bz2

Summary:        Build Tool For Open Office
Name:           dmake 
Epoch:          1
Version:        1
Release:        %{dmake}
License:        (MPLv1.1 or LGPLv3+) and LGPLv3 and LGPLv2+ and BSD and (MPLv1.1 or GPLv2 or LGPLv2 or Netscape) and Public Domain and ASL 2.0 and Artistic and MPLv2.0
Group:          Applications/Productivity
URL:            http://code.google.com/a/apache-extras.org/p/dmake/
Source0:        %{source_url}/dmake-{dmake_version}.tar.bz2

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

%description
DMake
A make utility similar to GNU make or the Workshop dmake. This
utility has an irregular syntax but is available for FreeBSD, Linux,
Solaris, Win32 and other platforms. It is used by the OpenOffice.org
build system, although for some time now Apache OpenOffice.Org and its
derivatives have been considering replacing it definitely with a
GNUmake-only build system.

%package tool
Summary: DMake Build Tool
Group: Development

%description tool
Main files for the dmake tool.
