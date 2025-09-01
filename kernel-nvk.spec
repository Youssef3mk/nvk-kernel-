Name:           kernel-nvk
Version:        6.15
Release:        1%{?dist}
Summary:        Linux Kernel from NVK branch on GitLab

License:        GPL-2.0-only
URL:            https://gitlab.freedesktop.org/gfxstrand/linux
Source0:        https://gitlab.freedesktop.org/gfxstrand/linux/-/archive/nvk/linux-nvk.tar.gz

BuildRequires:  bc bison dwarves elfutils-libelf-devel flex gcc gettext-devel kmod make ncurses-devel openssl-devel perl python3-devel

%global debug_package %{nil}
%define _devel_dir /usr/src/kernels/%{version}-nvk

%description
Custom Linux kernel built directly from the NVK branch on GitLab, without additional patches.

%prep
%setup -q -n linux-nvk

make defconfig

%build
make -j$(nproc)

%install
make INSTALL_MOD_PATH=%{buildroot}/usr/lib/modules/%{version}-nvk modules_install
install -d %{buildroot}/boot
install -m 644 arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{version}-nvk
install -m 644 System.map %{buildroot}/boot/System.map-%{version}-nvk
install -m 644 .config %{buildroot}/boot/config-%{version}-nvk

# إصلاح الرابط الرمزي build ليكون نسبي
rm -rf %{buildroot}/usr/lib/modules/%{version}-nvk/build
ln -s %{_devel_dir} %{buildroot}/usr/lib/modules/%{version}-nvk/build

%files
/boot/vmlinuz-%{version}-nvk
/boot/System.map-%{version}-nvk
/boot/config-%{version}-nvk
/usr/lib/modules/%{version}-nvk

%changelog
* Mon Sep 01 2025 Your Name <your.email@example.com> - 6.15-1
- Initial build; fixed debug package and symlink issues.
