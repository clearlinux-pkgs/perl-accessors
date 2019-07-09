#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-accessors
Version  : 1.01
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/S/SP/SPURKIS/accessors-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SP/SPURKIS/accessors-1.01.tar.gz
Summary  : create accessor methods in caller's package.
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

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


%prep
%setup -q -n accessors-1.01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
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
/usr/lib/perl5/vendor_perl/5.28.2/accessors.pm
/usr/lib/perl5/vendor_perl/5.28.2/accessors/chained.pm
/usr/lib/perl5/vendor_perl/5.28.2/accessors/classic.pm
/usr/lib/perl5/vendor_perl/5.28.2/accessors/ro.pm
/usr/lib/perl5/vendor_perl/5.28.2/accessors/rw.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/accessors.3
/usr/share/man/man3/accessors::chained.3
/usr/share/man/man3/accessors::classic.3
/usr/share/man/man3/accessors::ro.3
/usr/share/man/man3/accessors::rw.3
