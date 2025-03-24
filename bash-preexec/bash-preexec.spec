%global         forgeurl https://github.com/rcaloras/bash-preexec
%global         version0 0.5.0
%global         tag0 %{version0}
%forgemeta

Name:           bash-preexec
Version:        %{forgeversion}
Release:        %autorelease
Summary:        preexec and precmd functions for Bash just like Zsh

License:        MIT
URL:            https://github.com/rcaloras/bash-preexec
Source:         %{forgesource}

# Fix tests
Patch:          %{forgeurl}/commit/a44754f5c3ca76b0330324680670cb8574d2768f.patch

BuildRequires:  bats
BuildArch: noarch

%global _description %{expand:
preexec and precmd hook functions for Bash 3.1+ in the style of Zsh. They aim to
emulate the behavior as described for}

%description %_description

%package        all-users
Summary:        bash-preexec init script for all users
Requires:       bash-preexec = %{version}-%{release}

# Note: This package should conflict with any other package that uses `PROMPT_COMMAND` or `DEBUG`
# (See General Usage section of bash-preexec.sh)

%description    all-users %_description

This package contains the init script to enable bash-preexec for all users.


%prep
%autosetup -p1


%install
install -Dpm 644 bash-preexec.sh %{buildroot}%{_libexecdir}/bash-preexec/bash-preexec.sh
# Backport import guards into the auto-import script
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/bash-preexec.sh <<EOF
# bash-preexec initialization script

# Skip non-bash shells.
[ -z "\${BASH_VERSION-}" ] && return

# Skip noninteractive shells.
[[ \$- != *i* ]] && return

source %{_libexecdir}/bash-preexec/bash-preexec.sh
EOF


%check
bats test


%files
%license LICENSE.md
%doc README.md
%{_libexecdir}/bash-preexec/bash-preexec.sh

%files all-users
%{_sysconfdir}/profile.d/bash-preexec.sh


%changelog
%autochangelog

