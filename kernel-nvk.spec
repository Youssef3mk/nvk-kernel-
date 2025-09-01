Name:           kernel-nvk
Version:        6.15  # يمكن تعديل الإصدار بناءً على آخر إصدار في الفرع nvk، تحقق من المستودع
Release:        1%{?dist}
Summary:        Linux Kernel from NVK branch

License:        GPL-2.0-only
URL:            https://gitlab.freedesktop.org/gfxstrand/linux
Source0:        git+https://gitlab.freedesktop.org/gfxstrand/linux.git#branch=nvk

BuildRequires:  bc bison dwarves elfutils-libelf-devel flex gcc gettext-devel kmod make ncurses-devel openssl-devel perl python3-devel
Requires:       coreutils dracut linux-firmware systemd

%description
Custom Linux kernel built from the NVK branch on GitLab, without additional patches.

%prep
%autosetup -S git

%build
make defconfig
make -j$(nproc)

%install
make INSTALL_MOD_PATH=%{buildroot} modules_install
install -d %{buildroot}/boot
install -m 644 arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{version}-nvk
install -m 644 System.map %{buildroot}/boot/System.map-%{version}-nvk
install -m 644 .config %{buildroot}/boot/config-%{version}-nvk

%files
%license COPYING
%doc README.md
/boot/vmlinuz-%{version}-nvk
/boot/System.map-%{version}-nvk
/boot/config-%{version}-nvk
/lib/modules/%{version}-nvk

%changelog
* Mon Sep 01 2025 Your Name <your.email@example.com> - 6.10-1
- Initial build of kernel from NVK branch on GitLab
