%global commit 1a4fa013dcc112439edf57a3708c77d4ab6ba21a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global buildid .nvk

Name:           kernel-nvk
Version:        6.15.0
Release:        1%{?dist}
Summary:        Linux kernel with NVK (Nouveau Vulkan) support

License:        GPL-2.0-only
URL:            https://gitlab.freedesktop.org/gfxstrand/linux
Source0:        linux-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  bc
BuildRequires:  xz
BuildRequires:  cpio
BuildRequires:  openssl
BuildRequires:  dwarves
BuildRequires:  elfutils-libelf-devel
BuildRequires:  openssl-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  kernel-rpm-macros
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  findutils
BuildRequires:  kmod

%description
The Linux kernel with experimental NVK (Nouveau Vulkan) support from the gfxstrand/linux repository, nvk branch. This kernel includes enhancements for the Nouveau open-source NVIDIA driver with Vulkan capabilities.

%package headers
Summary:        Header files for the Linux kernel with NVK support
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description headers
This package provides kernel header files for development with the NVK kernel.

%prep
%autosetup -n linux-%{commit}
# Optionally, copy a custom kernel config (e.g., Fedora's kernel-x86_64.config)
# cp %{SOURCE1} .config || make olddefconfig
make olddefconfig

%build
make %{?_smp_mflags} bzImage
make %{?_smp_mflags} modules

%install
# Install kernel image, System.map, and config
install -d %{buildroot}/boot
install -m 644 arch/%{_target_cpu}/boot/bzImage %{buildroot}/boot/vmlinuz-%{version}%{buildid}
install -m 644 System.map %{buildroot}/boot/System.map-%{version}%{buildid}
install -m 644 .config %{buildroot}/boot/config-%{version}%{buildid}

# Install kernel modules
make INSTALL_MOD_PATH=%{buildroot} modules_install

# Install kernel headers for development
make INSTALL_HDR_PATH=%{buildroot}%{_prefix} headers_install

# Generate kernel module dependencies
%kernel_module_install

%files
%license COPYING
/boot/vmlinuz-%{version}%{buildid}
/boot/System.map-%{version}%{buildid}
/boot/config-%{version}%{buildid}
/lib/modules/%{version}%{buildid}

%files headers
%{_prefix}/include/linux
%{_prefix}/include/asm
%{_prefix}/include/asm-generic
%{_prefix}/include/uapi

%changelog
* Mon Sep 01 2025 Your Name <your.email@example.com> - 6.15.0-1
- Initial build from nvk branch, commit 1a4fa013dcc112439edf57a3708c77d4ab6ba21a
