Name: goss
Version: 0.3.5
Release: 1
Summary: Quick and Easy server testing/validation
Group: Development/Testing
License: Apache License 2.0
Url: https://github.com/aelsabbahy/goss
Source: https://github.com/aelsabbahy/%{name}/archive/v%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: curl

%description
Goss is a YAML based serverspec alternative tool for validating a servers configuration.
It eases the process of writing tests by allowing the user to generate tests from the current system state.
Once the test suite is written they can be executed, waited-on, or served as a health endpoint.

%prep

%setup -q

%install
rm -Rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
export GOSS_DST=%{buildroot}/usr/local/bin
sh install.sh

%clean
rm -rf %{buildroot}

%files
/usr/local/bin/goss
/usr/local/bin/dgoss

%changelog
* Tue Aug 29 2017 - robert (at) meinit.nl
- Initial release.
* Fri Sep 15 2017 - robert (at) meinit.nl
- Version bump 0.3.4 -> 0.3.5
