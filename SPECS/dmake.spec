%define dmake 1
%define dmake_version 4.12.2
%define source_url http://dmake.apache-extras.org.codespot.com/files/dmake-4.12.2.tar.bz2

Summary:        Build Tool For OpenOffice
Name:           dmake 
Epoch:          1
Version:        4.12.2
Release:        %{dmake}
License:	GPLv2+
Group:          Applications/Productivity
URL:            http://code.google.com/a/apache-extras.org/p/dmake/
Source0:        %{source_url}/dmake-%{dmake_version}.tar.bz2

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
BuildRequires: gperf
BuildRequires: icu
BuildRequires: perl(Archive::Zip)
BuildRequires: perl(Digest::MD5)
BuildRequires: zip

%description
DMake
A make utility similar to GNU make or the Workshop dmake. This
utility has an irregular syntax but is available for FreeBSD, Linux,
Solaris, Win32 and other platforms. It is used by the OpenOffice
build system, although for some time now Apache OpenOffice and
related projects have been considering replacing it with a
GNUmake-only build system.

%package tool
Summary: DMake Build Tool
Group: Development

%description tool
Main files for the dmake tool.

%prep
%setup -q 

%build
%configure
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
/usr/bin/dmake
/usr/share/startup/config.mk
/usr/share/startup/startup.mk
/usr/share/startup/unix/linux/macros.mk
/usr/share/startup/unix/macros.mk
/usr/share/startup/unix/recipes.mk

%doc man

%changelog
*  Mon Mar 11 2013 Fred Ollinger <follinge@gmail.com> 4.12.2-1
- Initial Packaging
