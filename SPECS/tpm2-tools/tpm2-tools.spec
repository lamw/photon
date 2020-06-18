Summary:        The source repository for the TPM (Trusted Platform Module) 2 tools
Name:           tpm2-tools
Version:        4.1.3
Release:        1%{?dist}
License:        BSD 2-Clause
URL:            https://github.com/tpm2-software/tpm2-tools
Group:          System Environment/Security
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        %{name}-%{version}.tar.gz
%define sha1    tpm2-tools=b2cef4d06817a6859082d50863464a858a493a63
BuildRequires:  openssl-devel curl-devel tpm2-tss-devel
Requires:       openssl curl tpm2-tss
%description
The source repository for the TPM (Trusted Platform Module) 2 tools.

%prep
%setup -q
%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1
/usr/share/bash-completion/*

%changelog
*   Thu Jun 18 2020 Michelle Wang <michellew@vmware.com> 4.1.3-1
-   Update version to 4.1.3
*   Thu Feb 21 2019 Alexey Makhalov <amakhalov@vmware.com> 3.1.3-1
-   Initial build. First version
