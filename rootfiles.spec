%define name	rootfiles
%define version 11.0
%define release %mkrel 9

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




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 11.0-7mdv2011.0
+ Revision: 669430
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 11.0-6mdv2011.0
+ Revision: 607370
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 11.0-5mdv2010.1
+ Revision: 523928
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 11.0-4mdv2010.0
+ Revision: 426954
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 11.0-3mdv2009.1
+ Revision: 351556
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 11.0-2mdv2009.0
+ Revision: 225324
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 11.0-1mdv2008.1
+ Revision: 136482
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 23:35:32 (53133)
- 0.11

* Fri Aug 04 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/04/06 23:11:04 (53129)
Import rootfiles

* Mon Jun 13 2005 Guillaume Rousse <guillomovitch@mandrake.org> 10.2-2mdk
- add .bash_completion  
- drop explicit bash_completion sourcing from .bashrc
- spec cleanup

* Tue Jan 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 10.2-1mdk
- Modernize root's .vimrc
- Trim obsolete information from description

* Mon Jul 12 2004 Guillaume Rousse <guillomovitch@mandrake.org> 9.1-1mdk 
- enable bash-completion support in root .bashrc
- spec cleanup

