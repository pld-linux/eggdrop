Summary:	Eggdrop is an IRC bot, written in C
Summary(pl):	Eggdrop jest botem IRC napisanym w C
Summary(pt_BR):	Bot de IRC escrito em C
Summary(ru_RU.KOI8-R): Eggdrop, это IRC-бот написанный на языке C.
Name:		eggdrop
Version:	1.6.15
Release:	0.3
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.eggheads.org/pub/eggdrop/source/1.6/%{name}%{version}.tar.bz2
# Source0-md5:	b5016e34942ff4113e97a8449b15dfce
# PLD docs - information about changes.
Source1:	http://pld.mysza.eu.org/sources/%{name}-README.PLD.en
# Source1-md5:	273f001b6294fc78eaafe0517a1d2771
Source2:	http://pld.mysza.eu.org/sources/%{name}-README.PLD.pl
# Source2-md5:	a1ead6e4cc3c5268e0daffa013d023f8
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
Patch1:		%{name}-doc_makefile.patch
# Multilevel sharing patch - now it is possible to create *secure* multilevel
# botnets, each bot will only accept changes to userlist from bot that acts as
# hub to him, and rejects changes from leaves
Patch2:		%{name}-multilevel_sharing.patch
# Topicprot - protects channel topic from being changed
# This patch was a bit modified to apply to eggdrop1.6.13
Patch3:		%{name}-topicprot.patch
# Adds information about additional encryption modules to config file
Patch4:		%{name}-config_encryption.patch
# This one fixes eggdrop botchk/autobotchk scripts
Patch5:		%{name}-autobotchk.patch
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
many modules and scripts, for example for sending files. Here is the
list of new features as opposed to vanilla eggdrop:
- Built-in IPv6 support
- Additional modules, including:
  - away
  - botnetop
  - fakebotnet
  - gseen
  - irctree
  - megahal
  - stats
  - three new encryption modules: idea, twofish, rijndael
- Additional language packs:
  - dannish
  - finnish
  - italian
  - norwegian
  - portuguese
  - brazillian portuguese
  - romanian
- Various small patches were applied 
For more information, see README.PLD.en file located under 
%{_docdir}/%{name}-%{version}

%description -l pl
Eggdrop jest IRCowym botem napisanym w C. Eggdrop, bЙd╠c botem jest na
kanale i zajmuje siЙ jego ochron╠: zabezpieczeniem przed przejЙciem,
nadawaniem odpowiednich przywilejСw zarejestrowanym u©ytkownikom,
pilnowanie tzw. banСw itp. Eggdrop poza tymi funkcjami posiada tak©e
wiele dodatkСw, jak przesyЁanie plikСw czy inne skrypty dla rozrywki.
Oto lista nowych mo©liwo╤ci w odrС©nieniu od 'czystego' eggdropa:
- Wbudowane wsparcie dla IPv6
- Dodatkowe moduЁy, takie jak:
  - away
  - botnetop
  - fakebotnet
  - gseen
  - irctree
  - megahal
  - stats
  - trzy nowe moduЁy szyfruj╠ce: idea, twofish, rijndael
- Dodatkowe
  - duЯski
  - fiЯski
  - wЁoski
  - norweski
  - portugalski
  - brazylijska odmiana portugalskiego
  - rumuЯski
- Zaaplikowano rСzne mniejsze lub wiЙksze Ёaty 
WiЙcej informacji znajdziesz w pliku README.PLD.pl znajduj╠cym siЙ 
w katalogu %{_docdir}/%{name}-%{version}

%description -l pt_BR
Eggdrop И um bot de IRC, escrito em linguagem C.

Eggdrop, sendo um bot, permanece em um canal e toma medidas de
proteГ?o: evitando que o canal seja tomado (usando as poucas maneiras
possМveis), reconhecendo usuАrios ou sites expulsos e os rejeitando,
reconhecendo usuАrios privilegiados e permitindo que estes recebam OPS
etc.

%description -l ru_RU.KOI8-R
Eggdrop, это IRC-бот написанный на языке C. Если вы не знаете,
что такое IRC, то это вероятно не то, что вы ищете!
Eggdrop находится на канале в целях оказания защитных мер:
охраны канала от перехвата управления злоумышленниками,
распознования пользователей или сайтов, для которых канал
блокирован, с последующим отказом в доступе,
распознавания операторов канала, с присвоением им
соответствующих прав и привилегий.

%prep
%setup -q -n %{name}%{version} -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a28 -a29
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
# There is no sense in using configure macro, as the eggdrop makes no use
# of provided settings, or at least of those given with --*dir options
./configure --enable-ipv6
%{__make} config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/modules,%{_datadir}/%{name},%{_mandir}/man1,%{_datadir}/%{name}/{help,scripts,language},%{_datadir}/doc/%{name}-%{version}}

%{__make} DESTDIR="$RPM_BUILD_ROOT" install

mv $RPM_BUILD_ROOT/%{name}-%{version} $RPM_BUILD_ROOT%{_bindir}/%{name}

cp %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/README.PLD.en
cp %{SOURCE2} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/README.PLD.pl

find $RPM_BUILD_ROOT/doc -type f | egrep -v "(\.html$|\.htm$)" | xargs gzip -9nf
gzip -9nf $RPM_BUILD_ROOT/README $RPM_BUILD_ROOT/%{name}.conf

cp $RPM_BUILD_ROOT/doc/man1/%{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz
rm -r $RPM_BUILD_ROOT/doc/man1

cp -a $RPM_BUILD_ROOT/*.gz \
	$RPM_BUILD_ROOT/doc/* \
	$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

cp -a $RPM_BUILD_ROOT/doc/modules $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

cp -a $RPM_BUILD_ROOT/text/* \
	$RPM_BUILD_ROOT/help/ \
	$RPM_BUILD_ROOT/scripts/ \
	$RPM_BUILD_ROOT/language/ \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/

cp -a $RPM_BUILD_ROOT/modules/* \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/modules/

# These are only to make /usr/lib/rpm/check-files happy(ier)
# Is this somehow ugly?
for i in modules modules-%{version} text help scripts language doc logs eggdrop.conf.gz README.gz; do
	rm -rf $RPM_BUILD_ROOT/$i
done

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
