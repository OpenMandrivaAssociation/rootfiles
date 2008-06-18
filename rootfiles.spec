%define name	rootfiles
%define version 11.0
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	The basic required files for the root user's directory
License:	Public Domain
Group:		System/Base
Source:		%name-%version.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildArch:	noarch

%description
The rootfiles package contains basic required files that are placed
in the root user's account.

%prep
%setup -q

%install
rm -rf %{buildroot}
install -d %buildroot/root
make install DESTDIR=%buildroot

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
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


