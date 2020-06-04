Summary:	The basic required files for the root user's directory
Name:		rootfiles
Version:	11.0
Release:	22
License:	Public Domain
Group:		System/Base
Source0:	%{name}-%{version}.tar.bz2
BuildArch:	noarch

%description
The rootfiles package contains basic required files that are placed
in the root user's account.

%prep
%autosetup -p1

%install
install -d %{buildroot}/root
%make_install

%files
%doc ChangeLog 
%config(noreplace) /root/.Xdefaults
%config(noreplace) /root/.bash_logout
%config(noreplace) /root/.bash_profile
%config(noreplace) /root/.bash_completion
%config(noreplace) /root/.bashrc
%config(noreplace) /root/.cshrc
%config(noreplace) /root/.tcshrc
%config(noreplace) /root/.vimrc
%attr(0700,root,root) /root/tmp/

