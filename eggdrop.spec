Summary:     Eggdrop is an IRC bot, written in C
Name:        eggdrop
%define versionmajor 2.0.0
%define versionminor -ALPHA
Version:     %{versionmajor}%{versionminor}
Release:     1
Copyright:   GPL
Group:       Applications/Communications
Group(pl):   Aplikacje/Komunikacja
Source0:     %{name}%{version}.tar.gz
Source1:     eggdrop.sh
Patch:       eggdrop-pld.patch
URL:         http://www.eggdrop.net/
Requires:    tcl
BuildRoot:	/tmp/%{name}-%{version}-root
Summary(pl): Eggdrop jest botem IRC napisanym w C

%description
Eggdrop is an IRC bot, written in C.  If you don't know what IRC is,
this is probably not whatever you're looking for!  Eggdrop, being a
bot, sits on a channel and takes protective measures: to keep the
channel from being taken over (in the few ways that anything CAN),
to recognize banished users or sites and reject them, to recognize
privileged users and let them gain ops, etc.
Eggdrop also contains many modules and scripts, for example for
sending files.

%description -l pl
Eggdrop jest IRCowym botem napisanym w C. Eggdrop, bêd±c botem
jest na kanale i zajmuje siê jego ochron±: zabezpieczeniem przed
takeover-em, nadawaniem odpowiednich przywilejów zarejestrowanym
u¿ytkownikom, pilnowanie tzw. banów. itp.
Eggdrop poza tymi funkcjami posiada tak¿e wiele dodatków, jak
przesy³anie plików czy inne skrypty dla rozrywki.

%prep
%setup -q -n %{name}%{version}
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=%{_bindir}
# Dziwny problem z -ldir w module filesys
cd src/mod/filesys.mod
rm -f config.cache config.log
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target}
cd ../../..
CFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,lib/eggdrop,man/man1}
make install DEST=$RPM_BUILD_ROOT%{_libdir}/eggdrop
rm -rf `find $RPM_BUILD_ROOT%{_libdir}/eggdrop -name CVS`
rm -rf $RPM_SOURCE_DIR/doc/CVS
mv $RPM_BUILD_ROOT%{_libdir}/eggdrop/doc/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
rm -rf $RPM_BUILD_ROOT%{_libdir}/eggdrop/doc/*
install $RPM_SOURCE_DIR/eggdrop.sh $RPM_BUILD_ROOT%{_bindir}/eggdrop

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc CONTENTS COPYING FEATURES INSTALL README doc/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/eggdrop/filesys
%{_libdir}/eggdrop/help
%{_libdir}/eggdrop/language
%ghost %{_libdir}/eggdrop/modules
%{_libdir}/eggdrop/modules-%{versionmajor}
%{_libdir}/eggdrop/scripts
%attr(755,root,root) %{_libdir}/eggdrop/eggdrop2-%{versionmajor}
%ghost %{_libdir}/eggdrop/eggdrop2
%{_libdir}/eggdrop/eggdrop2.conf.*
%{_libdir}/eggdrop/motd
%{_mandir}/man*/*

%changelog
* Sat Feb 20 1999 Marek Obuchowicz <elephant@shadow.eu.org>
[2.0.0-ALPHA-1]
 - minor spec modifications
 - added polish translations
 - compressed man files
 - added RPM_OPT_FLAGS support 

* Mon Sep 7 1998  Ian Macdonald <ianmacd@xs4all.nl>
 - Upgraded to 1.3.19
 
