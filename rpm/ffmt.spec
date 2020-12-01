Name:           ffmt
Version:        0.9.6.1
Release:        1%{?dist}
Summary:        FFXIV_Modding_Tool (FFMT for short) is a crossplatform commandline interface for Final Fantasy XIV Modding.
License:        GNU General Public License v3.0
URL:            https://ffmt.pwd.cat/docs/
Source0:        https://github.com/fosspill/FFXIV_Modding_Tool/releases/download/v0.9.6.1/FFXIV_Modding_Tool-linux-0.9.6.1.zip
AutoReqProv: no

%description
FFXIV_Modding_Tool, or FFMT for short, is a open source tool based on the xivModdingFramework which is used to modify datafiles belonging to Final Fantasy XIV

%prep
unzip %{SOURCE0}

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
/opt/ffmt/*


%changelog
* Sun Dec 01 2020 <github@elo.anonaddy.com> 
- Initial Build.
