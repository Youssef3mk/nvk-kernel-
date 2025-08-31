# Fedora bits
%define __spec_install_post %{__os_install_post}
%define _build_id_links none
%define _default_patch_fuzz 2
%define _disable_source_fetch 0
%define debug_package %{nil}
%define make_build make %{?_lto_args} %{?_smp_mflags}
%undefine __brp_mangle_shebangs
%undefine _auto_set_build_flags
%undefine _include_frame_pointers

# Linux Kernel Versions
%define _basekver 6.16
%define _stablekver 3
%define _rpmver %{version}-%{release}
%define _kver %{_rpmver}.%{_arch}

%if %{_stablekver} == 0
    %define _tarkver %{_basekver}
%else
    %define _tarkver %{version}
%endif

# Build minimal kernel config disabled
%define _build_minimal 0

# Don't build with clang/thinLTO
%define _build_lto 0

# No NVIDIA kernel modules build
%define _build_nv 0

# Kernel tickrate
%define _hz_tick 300

# x86_64 ISA level
%define _x86_64_lvl 2

# Packaging directories
%define _kernel_dir /lib/modules/%{_kver}
%define _devel_dir %{_usrsrc}/kernels/%{_kver}

# No patch source as no patches needed


Name:           kernel-nvk
Summary:        Vanilla Linux Kernel from NVK branch on GitLab
Version:        %{_basekver}.%{_stablekver}
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            https://gitlab.freedesktop.org/gfxstrand/linux

Requires:       kernel-core-uname-r = %{_kver}
Requires:       kernel-modules-uname-r = %{_kver}
Requires:       kernel-modules-core-uname-r = %{_kver}
Provides:       installonlypkg(kernel)
Provides:       kernel = %{_rpmver}
Provides:       kernel-core-uname-r = %{_kver}
Provides:       kernel-uname-r = %{_kver}

BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  dwarves
BuildRequires:  elfutils-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  kmod
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl-Carp
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  python3-devel
BuildRequires:  python3-pyyaml
BuildRequires:  python-srpm-macros

Source0:        git+https://gitlab.freedesktop.org/gfxstrand/linux.git#branch=nvk
Source1:            https://raw.githubusercontent.com/CachyOS/linux-cachyos/master/linux-cachyos-server/config


%description
Vanilla Linux kernel compiled from NVK branch on GitLab without patches.

%prep
%autosetup -S git

# Optional: if you want to use a specific config file, uncomment and add
# cp %{SOURCE1} .config

%build
make defconfig
make -j$(nproc)

%install
make INSTALL_MOD_PATH=%{buildroot} modules_install
install -d %{buildroot}%{_kernel_dir}
install -m 644 arch/x86/boot/bzImage %{buildroot}%{_kernel_dir}/vmlinuz

%files
%license COPYING
%doc README.md
%{_kernel_dir}/vmlinuz
%{_kernel_dir}/modules.builtin
%{_kernel_dir}/modules.builtin.modinfo
%{_kernel_dir}/symvers.zst
%{_kernel_dir}/config
%{_kernel_dir}/System.map

%changelog
* Mon Sep  1 2025 Your Name <your.email@example.com> - 1.0-1
- Build vanilla Linux kernel from NVK branch without patches
