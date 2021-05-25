# FFMT-Packaging

## ArchLinux, Manjaro, Arcolinux and other Arch-based distros:
```
cd arch
makepkg -sri
```
## RPM-based Distros, such as OpenSuse and Fedora:
```
cd rpm
rpmbuild --undefine=_disable_source_fetch --define "_rpmdir $(pwd)" --clean -bb --rmsource ffmt.spec
sudo zypper install x86_64/ffmt-0.9.10-1.x86_64.rpm
```


Other packages available:
- MacOS: https://github.com/fosspill/homebrew-ffmt

