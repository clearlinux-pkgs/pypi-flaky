#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-flaky
Version  : 3.7.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/d5/dd/422c7c5c8c9f4982f3045c73d0571ed4a4faa5754699cc6a6384035fbd80/flaky-3.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d5/dd/422c7c5c8c9f4982f3045c73d0571ed4a4faa5754699cc6a6384035fbd80/flaky-3.7.0.tar.gz
Summary  : Plugin for nose or pytest that automatically reruns flaky tests.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-flaky-license = %{version}-%{release}
Requires: pypi-flaky-python = %{version}-%{release}
Requires: pypi-flaky-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=====

%package license
Summary: license components for the pypi-flaky package.
Group: Default

%description license
license components for the pypi-flaky package.


%package python
Summary: python components for the pypi-flaky package.
Group: Default
Requires: pypi-flaky-python3 = %{version}-%{release}

%description python
python components for the pypi-flaky package.


%package python3
Summary: python3 components for the pypi-flaky package.
Group: Default
Requires: python3-core
Provides: pypi(flaky)

%description python3
python3 components for the pypi-flaky package.


%prep
%setup -q -n flaky-3.7.0
cd %{_builddir}/flaky-3.7.0
pushd ..
cp -a flaky-3.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656404804
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-flaky
cp %{_builddir}/flaky-3.7.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-flaky/4be60be3fb459a4bf5026ae94171ea41f9ea29bb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-flaky/4be60be3fb459a4bf5026ae94171ea41f9ea29bb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
