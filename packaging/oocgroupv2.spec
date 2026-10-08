Name:           oocgroupv2
Version:        0.2.0
Release:        1%{?dist}
Summary:        Visualizes the active cgroup v2 slice hierarchy and resource shares.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocgroupv2
Source0:        oocgroupv2-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocgroupv2 is a sovereign, capability-bounded CGROUP V2 TREE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocgroupv2
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocgroupv2-uninstall

%files
/usr/bin/oocgroupv2
/usr/bin/oocgroupv2-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
