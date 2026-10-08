# oocgroupv2: Sovereign CGROUP V2 TREE

<div align="center">

```
================================================================================
                                oocgroupv2
               Sovereign openOODA CGROUP V2 TREE
================================================================================
```

**Sovereign CGROUP V2 TREE**  
*Visualizes the active cgroup v2 slice hierarchy and resource shares.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oocgroupv2/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oocgroupv2-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oocgroupv2/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oocgroupv2/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oocgroupv2-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oocgroupv2/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oocgroupv2 [options] [PATH]

Visualizes the active cgroup v2 slice hierarchy and resource shares.

Options:
  -p, --path <PATH>    root cgroup path (default: /sys/fs/cgroup)
  -s, --slice <NAME>   filter hierarchy to specific slice (e.g. system, user)
  -d, --depth <N>      maximum traversal depth (default: 3)
      --shares         display sibling CPU shares and weight distribution
      --psi            display Pressure Stall Information (PSI) panel
      --events         display OOM kill counts and population events
      --procs          display task counts for cgroup nodes
      --summary        display summary of slices, active controllers, and tasks
      --demo           run against synthetic cgroup v2 hierarchy
      --json           output formatted as JSON Lines
  -h, --help           display this help and exit
  -v, --version        output version information and exit
      --mcp            run as Model Context Protocol stdio server
```

---

## 3. Theming Integration (`oote`)

`oocgroupv2` synchronizes visual styles and status colors with [oote](https://github.com/openOODA-tools/oote):
* **Configuration:** Reads active palette from `~/.openooda/theme.oot`.
* **Environment Overrides:** Respects `$OODA_THEME` and `$NO_COLOR`.

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oocgroupv2` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
oocgroupv2 --mcp
```

### Available Tools

* **`cgroupv2_tree`**: Visualizes active cgroup v2 slice hierarchy and resource limits.
  * Parameters: `path` (string, optional), `slice` (string, optional)
* **`cgroupv2_inspect`**: Inspects specific cgroup v2 node (controllers, procs, memory, CPU quota).
  * Parameters: `path` (string, required)
* **`cgroupv2_psi`**: Reads Pressure Stall Information (PSI) for CPU, memory, and IO.
  * Parameters: `resource` (string, optional: "all", "cpu", "memory", "io")
* **`cgroupv2_controllers`**: Audits controller delegation and subtree_control down the hierarchy.
  * Parameters: `path` (string, optional)
* **`cgroupv2_events`**: Inspects memory OOM kills and population state.
  * Parameters: `path` (string, optional)

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (&ProcCap, &SysInfoCap, &McpCap). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
