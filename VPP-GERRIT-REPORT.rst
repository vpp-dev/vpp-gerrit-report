
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Thursday 2023-07-06, 02:44:06
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
  | `38648 <https:////gerrit.fd.io/r/c/vpp/+/38648>`_ [VECr 23]: api: memclnt - Mark old message versions as deprecated

avf: **Damjan Marion** <damarion@cisco.com>
  | `39056 <https:////gerrit.fd.io/r/c/vpp/+/39056>`_ [VECr 22]: avf: remove barrier
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VECr 30]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 30]: interface dpdk avf: introducing setting RSS hash key feature

build: **Damjan Marion** <damarion@cisco.com>
  | `39198 <https:////gerrit.fd.io/r/c/vpp/+/39198>`_ [VECr 1]: dpdk: fix variable type in pattern parsing
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 1]: fateshare: a plugin for managing child processes

classify: **Dave Barach** <vpp@barachs.net>
  | `39196 <https:////gerrit.fd.io/r/c/vpp/+/39196>`_ [VECr 1]: classify: add bpf support to pcap classifier

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 5]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 5]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 1]: fateshare: a plugin for managing child processes

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 13]: dpdk: create and remove interface in runtime
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VECr 30]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 30]: interface dpdk avf: introducing setting RSS hash key feature

dpdk-cryptodev: **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38749 <https:////gerrit.fd.io/r/c/vpp/+/38749>`_ [VECr 1]: dpdk-cryptodev: introduce sw_ring to the crypto op data path

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 12]: ethernet: run callbacks for subifs too when mac changes

fib: **Neale Ranns** <neale@graphiant.com>
  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VECr 16]: fib: Crash when specify a big prefix length from CLI.

flow: **Damjan Marion** <damarion@cisco.com>
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VECr 30]: flow dpdk avf: add support for using l2tpv3 as RSS type

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `39157 <https:////gerrit.fd.io/r/c/vpp/+/39157>`_ [VECr 7]: hs-test: improve get stats

interface: **Dave Barach** <vpp@barachs.net>
  | `39196 <https:////gerrit.fd.io/r/c/vpp/+/39196>`_ [VECr 1]: classify: add bpf support to pcap classifier
  | `39092 <https:////gerrit.fd.io/r/c/vpp/+/39092>`_ [VECr 8]: stats: fix duplicate /if/names entry
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 30]: interface dpdk avf: introducing setting RSS hash key feature

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VECr 16]: fib: Crash when specify a big prefix length from CLI.
  | `38639 <https:////gerrit.fd.io/r/c/vpp/+/38639>`_ [VECr 23]: api: ip - Mark old message versions as deprecated

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 2]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `39174 <https:////gerrit.fd.io/r/c/vpp/+/39174>`_ [VECr 2]: ipsec: fix sa bind cli
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 5]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VECr 13]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 22]: ipsec: huge anti-replay window support
  | `38641 <https:////gerrit.fd.io/r/c/vpp/+/38641>`_ [VECr 23]: api: ipsec - Mark old message versions as deprecated

lb: **Pfister** <ppfister@cisco.com>, **Hongjun Ni** <hongjun.ni@intel.com>
  | `39162 <https:////gerrit.fd.io/r/c/vpp/+/39162>`_ [VECr 6]: lb: Fix src_ip_sticky evaluation bug in per-port-vip case.

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `38654 <https:////gerrit.fd.io/r/c/vpp/+/38654>`_ [VECr 23]: api: lcp - Mark old message versions as deprecated

memif: **Damjan Marion** <damarion@cisco.com>
  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [VECr 14]: memif: use VPP cache line size macro instead of hard coded 64 bytes
  | `38644 <https:////gerrit.fd.io/r/c/vpp/+/38644>`_ [VECr 23]: api: memif - Mark old message versions as deprecated

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 1]: fateshare: a plugin for managing child processes
  | `39196 <https:////gerrit.fd.io/r/c/vpp/+/39196>`_ [VECr 1]: classify: add bpf support to pcap classifier
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 30]: interface dpdk avf: introducing setting RSS hash key feature

mpls: **Neale Ranns** <neale@graphiant.com>
  | `39022 <https:////gerrit.fd.io/r/c/vpp/+/39022>`_ [VECr 22]: mpls: add mpls_interface_dump

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `39131 <https:////gerrit.fd.io/r/c/vpp/+/39131>`_ [VECr 0]: vcl: ldp support SO_ORIGINAL_DST

pg: **Dave Barach** <vpp@barachs.net>
  | `38649 <https:////gerrit.fd.io/r/c/vpp/+/38649>`_ [VECr 23]: api: pg - Mark old message versions as deprecated

session: **Florin Coras** <fcoras@cisco.com>
  | `39131 <https:////gerrit.fd.io/r/c/vpp/+/39131>`_ [VECr 0]: vcl: ldp support SO_ORIGINAL_DST

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `38650 <https:////gerrit.fd.io/r/c/vpp/+/38650>`_ [VECr 20]: api: sr - Mark old message versions as deprecated

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 2]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VECr 2]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 5]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `39162 <https:////gerrit.fd.io/r/c/vpp/+/39162>`_ [VECr 6]: lb: Fix src_ip_sticky evaluation bug in per-port-vip case.
  | `39134 <https:////gerrit.fd.io/r/c/vpp/+/39134>`_ [VECr 8]: tests: Add checksum offload interface tests
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 12]: ethernet: run callbacks for subifs too when mac changes
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 22]: ipsec: huge anti-replay window support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 5]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 22]: ipsec: huge anti-replay window support

vapi: **Ole Troan** <ot@cisco.com>
  | `38491 <https:////gerrit.fd.io/r/c/vpp/+/38491>`_ [VECr 15]: vppapigen: c++ vapi stream message codegen

vcl: **Florin Coras** <fcoras@cisco.com>
  | `39131 <https:////gerrit.fd.io/r/c/vpp/+/39131>`_ [VECr 0]: vcl: ldp support SO_ORIGINAL_DST

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39196 <https:////gerrit.fd.io/r/c/vpp/+/39196>`_ [VECr 1]: classify: add bpf support to pcap classifier

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 22]: ipsec: huge anti-replay window support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Adrian Pistol** <vifino@posteo.net>:

  | `38702 <https:////gerrit.fd.io/r/c/vpp/+/38702>`_ [VEc 3]: linux-cp: Basic MPLS support.

**Alexander Kozyrev** <akozyrev@mellanox.com>:

  | `39133 <https:////gerrit.fd.io/r/c/vpp/+/39133>`_ [vEC 8]: dpdk: add Mellanox ConnectX-7 support

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [veC 159]: wireguard: move buffer when insufficient pre_data left

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38794 <https:////gerrit.fd.io/r/c/vpp/+/38794>`_ [vEC 21]: TEST: remove IKEv2 tests
  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [veC 41]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [veC 51]: TEST: remove the rdma mappings
  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 99]: TEST: make test string a test crash, for testing

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 15]: ip: add support for buffer offload metadata in ip midchain

**Damjan Marion** <dmarion@0xa5.net>:

  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 35]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 47]: libmemif: added tests
  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 121]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 35]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 121]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `39021 <https:////gerrit.fd.io/r/c/vpp/+/39021>`_ [vEC 8]: tests: save api trace for testcases in json format
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VeC 35]: misc: patch to test CI infra changes

**Dmitry Valter** <dvalter@protonmail.com>:

  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VeC 159]: stats: fix node name compatison

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 78]: dpdk: use adapter MTU in max_frame_size setting

**Filip Tehlar** <ftehlar@cisco.com>:

  | `39158 <https:////gerrit.fd.io/r/c/vpp/+/39158>`_ [vEC 7]: session: use session error type instead of vnet error

**Filip Varga** <fivarga@cisco.com>:

  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 43]: nat: nat66 cli bug fix

**GaoChX** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 56]: nat: nat44-ed get out2in workers failed for static mapping without port
  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VeC 177]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VeC 131]: ip: fix update checksum in ip4_ttl_inc

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 111]: nat: fix address resolution

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [Vec 142]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Maxime Peim** <mpeim@cisco.com>:

  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VeC 166]: classify: bypass drop filter on specific error

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 96]: nat: fix tcp session reopen in nat44-ed

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 93]: cnat: remove rwlock on ts
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [VeC 93]: cnat: dont compute offloaded cksums
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 93]: cnat: flag to disable rsession
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 93]: cnat: add ip/client bihash
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 121]: vppinfra: improve & test abstract socket

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [vec 47]: ip: IP address family common input node
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VeC 132]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 132]: ip: IPv6 validate input packet's header length does not exist buffer size

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 56]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38408 <https:////gerrit.fd.io/r/c/vpp/+/38408>`_ [VeC 119]: ipsec: fix logic in ext_hdr_is_pre_esp
  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [VeC 119]: ipsec: intorduce function esp_prepare_packet_for_enc
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VeC 119]: ipsec: esp_encrypt prefetch and unroll

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [veC 97]: gtpu: support non-G-PDU packets and PDU Session

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 42]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 65]: linux-cp: auto select tap id when creating lcp pair

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [Vec 70]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [vEC 20]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Ting Xu** <ting.xu@intel.com>:

  | `38708 <https:////gerrit.fd.io/r/c/vpp/+/38708>`_ [Vec 42]: idpf: add native idpf driver plugin

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [Vec 83]: mpls: fix possible crashes on tunnel create/delete
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 96]: nat: fix nat44_ed set_session_limit crash
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VeC 96]: nat: improve nat44-ed outside address distribution
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VeC 107]: api: fix mp-safe mark for some messages and add more
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 109]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VeC 109]: fib: fix freed mpls label disposition dpo access

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VeC 44]: ip: make running_fragment_id thread safe
  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 170]: api: fix vl_socket_write_ready

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 42]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node
  | `38733 <https:////gerrit.fd.io/r/c/vpp/+/38733>`_ [VeC 63]: ipsec: improve fast path policy searching performance
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 68]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 70]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VeC 105]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VeC 110]: ipsec: missing linear search when flow cache search failed
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 121]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [Vec 131]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VeC 132]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VeC 145]: misc: fix feature dispatch possible crashed when feature config changed by user
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [Vec 168]: api: fix api msg thread safe setting not work

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 41]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 76]: af_xdp: optimizing send performance
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VeC 133]: tap: add interface type check

**Yulong Pei** <yulong.pei@intel.com>:

  | `38135 <https:////gerrit.fd.io/r/c/vpp/+/38135>`_ [vec 93]: af_xdp: change default queue size as kernel xsk default

**grimlock** <realbaseball2008@gmail.com>:

  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VeC 35]: nat: nat44-ed bug fix
  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VeC 37]: nat: nat44-ed cli bug fix

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [veC 41]: vrrp: dump vrrp vr peer

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 96]: nat: add local addresses correctly in nat lb static mapping

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [VEc 5]: ipsec: separate UDP and UDP-encapsulated ESP packet processing

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
authors          72
maintainers      31
committers       0
abandoned        0
================ ===

