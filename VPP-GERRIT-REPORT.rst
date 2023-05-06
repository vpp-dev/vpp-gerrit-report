
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Saturday 2023-05-06, 02:05:16
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

af_packet: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `38643 <https:////gerrit.fd.io/r/c/vpp/+/38643>`_ [VECr 8]: api: Mark old message versions as deprecated

api: **Dave Barach** <vpp@barachs.net>
  | `38648 <https:////gerrit.fd.io/r/c/vpp/+/38648>`_ [VECr 8]: api: Mark old message versions as deprecated

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 18]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 18]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `38415 <https:////gerrit.fd.io/r/c/vpp/+/38415>`_ [VECr 15]: dpdk: fix format rx/tx burst function name failed
  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VECr 17]: dpdk: use adapter MTU in max_frame_size setting

dpdk-cryptodev: **Sergio Gonzalez Monroy** <sergio.gonzalez.monroy@outlook.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38749 <https:////gerrit.fd.io/r/c/vpp/+/38749>`_ [VECr 0]: dpdk-cryptodev: introduce sw_ring to the crypto op data path

flow: **Damjan Marion** <damarion@cisco.com>
  | `38727 <https:////gerrit.fd.io/r/c/vpp/+/38727>`_ [VECr 0]: flow: fix wrong to use ntohl function to u64 type variable

hash: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `38776 <https:////gerrit.fd.io/r/c/vpp/+/38776>`_ [VECr 0]: hash: add the document

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 0]: ipsec: huge anti-replay window support

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38639 <https:////gerrit.fd.io/r/c/vpp/+/38639>`_ [VECr 8]: api: Mark old message versions as deprecated

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 0]: ipsec: huge anti-replay window support
  | `38655 <https:////gerrit.fd.io/r/c/vpp/+/38655>`_ [VECr 0]: crypto: UDP packet dropped when ipsec policy configured
  | `38757 <https:////gerrit.fd.io/r/c/vpp/+/38757>`_ [VECr 0]: ipsec: fix ipsec_set_next_index set with wrong sa index when async frame commit failed
  | `38733 <https:////gerrit.fd.io/r/c/vpp/+/38733>`_ [VECr 2]: ipsec: improve fast path policy searching performance
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 18]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `38641 <https:////gerrit.fd.io/r/c/vpp/+/38641>`_ [VECr 21]: api: Mark old message versions as deprecated

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `38654 <https:////gerrit.fd.io/r/c/vpp/+/38654>`_ [VECr 0]: api: Mark old message versions as deprecated
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VECr 4]: linux-cp: auto select tap id when creating lcp pair

memif: **Damjan Marion** <damarion@cisco.com>
  | `38766 <https:////gerrit.fd.io/r/c/vpp/+/38766>`_ [VECr 0]: memif: fix coverity warnings
  | `38644 <https:////gerrit.fd.io/r/c/vpp/+/38644>`_ [VECr 8]: api: Mark old message versions as deprecated

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `38777 <https:////gerrit.fd.io/r/c/vpp/+/38777>`_ [VECr 0]: interface: add the transmit queue infrastructure document
  | `38624 <https:////gerrit.fd.io/r/c/vpp/+/38624>`_ [VECr 16]: misc: fix tracedump API to match CLI behavior

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VECr 0]: nat: nat44-ed bug fix
  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VECr 0]: nat: nat44-ed cli bug fix
  | `38647 <https:////gerrit.fd.io/r/c/vpp/+/38647>`_ [VECr 8]: api: Mark old message versions as deprecated
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 30]: nat: nat44-ed get out2in workers failed for static mapping without port

packetforge: **Ting Xu** <ting.xu@intel.com>
  | `38499 <https:////gerrit.fd.io/r/c/vpp/+/38499>`_ [VECr 0]: packetforge: add option to show spec and mask only

pg: **Dave Barach** <vpp@barachs.net>
  | `38649 <https:////gerrit.fd.io/r/c/vpp/+/38649>`_ [VECr 8]: api: Mark old message versions as deprecated

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `38694 <https:////gerrit.fd.io/r/c/vpp/+/38694>`_ [VECr 0]: misc: make format_hexdump length u32

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `38650 <https:////gerrit.fd.io/r/c/vpp/+/38650>`_ [VECr 8]: api: Mark old message versions as deprecated

tap: **Damjan Marion** <damarion@cisco.com>, **Steven Luong** <sluong@cisco.com>, **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VECr 4]: linux-cp: auto select tap id when creating lcp pair
  | `38651 <https:////gerrit.fd.io/r/c/vpp/+/38651>`_ [VECr 8]: api: Mark old message versions as deprecated

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 0]: ipsec: huge anti-replay window support
  | `38597 <https:////gerrit.fd.io/r/c/vpp/+/38597>`_ [VECr 4]: wireguard: add support for chained buffers
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 18]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 30]: nat: nat44-ed get out2in workers failed for static mapping without port

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 0]: ipsec: huge anti-replay window support
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 18]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 2]: misc: patch to test CI infra changes

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 0]: ipsec: huge anti-replay window support
  | `38694 <https:////gerrit.fd.io/r/c/vpp/+/38694>`_ [VECr 0]: misc: make format_hexdump length u32
  | `38738 <https:////gerrit.fd.io/r/c/vpp/+/38738>`_ [VECr 8]: vppinfra: add aarch64 support for format_ucontext_pc
  | `38415 <https:////gerrit.fd.io/r/c/vpp/+/38415>`_ [VECr 15]: dpdk: fix format rx/tx burst function name failed

vxlan: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `38646 <https:////gerrit.fd.io/r/c/vpp/+/38646>`_ [VECr 8]: api: Mark old message versions as deprecated

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38597 <https:////gerrit.fd.io/r/c/vpp/+/38597>`_ [VECr 4]: wireguard: add support for chained buffers

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [veC 98]: wireguard: move buffer when insufficient pre_data left
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [Vec 144]: arp: fix arp request for ip4-glean node

**Andrew Ying** <hi@andrewying.com>:

  | `38064 <https:////gerrit.fd.io/r/c/vpp/+/38064>`_ [VeC 98]: dpdk: fix compatibility with DPDK < 21.11

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 38]: TEST: make test string a test crash, for testing
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VeC 50]: fateshare: a plugin for managing child processes
  | `32164 <https:////gerrit.fd.io/r/c/vpp/+/32164>`_ [VeC 164]: acl: change the algorithm for cleaning the sessions from purgatory

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 137]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `33455 <https:////gerrit.fd.io/r/c/vpp/+/33455>`_ [VeC 51]: ip_session_redirect: add session redirect plugin
  | `38315 <https:////gerrit.fd.io/r/c/vpp/+/38315>`_ [VeC 51]: fib: fix load-balance and replicate dpos buckets overflow

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 60]: ebuild: adding libmemif to debian packages
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 100]: libmemif: added tests

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37836 <https:////gerrit.fd.io/r/c/vpp/+/37836>`_ [vEc 0]: dpdk-cryptodev: enq/deq scheme rework
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 60]: ipsec: esp_encrypt prefetch and unroll
  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 79]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dmitry Valter** <dvalter@protonmail.com>:

  | `38082 <https:////gerrit.fd.io/r/c/vpp/+/38082>`_ [VeC 94]: lb: fix flow table update vector handing with ASAN
  | `38071 <https:////gerrit.fd.io/r/c/vpp/+/38071>`_ [veC 95]: vppinfra: fix preallocated pool_put OOB with ASAN
  | `38070 <https:////gerrit.fd.io/r/c/vpp/+/38070>`_ [veC 95]: lb: fix flow table update vector handing with ASAN
  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VeC 98]: stats: fix node name compatison

**Duncan Eastoe** <duncaneastoe+github@gmail.com>:

  | `37750 <https:////gerrit.fd.io/r/c/vpp/+/37750>`_ [VeC 148]: stats: fix memory leak in stat_segment_dump_r()

**Filip Varga** <fivarga@cisco.com>:

  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 35]: nat: nat66 cli bug fix

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `37764 <https:////gerrit.fd.io/r/c/vpp/+/37764>`_ [Vec 70]: wireguard: under-load state determination update

**GaoChX** <chiso.gao@gmail.com>:

  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VeC 115]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VeC 70]: ip: fix update checksum in ip4_ttl_inc

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [Vec 142]: nat: make nat44 session limit api reinit flow_hash with new buckets.
  | `37726 <https:////gerrit.fd.io/r/c/vpp/+/37726>`_ [Vec 153]: nat: fix crash when set nat44 session limit with nonexisted vrf.
  | `37379 <https:////gerrit.fd.io/r/c/vpp/+/37379>`_ [VeC 164]: policer: fix crash when delete interface policer classify.
  | `37651 <https:////gerrit.fd.io/r/c/vpp/+/37651>`_ [VeC 164]: classify: fix classify session cli.

**Klement Sekera** <klement.sekera@gmail.com>:

  | `38042 <https:////gerrit.fd.io/r/c/vpp/+/38042>`_ [VEc 24]: tests: enhance counter comparison error message
  | `38572 <https:////gerrit.fd.io/r/c/vpp/+/38572>`_ [VeC 37]: tests: support for expected failures
  | `38041 <https:////gerrit.fd.io/r/c/vpp/+/38041>`_ [VeC 99]: tests: refactor extra_vpp_punt_config

**Koki Kiriyama** <kiriyama.kk@gmail.com>:

  | `38676 <https:////gerrit.fd.io/r/c/vpp/+/38676>`_ [vEC 17]: build: add Rocky Linux 8 support

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 50]: nat: fix address resolution

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [Vec 81]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Maxime Peim** <mpeim@cisco.com>:

  | `38528 <https:////gerrit.fd.io/r/c/vpp/+/38528>`_ [VeC 36]: ipsec: manually binding an SA to a worker
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VeC 105]: classify: bypass drop filter on specific error

**Miguel Borges de Freitas** <miguel-r-freitas@alticelabs.com>:

  | `37532 <https:////gerrit.fd.io/r/c/vpp/+/37532>`_ [Vec 150]: cnat: fix cnat_translation_cli_add_del call for del with INVALID_INDEX

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 35]: nat: fix tcp session reopen in nat44-ed

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `36484 <https:////gerrit.fd.io/r/c/vpp/+/36484>`_ [VEc 10]: libmemif: add testing application

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 32]: cnat: remove rwlock on ts
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [VeC 32]: cnat: dont compute offloaded cksums
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 32]: cnat: flag to disable rsession
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 32]: cnat: add ip/client bihash
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 60]: vppinfra: improve & test abstract socket

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [Vec 59]: ip: IP address family common input node
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VeC 71]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 71]: ip: IPv6 validate input packet's header length does not exist buffer size

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [VEc 0]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38408 <https:////gerrit.fd.io/r/c/vpp/+/38408>`_ [VeC 58]: ipsec: fix logic in ext_hdr_is_pre_esp
  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [VeC 58]: ipsec: intorduce function esp_prepare_packet_for_enc
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VeC 58]: ipsec: esp_encrypt prefetch and unroll

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [veC 36]: gtpu: support non-G-PDU packets and PDU Session

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `38491 <https:////gerrit.fd.io/r/c/vpp/+/38491>`_ [VeC 50]: vppapigen: c++ vapi stream message codegen
  | `38305 <https:////gerrit.fd.io/r/c/vpp/+/38305>`_ [VeC 73]: teib: fix nh-table-id
  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [Vec 101]: virtio: allocate frame per interface

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VEc 9]: srv6-mobile: Implement SRv6 mobile API funcs

**Ting Xu** <ting.xu@intel.com>:

  | `38708 <https:////gerrit.fd.io/r/c/vpp/+/38708>`_ [vEC 16]: idpf: add native idpf driver plugin

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VEc 22]: mpls: fix possible crashes on tunnel create/delete
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 35]: nat: fix nat44_ed set_session_limit crash
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VeC 35]: nat: improve nat44-ed outside address distribution
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VeC 46]: api: fix mp-safe mark for some messages and add more
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 48]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VeC 48]: fib: fix freed mpls label disposition dpo access

**Vratko Polak** <vrpolak@cisco.com>:

  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 109]: api: fix vl_socket_write_ready

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [vEC 7]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [vEC 9]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VeC 44]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VeC 49]: ipsec: missing linear search when flow cache search failed
  | `38453 <https:////gerrit.fd.io/r/c/vpp/+/38453>`_ [VeC 57]: crypto: making crypto-dispatch node working in adaptive mode
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 60]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [Vec 70]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VeC 71]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VeC 84]: misc: fix feature dispatch possible crashed when feature config changed by user
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [Vec 107]: api: fix api msg thread safe setting not work
  | `37681 <https:////gerrit.fd.io/r/c/vpp/+/37681>`_ [Vec 160]: udp: hand off packet to right session thread

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [vEc 10]: interface dpdk avf: introducing setting RSS hash key feature

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VEc 15]: af_xdp: optimizing send performance
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VeC 72]: tap: add interface type check

**Yulong Pei** <yulong.pei@intel.com>:

  | `38135 <https:////gerrit.fd.io/r/c/vpp/+/38135>`_ [vec 32]: af_xdp: change default queue size as kernel xsk default

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [veC 58]: vrrp: dump vrrp vr peer Type: fix

**jinshaohui** <jinsh11@chinatelecom.cn>:

  | `30929 <https:////gerrit.fd.io/r/c/vpp/+/30929>`_ [Vec 171]: vppinfra: fix memory issue in mhash
  | `37297 <https:////gerrit.fd.io/r/c/vpp/+/37297>`_ [Vec 174]: ping: fix ping ipv6 address set packet size greater than  mtu,packet drop

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 35]: nat: add local addresses correctly in nat lb static mapping
  | `37566 <https:////gerrit.fd.io/r/c/vpp/+/37566>`_ [veC 179]: policer: add policer classify to output path

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
maintainers      33
committers       0
abandoned        0
================ ===

