Summary:	Eggdrop is an IRC bot, written in C
Summary(pl):	Eggdrop jest botem IRC napisanym w C
Name:		eggdrop
Version:	1.6.13
Release:	4
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.eggheads.org/pub/eggdrop/source/1.6/%{name}%{version}.tar.gz
# PLD docs - information about changes.
Source1:	http://pld.mysza.eu.org/sources/%{name}-README.PLD.en
Source2:	http://pld.mysza.eu.org/sources/%{name}-README.PLD.pl
# In order to unify filenames, following language packs and third-party modules were 
# repackaged. Some files were renamed, but none modified. Original archives can be 
# found by looking at http://www.egghelp.org/
Source10:	%{name}-language-danish.tar.gz
Source11:	%{name}-language-finnish.tar.gz
Source12:	%{name}-language-italian.tar.gz
Source13:	%{name}-language-norwegian.tar.gz
Source14:	%{name}-language-portuguese.tar.gz
Source15:	%{name}-language-portuguese_br.tar.gz
Source16:	%{name}-language-romanian.tar.gz
# Additional modules taken from various places
Source20:	%{name}-module-away-1.0.tar.gz
Source21:	%{name}-module-botnetop-1.0.1.tar.gz
Source22:	%{name}-module-fakebotnet-1.3.tar.gz
Source23:	%{name}-module-gseen-1.1.0.tar.gz
Source24:	%{name}-module-irctree-1.1.tar.gz
Source25:	%{name}-module-megahal-2.5.tar.gz
Source26:	%{name}-module-stats-1.3.3dev1.tar.gz
Source27:	%{name}-module-idea-1.0.0.tar.gz
Source28:	%{name}-module-twofish-1.0.tar.gz
Source29:	%{name}-module-rijndael-1.0.tar.gz
Patch0:		%{name}-FHS.patch
# Unofficial IPv6 patch
Patch1:		http://www.egghelp.org/files/patches/%{name}%{version}+ipv6.patch.gz
# Adds IPv6 variables to config file
Patch2:		%{name}%{version}+ipv6_config.patch
# Adds additional docs
Patch3:		%{name}-doc_makefile.patch
# Multilevel sharing patch - now it is possible to create *secure* multilevel
# botnets, each bot will only accept changes to userlist from bot that acts as 
# hub to him, and rejects changes from leaves
Patch4:		%{name}%{version}-multilevel_sharing.patch.gz
# Unlinkedby patch - when unlinking bot from botnet, adds nickname of a person
# that issues .unlink command to a broadcasted message
Patch5:		%{name}%{version}-unlinkedby.patch
URL:		http://www.eggheads.org/
BuildRequires:	tcl-devel
Requires:	tcl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eggdrop is an IRC bot, written in C. If you don't know what IRC is,
this is probably not whatever you're looking for! Eggdrop, being a
bot, sits on a channel and takes protective measures: to keep the
channel from being taken over (in the few ways that anything CAN), to
recognize banished users or sites and reject them, to recognize
privileged users and let them gain ops, etc. Eggdrop also contains
many modules and scripts, for example for sending files.

%description -l pl
Eggdrop jest IRCowym botem napisanym w C. Eggdrop, bêd±c botem jest na
kanale i zajmuje siê jego ochron±: zabezpieczeniem przed przejêciem,
nadawaniem odpowiednich przywilejów zarejestrowanym u¿ytkownikom,
pilnowanie tzw. banów itp. Eggdrop poza tymi funkcjami posiada tak¿e
wiele dodatków, jak przesy³anie plików czy inne skrypty dla rozrywki.

%prep
%setup -q -n %{name}%{version} -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p1

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
./configure
%{__make} config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/modules,%{_datadir}/%{name},%{_mandir}/man1,%{_datadir}/%{name}/{help,scripts,language},%{_datadir}/doc/%{name}-%{version}}

%{__make} DESTDIR="$RPM_BUILD_ROOT" install

cp $RPM_BUILD_ROOT/%{name}-%{version} $RPM_BUILD_ROOT%{_bindir}/%{name}

cp %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-%{version}/README.PLD.en
cp %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/doc/%{name}-%{version}/README.PLD.pl

find $RPM_BUILD_ROOT/doc -type f | egrep -v "(\.html$|\.htm$)" | xargs gzip -9nf
gzip -9nf $RPM_BUILD_ROOT/README $RPM_BUILD_ROOT/%{name}.conf 

cp $RPM_BUILD_ROOT/doc/man1/%{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz
rm -r $RPM_BUILD_ROOT/doc/man1

cp -a $RPM_BUILD_ROOT/*.gz \
	$RPM_BUILD_ROOT/doc/* \
	$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}/

cp -a $RPM_BUILD_ROOT/doc/modules $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

cp -a $RPM_BUILD_ROOT/text/* \
	$RPM_BUILD_ROOT/help/ \
	$RPM_BUILD_ROOT/scripts/ \
	$RPM_BUILD_ROOT/language/ \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/

cp -a $RPM_BUILD_ROOT/modules/* \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/modules/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_datadir}/doc/%{name}-%{version}
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
