Name:       alsa-ucm-data-max98090
Summary:    ALSA UCM data pkg for MAXIM MAX98090 codec
Version:    0.0.1
Release:    1
License:    LGPL-2.1+
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz

%description
ALSA UCM data for max98090

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/alsa/ucm
cp -a max98090 %{buildroot}/usr/share/alsa/ucm
mkdir -p %{buildroot}/usr/share/license
cp -a LICENSE.LGPL-2.1+ %{buildroot}/usr/share/license/%{name}

%post

%files
%manifest alsa-ucm-conf-max98090.manifest
/usr/share/alsa/ucm/max98090/*
/usr/share/license/alsa-ucm-data-max98090
