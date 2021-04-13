Name:           ffmt
Version:        0.9.9
Release:        1%{?dist}
Summary:        FFXIV_Modding_Tool (FFMT for short) is a crossplatform commandline interface for Final Fantasy XIV Modding.
License:        GNU General Public License v3.0
URL:            https://ffmt.pwd.cat/docs/
Source0:        https://github.com/fosspill/FFXIV_Modding_Tool/releases/download/v%{version}/FFXIV_Modding_Tool-linux-%{version}.zip
AutoReqProv:    no
BuildRequires:  unzip

%description
FFXIV_Modding_Tool, or FFMT for short, is a open source tool based on the xivModdingFramework which is used to modify datafiles belonging to Final Fantasy XIV

%prep
unzip -o %{SOURCE0}

%setup -n FFXIV_Modding_Tool-linux

%build 

%install
mkdir -p %{buildroot}
mkdir -p -m0755 %{buildroot}/opt/
mkdir -p -m0755 %{buildroot}/%{_bindir}/
cp -r ffmt "%{buildroot}/opt/%{name}";
install -m 0755 ffmt.sh %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
/opt/%{name}
/opt/%{name}/*

%changelog
* Tue Apr 13 2021 <shinnova@users.noreply.github.com>
- Update to 0.9.9 for patch 5.5 support
* Tue Feb 09 2021 <shinnova@users.noreply.github.com>
- Update to 0.9.8 with small fixes
* Tue Dec 08 2020 <github@elo.anonaddy.com> 
- Update to 0.9.7 for patch 5.4 support
* Sun Dec 01 2020 <github@elo.anonaddy.com> 
- Initial Build.
