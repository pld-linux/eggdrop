$Revision$, $Date$

Ten plik zawiera informacje dotyczace zmian, jakie wprowadzono w stosunku
do oryginalnego eggdropa.

Wszystkie ze wspomianych ni¿ej plików dostêpne s± tak¿e poprzez interfejs
CVSweb: http://cvs.pld.org.pl/

Nastêpuj±ce ³atki zosta³y na³o¿one:
* eggdrop-FHS.patch dostêpne pod adresem:
  http://pld.mysza.eu.org/sources/eggdrop-FHS.patch
  £ata ta modyfikuje rózne pliki sprawiaj±c, ¿e Eggdrop jest bardziej
  kompatybilny ze standardem Filesystem Hierarchy Standard
  
* eggdrop1.6.13+ipv6.patch.gz dostêpne pod adresem:
  http://www.egghelp.org/files/patches/eggdrop1.6.3+ipv6.patch.gz
  Ta ³ata dodaje wsparcie dla protoko³u IPv6.

* eggdrop1.6.13+ipv6_config.patch dostêpne pod adresem
  http://pld.mysza.eu.org/sources/eggdrop1.6.13+ipv6_config.patch
  Ta ³ata dodaje nowe zmienne (my-hostname6 i my-ip6) do pliku
  konfiguracyjnego.
  
* eggdrop-config_encryption.patch dostpne pod adresem
  http://pld.mysza.eu.org/sources/eggdrop-config_encryption.patch
  Ta prosta ³ata dodaje informacje o trzech nowych modu³ach szyfruj±cych
  do pliku eggdrop.conf
  
* eggdrop-doc_makefile.patch dostêpne pod adresem
  http://pld.mysza.eu.org/sources/eggdrop-doc_makefile.patch
  Ta ³ata modyfikuje plik doc/Makefile.in tak, aby dodatkowa dokumentacja
  zosta³a zainstalowana.
  
* eggdrop1.6.13-multilevel_sharing.patch.gz dostepne pod adresem
  ftp://ftp.eggheads.org/pub/eggdrop/patches/1.6/multilevel_sharing1.6.13.patch.gz
  (zmieniono nazwê pliku, ale nie zmodyfikowano go w ¿aden sposób)
  Ta ³ata dodaje nowe ustawienia, które sprawiaj±, ¿e botnet staje siê
  bezpieczniejszy - od tej pory bot mo¿e akceptowac zmiany w userli¶cie
  tylko od huba (hubów), i odrzuciæ wszelkie zmiany wys³ane przez boty mu
  podleg³e (leaves).
  
* eggdrop1.6.13-unlinkedby.patch dostêpne pod adresem
  ftp://ftp.eggheads.org/pub/eggdrop/patches/1.6/unlinkedby1.6.13.patch
  (zmieniono nazwê pliku, ale nie zmodyfikowano go w ¿aden sposób)
  Ta ³ata rozszerza wiadomo¶æ rozsy³an± do botnetu podczas od³±czania bota
  o pseudonim osoby, która u¿y³a komendy .unlink.

* eggdrop1.6.13-topicprot.patch dostêpne pod adresem
  http://pld.mysza.eu.org/sources/eggdrop1.6.13-topicprot.patch
  Ta ³ata, bazowana na ³atce topicprot.patch dla eggdrop1.6.12 dodaje mo¿liwo¶æ
  zablokowania topicu na danym kanale.

  
Dodano t³umaczenia plików pomocy na nastêpuj±ce jêzyki.
* duñski (dannish)
* fiñski (finnish)
* w³oski (italian)
* norweski (norwegian)
* portugalski (portuguese)
* brazyliska odmiana portugalskiego (portuguese_br)
* rumuñski (romanian)
  T³umaczenia dla poszczególnych jêzyków dostêpne s± pod adresem
  http://pld.mysza.eu.org/sources/eggdrop-language-{language}.tar.gz
  gdzie {language} jest angielsk± nazw± danego jêzyka (podana w nawiasach)
  Pliki te zosta³y znalezione pod adresem http://www.egghelp.org/ . Zosta³y
  one przepakowane.
  
Dodano nastêpuj±ce dodatkowe modu³y:  
* away 1.0
* botnetop 1.0.1
* fakebotnet 1.3
* gseen 1.1.0
* irctree 1.1
* megahal 2.5
* stats 1.3.3dev1
  Ka¿dy z tych modu³ów dostepny jest pod adresem:
  http://pld.mysza.eu.org/sources/eggdrop-module-{module}-{version}.tar.gz
  Zosta³y one wziête z ró¿nych miejsc, wliczaj±c w to:
  * http://www.visions-of-fantasy.de/
  * http://johoho.eggheads.org/
  * ftp://ftp.eggheads.org/
  Pliki te mog± byæ ³atwo znaleziono u¿ywaj±c google.

