Creating RPM's for CENTOS or RHEL
=================================

This repository contains 2 different images and an examples making use of both 

1. A simple docker image which creates the tools necessary to create an RPM.
The expectation is that this will be extended to be part of a pipeline,
potentionally a jenkins slave, but it works fine simply as a docker image running
locally.

2. An image that inherits from the base docker image in step 1, and supports the
use of a makefile.


## Create the first docker image

Note it installs a lot of additional dependency packages, so can take awhile

```
$ cd rpm-builder
$ docker build -t rpm-builder .
```


## Now the first example we can manually use image 1 to create an rpm, in this case nodejs.

I have a few files prepared on my local directory
```
$ ls -l  .
-rw-rw-r-- 1 owenn owenn      797 Oct 11 11:49 nodejs.spec
-rw-rw-r-- 1 owenn owenn      894 Oct 11 12:56 README.md
-rw-r--r-- 1 root  root  14781396 Oct 10 01:16 node-v12.19.0-linux-x64.tar.xz
```

So when I mount my docker image I specify the local directory, it also allows
me to write the output back to my local filesystem.

### Run the docker image which will also log into the image

```
$ docker run -ti -v`pwd`:/mnt rpm-builder:latest /bin/bash
```

### cd to the directory to build the package
```
#  cd ~/rpmbuild
```
_copy the source xz file into the SOURCES directory in root home directory, not
ideal but it works_
```
# cp /mnt/node-v12.19.0-linux-x64.tar.xz SOURCES/
```
_We can leave the spec file which decribes the rpm to create in the /mnt directory,
so lets have a quick look at it then run it_
```
# cat /mnt.nodejs.spec

Name:           nodejs
Version:        v12.19.0
Release:        1%{?dist}
Summary:        node-v12.19.0-linux-x64

License:        BSD
URL:		https://nodejs.org
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
```
```
# rpmbuild -bb /mnt/nodejs.spec
```
_After a lot of output, near the bottom you should have the line_

```Wrote: /root/rpmbuild/RPMS/x86_64/nodejs-v12.19.0-1.el7.x86_64.rpm```

_Copy it out to the the /mnt directory which will put it onto your local
filesystem, make sure you fix the permissions_

```
# cp /root/rpmbuild/RPMS/x86_64/nodejs-v12.19.0-1.el7.x86_64.rpm /mnt
# chmod 777 /mnt/nodejs-v12.19.0-1.el7.x86_64.rpm
# exit
```

## Creating the second image
We want this image to be runable on Openshift and if it detects a Makefile in
the current directory of the image it will run the Makefile

```
$ cd make
$ docker build -t rpm-build-make .
```

### Notes


Evaluate an RPM macro expression:

```
rpm -E '%_topdir'
```

Show all macro definitions:
```
rpm --showrc
spectool -C ~/rpmbuild/SOURCES -g package.spec
```

