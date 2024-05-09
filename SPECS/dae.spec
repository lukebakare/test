Name:           dae
Version:        6.0
Release:        1%{?dist}
Summary:        dae transparrent proxy
BuildArch:      noarch

License:        GPLv3
URL:            https://github.com/daeuniverse/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  go
Requires:       bash

%description
eBPF-based Linux high-performance transparent proxy solution.

%prep
%autosetup -n %{name}-%{version}

%build
# No build step required for a script

%install
install -Dm755 sources/installer.sh %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%changelog
* Thu May 09 2024 EC2 Default User
- Initial package
