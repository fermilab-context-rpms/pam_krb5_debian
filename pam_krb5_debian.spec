Summary:	A Pluggable Authentication Module for Kerberos 5
Name:		pam_krb5_debian
Version:	4.11
Release:	2%{?dist}
License:	MIT
Group:		System/Libraries
URL:		https://github.com/rra/pam-krb5
Source0:	https://github.com/rra/pam-krb5/archive/refs/tags/upstream/%{version}.tar.gz

Provides:	pam_krb5 = %{version}-%{release}

BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	krb5-devel
BuildRequires:	pam-devel

%description 
pam-krb5 is a Kerberos v5 PAM module for either MIT Kerberos or
Heimdal.  It supports ticket refreshing by screen savers, configurable
authorization handling, authentication of non-local accounts for
network services, password changing, and password expiration, as well
as all the standard expected PAM features.  It works correctly with
OpenSSH, even with ChallengeResponseAuthentication and
PrivilegeSeparation enabled, and supports extensive configuration
either by PAM options or in krb5.conf or both.  PKINIT is supported
with recent versions of both MIT Kerberos and Heimdal and FAST is
supported with recent MIT Kerberos.
  
%prep 
%setup -q -n pam-krb5-upstream-%{version}

%build
%configure --libdir=/%{_libdir}
%make_build

%install
%make_install

# Make the paths jive to avoid conflicts on multilib systems.
sed -ri -e 's|/lib(64)?/|/\$LIB/|g' %{buildroot}/%{_mandir}/man*/pam_krb5*.5*

# cleanup
rm -f %{buildroot}/%{_libdir}/security/*.la

%files
%license LICENSE
%doc README NEWS TODO
/%{_libdir}/security/pam_krb5.so
/%{_mandir}/man5/pam_krb5*

%changelog
* Wed Mar 9 2022 Pat Riehecky <riehecky@fnal.gov> 4.11-2
- Minor packaging nit

* Wed Feb 23 2022 Pat Riehecky <riehecky@fnal.gov> 4.11-1
- Initial fedora package
