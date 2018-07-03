Name:		parity
Version:	1.11.4
Release:	1%{?dist}
Summary:	Fast, light, and robust Ethereum client

Group:		Applications/Internet
License:	GPLv3
URL:		http://www.github.com/parity/parity.git
Source0:	parity-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/tiggi/parity/rpm-package/scripts/rpm.parity.service
Source2:	https://raw.githubusercontent.com/tiggi/parity/rpm-package/scripts/rpm.parity.sysconfig
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


BuildRequires: rust, rhash
Requires: openssl

%description
Fast, light, and robust Ethereum client

%prep
%setup -q
export HOST_CC=gcc
export HOST_CXX=g++
export PLATFORM=x86_64-unknown-linux-gnu
rm -rf .cargo
mkdir -p .cargo
echo "[target.$PLATFORM]" >> .cargo/config
echo "linker= \"gcc\"" >> .cargo/config
touch configure
chmod 0755 configure


%build
#%configure
#make %{?_smp_mflags}
export HOST_CC=gcc
export HOST_CXX=g++
export PLATFORM=x86_64-unknown-linux-gnu
cargo build --target $PLATFORM --features final --release
cargo build --target $PLATFORM --release -p evmbin
cargo build --target $PLATFORM --release -p ethstore-cli
cargo build --target $PLATFORM --release -p ethkey-cli
cargo build --target $PLATFORM --release -p whisper-cli



%install
#make install DESTDIR=%{buildroot}
#rm -rf $RPM_BUILD_ROOT
export PLATFORM=x86_64-unknown-linux-gnu
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
cp target/$PLATFORM/release/parity $RPM_BUILD_ROOT/usr/bin/parity
cp target/$PLATFORM/release/parity-evm $RPM_BUILD_ROOT/usr/bin/parity-evm
cp target/$PLATFORM/release/ethstore $RPM_BUILD_ROOT/usr/bin/ethstore
cp target/$PLATFORM/release/ethkey $RPM_BUILD_ROOT/usr/bin/ethkey
cp target/$PLATFORM/release/whisper $RPM_BUILD_ROOT/usr/bin/whisper
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/lib/systemd/system/parity.service
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/parity
#cp rpm.parity.service $RPM_BUILD_ROOT/usr/lib/systemd/system/parity.service
#cp rpm.parity.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/parity

%files
%defattr(-,root,root,-)
/usr/bin/*
/usr/lib/systemd/system/parity.service
%config /etc/sysconfig/parity
%doc



%changelog
* Fri Jun 29 2018 Ulf Tigerstedt <tigerstedt@iki.fi> 1.11.4
- Initial rpm spec file
