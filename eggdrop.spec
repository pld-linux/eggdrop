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
# In order to unify filenames, following language packs and third-party modules were
# repackaged. Some files were renamed, but none modified. Original archives can be
# found by looking at http://www.egghelp.org/
Source10:	%{name}-language-danish.tar.gz
# Source10-md5:	86b9bbab196f64b09e4daf2dec93fd50
Source11:	%{name}-language-finnish.tar.gz
# Source11-md5:	d720c6ad3f19deb8d51eeb753d0da390
Source12:	%{name}-language-italian.tar.gz
# Source12-md5:	9c568bc516ecb202ed9e76c1523e4d6a
Source13:	%{name}-language-norwegian.tar.gz
# Source13-md5:	118e14c8dfe0a6917e8e7b191a733e3f
Source14:	%{name}-language-portuguese.tar.gz
# Source14-md5:	1b96f1ba51a0162665be892327c405cf
Source15:	%{name}-language-portuguese_br.tar.gz
# Source15-md5:	93d4afae51dfa4cd7512fa6236868960
Source16:	%{name}-language-romanian.tar.gz
# Source16-md5:	3664b4f4870eb099d3a291284a076561
# Additional modules taken from various places
Source20:	%{name}-module-away-1.0.tar.gz
# Source20-md5:	89b0529d024d8c29a855fb26e9e24a58
Source21:	%{name}-module-botnetop-1.0.1.tar.gz
# Source21-md5:	1815a88748529d2ce6a221d560678285
Source22:	%{name}-module-fakebotnet-1.3.tar.gz
# Source22-md5:	bf6e0ecc97bbe154137dba5f47c6e518
Source23:	%{name}-module-gseen-1.1.0.tar.gz
# Source23-md5:	d1b5ff929c360581647a2baf7281a7a6
Source24:	%{name}-module-irctree-1.1.tar.gz
# Source24-md5:	8bf884c57adbb131228fe47bffc69836
Source25:	%{name}-module-megahal-2.5.tar.gz
# Source25-md5:	ee00bf26ef44ea587200c7e9a73dc767
Source26:	%{name}-module-stats-1.3.3dev1.tar.gz
# Source26-md5:	f50299b06dc9c8d29f7abb19defaa917
Source27:	%{name}-module-idea-1.0.0.tar.gz
# Source27-md5:	b1aa55ba5abebfcf0cf346b5bbba3bae
Source28:	%{name}-module-twofish-1.0.tar.gz
# Source28-md5:	861957c170b4af105199202e724be2a3
Source29:	%{name}-module-rijndael-1.0.tar.gz
# Source29-md5:	0210476c24ed6f24e1fdc1cbab41a863
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-doc_makefile.patch
# Multilevel sharing patch - now it is possible to create *secure* multilevel
# botnets, each bot will only accept changes to userlist from bot that acts as
# hub to him, and rejects changes from leaves
Patch2:		ftp://ftp.eggheads.org/pub/%{name}/patches/1.6/multilevel_sharing%{version}.patch
# Topicprot - protects channel topic from being changed
# This patch was a bit modified to apply to eggdrop1.6.13
Patch3:		ftp://ftp.eggheads.org/pub/%{name}/patches/1.6/topicprot%{version}.patch
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
# HUMPF! At least one thing sucks: 
# eggdrop's configure thingie, or my linux knowledge.
#./configure --enable-ipv6
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#cd src/mod/compress.mod
#%{__autoconf}
#cd ../dns.mod
#%{__autoconf}
#cd ../../..
%configure2_13 --enable-ipv6
%{__make} config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/modules,%{_datadir}/%{name},%{_mandir}/man1,%{_datadir}/%{name}/{help,scripts,language},%{_datadir}/doc/%{name}-%{version}}

%{__make} DESTDIR="$RPM_BUILD_ROOT" install

mv $RPM_BUILD_ROOT/%{name}-%{version} $RPM_BUILD_ROOT%{_bindir}/%{name}

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
