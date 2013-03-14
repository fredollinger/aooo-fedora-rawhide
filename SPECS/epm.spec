%define name TEMPLATE
%define epm 1
%define epm_version 4.2
%define source_url http://svn.easysw.com/public/epm

Summary:        ESP Package Manager (EPM)
Name:           epm 
Epoch:          1
Version:        %{epm_version}
Release:        %{dmake}
License:	GPLv2+
Group:          Applications/Development
URL:            http://www.epmhome.org
Source0:        epm-%{epm_version}.bz2

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
ESP Package Manager
EPM is an open source Unix software and file packageing program that generates archives from a list of files. 

%package tool
Summary: ESP Package Manager Tool
Group: Development

%description tool
Main files for the epm tool.

%prep
%setup -q 

%build
echo rm -rf epm %{buildroot}
%configure
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files

%doc man

%changelog
*  Thu Mar 20 2013 Fred Ollinger <follinge@gmail.com> 4.2-1
- Initial Packaging
