Summary:    Eggdrop is an IRC bot, written in C
Name:       eggdrop
Version:    1.3.19
Release:    1
Copyright:  GPL
Group:      Applications/Communications
Source0:    ftp://ftp.eggdrop.net/pub/eggdrop/official/%{name}%{version}.tar.gz
Source1:    eggdrop.sh
Patch:      eggdrop.diff
URL:        http://www.eggdrop.net/
Requires:   tcl
BuildRoot:  /tmp/%{name}-%{version}-root

%description
Eggdrop is an IRC bot, written in C.  If you don't know what IRC is,
this is probably not whatever you're looking for!  Eggdrop, being a
bot, sits on a channel and takes protective measures: to keep the
channel from being taken over (in the few ways that anything CAN),
to recognize banished users or sites and reject them, to recognize
privileged users and let them gain ops, etc.

%prep
%setup -n %{name}%{version}
%patch -p1

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,lib/%{name},man/man1}

make install DEST=$RPM_BUILD_ROOT/usr/lib/%{name}
install  $RPM_BUILD_ROOT/usr/lib/%{name}/doc/man1/%{name}.1 \
	$RPM_BUILD_ROOT/usr/man/man1
rm -rf doc/man1/
install $RPM_SOURCE_DIR/eggdrop.sh $RPM_BUILD_ROOT/usr/bin/eggdrop

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%attr(644, root, root, 755)
%doc README doc/BOTNET doc/KNOWN-PROBLEMS doc/MODULES doc/UPDATES*
%doc doc/eggdrop.doc doc/nets.list doc/tcl-commands.doc doc/tricks
%attr(755, root, root) /usr/bin/*
/usr/lib/%{name}/%{name}
/usr/lib/%{name}/motd
/usr/lib/%{name}/filesys
/usr/lib/%{name}/help
/usr/lib/%{name}/language
/usr/lib/%{name}/modules
/usr/lib/%{name}/scripts
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Mon Sep 7 1998  Ian Macdonald <ianmacd@xs4all.nl>
- Upgraded to 1.3.19
