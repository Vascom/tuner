Name:           tuner
Version:        1.5.1
Release:        1%{?dist}
Summary:        Minimalist radio station player

License:        GPLv3+
URL:            https://github.com/louis77/tuner
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gtk3-devel
BuildRequires:  granite-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  libsoup-devel
BuildRequires:  json-glib-devel
BuildRequires:  geoclue2-devel
BuildRequires:  geocode-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme


%description
Discover and Listen to your favourite internet radio stations.

%prep
%autosetup


%build
%meson
%meson_build

%install
%meson_install
%find_lang com.github.louis77.%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.louis77.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.louis77.%{name}.appdata.xml

%files -f com.github.louis77.%{name}.lang
%license LICENSE
%doc README.md NOTES.md
%{_bindir}/com.github.louis77.%{name}
%{_datadir}/icons/hicolor/*/apps/com.github.louis77.%{name}.svg
%{_datadir}/metainfo/com.github.louis77.%{name}.appdata.xml
%{_datadir}/applications/com.github.louis77.%{name}.desktop
%{_datadir}/glib-2.0/schemas/com.github.louis77.%{name}.gschema.xml

%changelog
* Sun Nov 27 2022 Vasiliy Glazov <vascom2@gmail.com> - 1.5.1-1
- Initial packaging
 
