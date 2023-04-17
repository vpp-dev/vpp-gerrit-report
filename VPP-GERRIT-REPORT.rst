
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Monday 2023-04-17, 02:11:09
--------------------------------------------


Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Maintainers:
------------
| **Please review these gerrit changes.**

| **NOTE: Gerrit changes may be included under more than one feature based on the modified files regardless of the feature list included on the commit headline.**

api: **Dave Barach** <vpp@barachs.net>
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 27]: api: fix mp-safe mark for some messages and add more

avf: **Damjan Marion** <damarion@cisco.com>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 5]: interface dpdk avf: introducing setting RSS hash key feature

build: **Damjan Marion** <damarion@cisco.com>
  | `38676 <https:////gerrit.fd.io/r/c/vpp/+/38676>`_ [VECr 0]: build: add Rocky Linux 8 support
  | `38632 <https:////gerrit.fd.io/r/c/vpp/+/38632>`_ [VECr 4]: dpdk: bump to DPDK 23.03
  | `38628 <https:////gerrit.fd.io/r/c/vpp/+/38628>`_ [VECr 4]: dpdk: code preparation for bumping to DPDK 22.11 and 23.03
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VECr 4]: dpdk: bump to dpdk 23.03

cnat: **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>, **Neale Ranns** <neale@graphiant.com>
  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VECr 13]: cnat: remove rwlock on ts
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [VECr 13]: cnat: dont compute offloaded cksums
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VECr 13]: cnat: flag to disable rsession
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VECr 13]: cnat: add ip/client bihash

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `38628 <https:////gerrit.fd.io/r/c/vpp/+/38628>`_ [VECr 4]: dpdk: code preparation for bumping to DPDK 22.11 and 23.03
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VECr 4]: dpdk: bump to dpdk 23.03
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 5]: interface dpdk avf: introducing setting RSS hash key feature

dpdk-cryptodev: **Sergio Gonzalez Monroy** <sergio.gonzalez.monroy@outlook.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38628 <https:////gerrit.fd.io/r/c/vpp/+/38628>`_ [VECr 4]: dpdk: code preparation for bumping to DPDK 22.11 and 23.03
  | `37840 <https:////gerrit.fd.io/r/c/vpp/+/37840>`_ [VECr 4]: dpdk: bump to dpdk 23.03

fib: **Neale Ranns** <neale@graphiant.com>
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VECr 29]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VECr 29]: fib: fix freed mpls label disposition dpo access

flow: **Damjan Marion** <damarion@cisco.com>
  | `38637 <https:////gerrit.fd.io/r/c/vpp/+/38637>`_ [VECr 3]: api: Mark old message versions as deprecated

interface: **Dave Barach** <vpp@barachs.net>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 5]: interface dpdk avf: introducing setting RSS hash key feature

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38639 <https:////gerrit.fd.io/r/c/vpp/+/38639>`_ [VECr 3]: api: Mark old message versions as deprecated
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 27]: api: fix mp-safe mark for some messages and add more

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38641 <https:////gerrit.fd.io/r/c/vpp/+/38641>`_ [VECr 2]: api: Mark old message versions as deprecated
  | `38528 <https:////gerrit.fd.io/r/c/vpp/+/38528>`_ [VECr 17]: ipsec: manually binding an SA to a worker
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VECr 25]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VECr 30]: ipsec: missing linear search when flow cache search failed

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 27]: api: fix mp-safe mark for some messages and add more

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VECr 2]: linux-cp: auto select tap id when creating lcp pair

memif: **Damjan Marion** <damarion@cisco.com>
  | `38477 <https:////gerrit.fd.io/r/c/vpp/+/38477>`_ [VECr 11]: memif: support dma option

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `38676 <https:////gerrit.fd.io/r/c/vpp/+/38676>`_ [VECr 0]: build: add Rocky Linux 8 support
  | `38634 <https:////gerrit.fd.io/r/c/vpp/+/38634>`_ [VECr 1]: build: correct variable name
  | `38629 <https:////gerrit.fd.io/r/c/vpp/+/38629>`_ [VECr 4]: build: few more .gitignore entries
  | `38624 <https:////gerrit.fd.io/r/c/vpp/+/38624>`_ [VECr 4]: misc: fix tracedump API to match CLI behavior
  | `38545 <https:////gerrit.fd.io/r/c/vpp/+/38545>`_ [VECr 24]: stats: check if stats vector entry is empty

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 11]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VECr 16]: nat: nat66 cli bug fix

packetforge: **Ting Xu** <ting.xu@intel.com>
  | `38499 <https:////gerrit.fd.io/r/c/vpp/+/38499>`_ [VECr 6]: packetforge: add option to show spec and mask only

perfmon: **Damjan Marion** <damarion@cisco.com>, **Ray Kinsella** <mdr@ashroe.eu>
  | `38506 <https:////gerrit.fd.io/r/c/vpp/+/38506>`_ [VECr 26]: perfmon: fix perfmon start type argument

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `38556 <https:////gerrit.fd.io/r/c/vpp/+/38556>`_ [VECr 20]: rdma: fix rx CQ mask to calculate right next_cqe_index

session: **Florin Coras** <fcoras@cisco.com>
  | `38526 <https:////gerrit.fd.io/r/c/vpp/+/38526>`_ [VECr 26]: session: cleanup ho lookup table on close

tcp: **Florin Coras** <fcoras@cisco.com>
  | `38526 <https:////gerrit.fd.io/r/c/vpp/+/38526>`_ [VECr 26]: session: cleanup ho lookup table on close

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 11]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VECr 16]: nat: fix tcp session reopen in nat44-ed
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 16]: nat: fix nat44_ed set_session_limit crash
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VECr 16]: nat: improve nat44-ed outside address distribution
  | `38597 <https:////gerrit.fd.io/r/c/vpp/+/38597>`_ [VECr 17]: wireguard: add support for chained buffers
  | `38528 <https:////gerrit.fd.io/r/c/vpp/+/38528>`_ [VECr 17]: ipsec: manually binding an SA to a worker
  | `38572 <https:////gerrit.fd.io/r/c/vpp/+/38572>`_ [VECr 18]: tests: support for expected failures

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 23]: misc: patch to test CI infra changes

vhost: **Steven Luong** <sluong@cisco.com>
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 27]: api: fix mp-safe mark for some messages and add more

vpp: **Dave Barach** <vpp@barachs.net>
  | `38545 <https:////gerrit.fd.io/r/c/vpp/+/38545>`_ [VECr 24]: stats: check if stats vector entry is empty
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VECr 27]: api: fix mp-safe mark for some messages and add more

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `38677 <https:////gerrit.fd.io/r/c/vpp/+/38677>`_ [VECr 0]: vppinfra: add format_hexdump_u{16,32,64}

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38597 <https:////gerrit.fd.io/r/c/vpp/+/38597>`_ [VECr 17]: wireguard: add support for chained buffers

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [veC 79]: wireguard: move buffer when insufficient pre_data left
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [Vec 125]: arp: fix arp request for ip4-glean node

**Andrew Ying** <hi@andrewying.com>:

  | `38064 <https:////gerrit.fd.io/r/c/vpp/+/38064>`_ [VeC 79]: dpdk: fix compatibility with DPDK < 21.11

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [vEC 19]: TEST: make test string a test crash, for testing
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VeC 31]: fateshare: a plugin for managing child processes
  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VeC 145]: acl: change the algorithm for cleaning the sessions from purgatory

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 118]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VEc 24]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VeC 32]: ip_session_redirect: add session redirect plugin
  | `38315 <https:////gerrit.fd.io/r/c/vpp/+/38315>`_ [VeC 32]: fib: fix load-balance and replicate dpos buckets overflow

**Damjan Marion** <dmarion@0xa5.net>:

  | `38630 <https:////gerrit.fd.io/r/c/vpp/+/38630>`_ [vEC 0]: vppinfra: native poly1305 implementation

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 41]: ebuild: adding libmemif to debian packages
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 81]: libmemif: added tests

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37836 <https:////gerrit.fd.io/r/c/vpp/+/37836>`_ [VEc 12]: dpdk-cryptodev: enq/deq scheme rework
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 41]: ipsec: esp_encrypt prefetch and unroll
  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 60]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dmitry Valter** <dvalter@protonmail.com>:

  | `38082 <https:////gerrit.fd.io/r/c/vpp/+/38082>`_ [VeC 75]: lb: fix flow table update vector handing with ASAN
  | `38071 <https:////gerrit.fd.io/r/c/vpp/+/38071>`_ [veC 76]: vppinfra: fix preallocated pool_put OOB with ASAN
  | `38070 <https:////gerrit.fd.io/r/c/vpp/+/38070>`_ [veC 76]: lb: fix flow table update vector handing with ASAN
  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VeC 79]: stats: fix node name compatison

**Duncan Eastoe** <duncaneastoe+github@gmail.com>:

  | `37750 <https:////gerrit.fd.io/r/c/vpp/+/37750>`_ [VeC 129]: stats: fix memory leak in stat_segment_dump_r()

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 41]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <fivarga@cisco.com>:

  | `35444 <https:////gerrit.fd.io/r/c/vpp/+/35444>`_ [veC 172]: nat: nat44-ed cleanup & improvements
  | `35966 <https:////gerrit.fd.io/r/c/vpp/+/35966>`_ [veC 172]: nat: nat44-ed update timeout api
  | `34929 <https:////gerrit.fd.io/r/c/vpp/+/34929>`_ [veC 172]: nat: det44 map configuration improvements
  | `36724 <https:////gerrit.fd.io/r/c/vpp/+/36724>`_ [VeC 172]: nat: fixing incosistency in use of sw_if_index
  | `36480 <https:////gerrit.fd.io/r/c/vpp/+/36480>`_ [VeC 172]: nat: nat64 fix add_del calls requirements

**Florin Coras** <florin.coras@gmail.com>:

  | `38562 <https:////gerrit.fd.io/r/c/vpp/+/38562>`_ [vEC 20]: session: support catch all proxy lookup

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37764 <https:////gerrit.fd.io/r/c/vpp/+/37764>`_ [Vec 51]: wireguard: under-load state determination update

**GaoChX** <chiso.gao@gmail.com>:

  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VeC 96]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VeC 51]: ip: fix update checksum in ip4_ttl_inc

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [Vec 123]: nat: make nat44 session limit api reinit flow_hash with new buckets.
  | `37726 <https:////gerrit.fd.io/r/c/vpp/+/37726>`_ [Vec 134]: nat: fix crash when set nat44 session limit with nonexisted vrf.
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VeC 145]: policer: fix crash when delete interface policer classify.
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VeC 145]: classify: fix classify session cli.

**Jing Peng** <jing@meter.com>:

  | `36578 <https:////gerrit.fd.io/r/c/vpp/+/36578>`_ [VeC 172]: nat: fix nat44-ed outside address selection
  | `36597 <https:////gerrit.fd.io/r/c/vpp/+/36597>`_ [VeC 172]: nat: fix nat44-ed API

**Klement Sekera** <klement.sekera@gmail.com>:

  | `38042 <https:////gerrit.fd.io/r/c/vpp/+/38042>`_ [VEc 5]: tests: enhance counter comparison error message
  | `38041 <https:////gerrit.fd.io/r/c/vpp/+/38041>`_ [VeC 80]: tests: refactor extra_vpp_punt_config

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 31]: nat: fix address resolution

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [Vec 62]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Maxime Peim** <mpeim@cisco.com>:

  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [vEc 4]: ipsec: huge anti-replay window support
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VeC 86]: classify: bypass drop filter on specific error

**Miguel Borges de Freitas** <miguel-r-freitas@alticelabs.com>:

  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [Vec 131]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 41]: vppinfra: improve & test abstract socket

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 40]: ip: IP address family common input node
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VeC 52]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 52]: ip: IPv6 validate input packet's header length does not exist buffer size

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38408 <https:////gerrit.fd.io/r/c/vpp/+/38408>`_ [VeC 39]: ipsec: fix logic in ext_hdr_is_pre_esp
  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [VeC 39]: ipsec: intorduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [VeC 39]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VeC 39]: ipsec: esp_encrypt prefetch and unroll

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [vEC 17]: gtpu: support non-G-PDU packets and PDU Session

**Sergey Matov** <sergey.matov@travelping.com>:

  | `31319 <https:////gerrit.fd.io/r/c/vpp/+/31319>`_ [VeC 172]: nat: DET: Allow unknown protocol translation

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `38491 <https:////gerrit.fd.io/r/c/vpp/+/38491>`_ [VeC 31]: vppapigen: c++ vapi stream message codegen
  | `38305 <https:////gerrit.fd.io/r/c/vpp/+/38305>`_ [VeC 54]: teib: fix nh-table-id
  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [Vec 82]: virtio: allocate frame per interface

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 63]: srv6-mobile: Implement SRv6 mobile API funcs

**Vladimir Bernolak** <vladimir.bernolak@pantheon.tech>:

  | `36723 <https:////gerrit.fd.io/r/c/vpp/+/36723>`_ [VeC 172]: nat: det44 map configuration improvements + tests

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VEc 3]: mpls: fix possible crashes on tunnel create/delete
  | `37263 <https:////gerrit.fd.io/r/c/vpp/+/37263>`_ [VeC 172]: nat: add nat44-ed session filtering by fib table

**Vratko Polak** <vrpolak@cisco.com>:

  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 90]: api: fix vl_socket_write_ready

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VeC 38]: crypto: making crypto-dispatch node working in adaptive mode
  | `38415 <https:////gerrit.fd.io/r/c/vpp/+/38415>`_ [VeC 39]: dpdk: fix format rx/tx burst function name failed
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 41]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [Vec 51]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VeC 52]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VeC 65]: misc: fix feature dispatch possible crashed when feature config changed by user
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [Vec 88]: api: fix api msg thread safe setting not work
  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [Vec 141]: udp: hand off packet to right session thread
  | `36704 <https:////gerrit.fd.io/r/c/vpp/+/36704>`_ [VeC 172]: nat: auto forward inbound packet for local server session app with snat

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38631 <https:////gerrit.fd.io/r/c/vpp/+/38631>`_ [vEC 3]: dpdk: bump to DPDK 22.11

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VEc 10]: af_xdp: optimizing send performance
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VeC 53]: tap: add interface type check

**Yulong Pei** <yulong.pei@intel.com>:

  | `38135 <https:////gerrit.fd.io/r/c/vpp/+/38135>`_ [vEc 13]: af_xdp: change default queue size as kernel xsk default

**grimlock** <realbaseball2008@gmail.com>:

  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VeC 39]: nat: nat44-ed cli bug fix
  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VeC 39]: nat: nat44-ed bug fix

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [veC 39]: vrrp: dump vrrp vr peer Type: fix

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [Vec 152]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [Vec 155]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [vEC 16]: nat: add local addresses correctly in nat lb static mapping
  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [veC 160]: policer: add policer classify to output path

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38497 <https:////gerrit.fd.io/r/c/vpp/+/38497>`_ [vEc 9]: crypto:  0UDP packet dropped when ipsec policy configured

Legend:
-------
========================== ===========================
Status Complete            Needs To Be Addressed
========================== ===========================
V - verified               v - not verified
E - not expired            e - expired
C - no unresolved comments c - comments not resolved
R - reviewed/approved      r - review incomplete
A - abandoned              A - gerrit.fd.io to restore
# - days since update      # - days since update > 30
========================== ===========================

Example: [VECr 23]
    - Verified
    - Not Expired
    - Comments resolved
    - Review incomplete (Code-Review < +1)
    - 23 days since last update


Statistics:
-----------
================ ===
Patches assigned
================ ===
authors          83
maintainers      37
committers       0
abandoned        0
================ ===

