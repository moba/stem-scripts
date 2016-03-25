# stem scripts
a collection of small scripts for some Tor metrics that I needed, using the [stem](https://stem.torproject.org) library

## listrelaysbyspeed.py

```
❯ python listrelaysbyspeed.py
Fetching latest descriptors, can take a while...

7623 relays (1036 exits)
total bandwidth exit relays: 4886 MB/s
80% (3909 MB/s): 280 exit relays
Fastest: aurora (78 MB/s): 0x02225522 Frenn vun der Enn (FVDE) <info AT enn DOT lu>
Slowest: nirvana (5 MB/s): None

Total contacts: 128

Fuzzy total: 108

#RELAYS | Contact
58      | <none>
11      | Nicholas Merrill <nick AT calyx dot com> 14wntQ8cBdnhUVfYmDjXz6PbpSSX8nCtkr
10      | Torservers.net <support .AT. torservers .DOT. net>
10      | Babylon Network | noc <AT> babylon <DOT> network | PGP 0x2A540FA5 | 1HiSG8pia5DdDLUMyYNkF9sicGozojZLnH
7       | http://www.privacyfoundation.ch/abuse/  BTC: 15s5e8u9NcAZUie6ivMXLa2AvatvmtxqXu
7       | abuse[__aT   ]necto|doT--|onion
6       | 0x02225522 Frenn vun der Enn (FVDE) <info AT enn DOT lu>
6       | Accessnow.org <abuse .AT. accessnow .DOT. org>
5       | Privacy Republic <abuse-team _at_ PrivacyRepublic _dot_ org>
5       | TNinja <abuse-team _at_ tor _dot_ ninja>
5       | drift@multinet.no - 1Geq8GGC7qTh7dfptneAYtpeARPAL8B2kh
5       | Random Person <tor0102.10.swsnyder AT spamgourmet dot com>
4       | 0x9F29C15D42A8B6F3 Nos oignons <adminsys@nos-oignons.net> - 17WLwtW63FrHeMAEVkALnwhfmizBxGXDW1
3       | https://www.torservers.net/donate.html <support .AT. torservers .DOT. net>
2       | tor-admin AT torland DOT is
2       | tor.glubbo@yandex.com
2       | SaveYourPrivacy.NET <saveyourprivacynet@openmailbox.org> - 1LJ9d5StAKr2Yb3q1avLCeRTq4GddDN8d2
2       | Ben <tor@bendellar.com>
2       | kolus riseup net
2       | tor-relays@coldhak.ca
2       | TvdW <tor AT tvdw DOT eu> - bitcoin 1NKKoCQwKs67eKBGedMD8wYoAs3Z4mMAex
2       | Harvester 0xEFF9A2B7 <contact .AT. harvester .DOT. fr>
2       | Umich Tor <tor-exit-admin@umich.edu>
2       | TNOR-ARIN
2       | technik@piraten-nds.de
2       | <tordonator (aaat) openmail.cc> - 1PSZsh9J3ZDL42AaiUPfpTjk5SaFtBNFqX
2       | 0x6F6D60C1 Security Dept <hello@brasshorncommunications.uk>
2       | Abuse Department <abuse AT hartvoorinternetvrijheid dot nl>
2       | Eran Sandler <eran@sandler.co.il>
1       | 0x65714c2b6f3b74cb Thijs Houtenbos <info@thijshoutenbos.nl>
```
