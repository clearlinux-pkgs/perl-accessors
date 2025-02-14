#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-accessors
Version  : 1.01
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/S/SP/SPURKIS/accessors-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SP/SPURKIS/accessors-1.01.tar.gz
Summary  : create accessor methods in caller's package.
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-accessors-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
accessors - create accessor methods in caller's package.
SYNOPSIS
package Foo;
use accessors qw( foo bar baz );

%package dev
Summary: dev components for the perl-accessors package.
Group: Development
Provides: perl-accessors-devel = %{version}-%{release}
Requires: perl-accessors = %{version}-%{release}

%description dev
dev components for the perl-accessors package.


%package perl
Summary: perl components for the perl-accessors package.
Group: Default
Requires: perl-accessors = %{version}-%{release}

%description perl
perl components for the perl-accessors package.


%prep
%setup -q -n accessors-1.01
cd %{_builddir}/accessors-1.01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/accessors.3
/usr/share/man/man3/accessors::chained.3
/usr/share/man/man3/accessors::classic.3
/usr/share/man/man3/accessors::ro.3
/usr/share/man/man3/accessors::rw.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
