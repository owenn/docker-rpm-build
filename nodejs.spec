Name:           nodejs
Version:        v12.19.0
Release:        1%{?dist}
Summary:        node-v12.19.0-linux-x64

License:        BSD
URL:		https://nodejs.org/dist/v12.19.0/node-v12.19.0-linux-x64.tar.xz
Source0:       	node-v12.19.0-linux-x64.tar.xz
Packager:	Nigel Owen     

%description
nodejs as Rhel 7.8 does not support nodejs as a package I have created this package

%prep
%setup -n node-v12.19.0-linux-x64

%install
mkdir -p %{buildroot}/usr/local
mv bin lib include share %{buildroot}/usr/local
chmod -R 0755 %{buildroot}/usr/local/lib/ %{buildroot}/usr/local/bin %{buildroot}/usr/local/include
chmod -R 444 %{buildroot}/usr/local/share
rm -rf %{buildroot}/usr/local/share/doc %{buildroot}/usr/local/share/systemtap
%files
%doc
/usr/local/lib/*
/usr/local/bin/*
/usr/local/include/*
/usr/local/share/man/man1/*
%build

%changelog
