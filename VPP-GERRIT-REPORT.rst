
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Saturday 2023-06-10, 02:27:27
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

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `38963 <https:////gerrit.fd.io/r/c/vpp/+/38963>`_ [VECr 7]: af_xdp: set frame_no_append flag

avf: **Damjan Marion** <damarion@cisco.com>
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VECr 4]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 4]: interface dpdk avf: introducing setting RSS hash key feature

build: **Damjan Marion** <damarion@cisco.com>
  | `39017 <https:////gerrit.fd.io/r/c/vpp/+/39017>`_ [VECr 0]: misc: bpf_trace_filter
  | `38782 <https:////gerrit.fd.io/r/c/vpp/+/38782>`_ [VECr 21]: af_xdp: fix the error of linking to libbpf.a

classify: **Dave Barach** <vpp@barachs.net>
  | `38997 <https:////gerrit.fd.io/r/c/vpp/+/38997>`_ [VECr 0]: vnet: turn vnet_is_packet_traced into callback

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 10]: crypto: fix async frame memory crash if frame pool expanded when using

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `39017 <https:////gerrit.fd.io/r/c/vpp/+/39017>`_ [VECr 0]: misc: bpf_trace_filter
  | `39005 <https:////gerrit.fd.io/r/c/vpp/+/39005>`_ [VECr 2]: docs: fix packages path in tutorial

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VECr 4]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 4]: interface dpdk avf: introducing setting RSS hash key feature
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VECr 15]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

dpdk-cryptodev: **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38749 <https:////gerrit.fd.io/r/c/vpp/+/38749>`_ [VECr 0]: dpdk-cryptodev: introduce sw_ring to the crypto op data path
  | `39018 <https:////gerrit.fd.io/r/c/vpp/+/39018>`_ [VECr 0]: dpdk-cryptodev: introduce sw_ring
  | `39019 <https:////gerrit.fd.io/r/c/vpp/+/39019>`_ [VECr 0]: dpdk-cryptodev: enq/deq scheme rework

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 15]: ethernet: run callbacks for subifs too when mac changes

fib: **Neale Ranns** <neale@graphiant.com>
  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VECr 16]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

flow: **Damjan Marion** <damarion@cisco.com>
  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VECr 4]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VECr 15]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

interface: **Dave Barach** <vpp@barachs.net>
  | `39002 <https:////gerrit.fd.io/r/c/vpp/+/39002>`_ [VECr 0]: vppapigen: fix crash with autoendian arrays
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 4]: interface dpdk avf: introducing setting RSS hash key feature

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VECr 18]: ip: make running_fragment_id thread safe

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VECr 0]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process
  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [VECr 3]: ipsec: separate UDP and UDP-encapsulated ESP packet processing
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 10]: crypto: fix async frame memory crash if frame pool expanded when using

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VECr 21]: libmemif: added tests

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `38702 <https:////gerrit.fd.io/r/c/vpp/+/38702>`_ [VECr 2]: linux-cp: Basic MPLS support.

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39017 <https:////gerrit.fd.io/r/c/vpp/+/39017>`_ [VECr 0]: misc: bpf_trace_filter
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 4]: interface dpdk avf: introducing setting RSS hash key feature
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 7]: vcl: ldp support SO_ORIGINAL_DST

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 7]: vcl: ldp support SO_ORIGINAL_DST
  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VECr 9]: nat: nat44-ed bug fix
  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VECr 11]: nat: nat44-ed cli bug fix
  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VECr 17]: nat: nat66 cli bug fix

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VECr 16]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node

session: **Florin Coras** <fcoras@cisco.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 7]: vcl: ldp support SO_ORIGINAL_DST

tcp: **Florin Coras** <fcoras@cisco.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 7]: vcl: ldp support SO_ORIGINAL_DST

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VECr 1]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 15]: ethernet: run callbacks for subifs too when mac changes
  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VECr 30]: nat: nat44-ed get out2in workers failed for static mapping without port

udp: **Florin Coras** <fcoras@cisco.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 7]: vcl: ldp support SO_ORIGINAL_DST

vapi: **Ole Troan** <ot@cisco.com>
  | `38491 <https:////gerrit.fd.io/r/c/vpp/+/38491>`_ [VECr 25]: vppapigen: c++ vapi stream message codegen

vcl: **Florin Coras** <fcoras@cisco.com>
  | `38958 <https:////gerrit.fd.io/r/c/vpp/+/38958>`_ [VECr 7]: vcl: ldp support SO_ORIGINAL_DST
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 9]: misc: patch to test CI infra changes

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `36110 <https:////gerrit.fd.io/r/c/vpp/+/36110>`_ [VECr 7]: virtio: use fast-path for ethernet-input if possible

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38997 <https:////gerrit.fd.io/r/c/vpp/+/38997>`_ [VECr 0]: vnet: turn vnet_is_packet_traced into callback

vppapigen: **Ole Troan** <otroan@employees.org>
  | `39002 <https:////gerrit.fd.io/r/c/vpp/+/39002>`_ [VECr 0]: vppapigen: fix crash with autoendian arrays

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `37719 <https:////gerrit.fd.io/r/c/vpp/+/37719>`_ [VECr 10]: crypto: fix async frame memory crash if frame pool expanded when using

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [veC 133]: wireguard: move buffer when insufficient pre_data left
  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [Vec 179]: arp: fix arp request for ip4-glean node

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [vEC 15]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [vEC 25]: TEST: remove the rdma mappings
  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 73]: TEST: make test string a test crash, for testing
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VeC 85]: fateshare: a plugin for managing child processes

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 172]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VeC 31]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

**Damjan Marion** <dmarion@0xa5.net>:

  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [VEc 9]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 95]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37836 <https:////gerrit.fd.io/r/c/vpp/+/37836>`_ [VEc 3]: dpdk-cryptodev: enq/deq scheme rework
  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [VEc 9]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 95]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `39021 <https:////gerrit.fd.io/r/c/vpp/+/39021>`_ [vEC 0]: tests: save api trace for testcases in json format

**Dmitry Valter** <dvalter@protonmail.com>:

  | `38082 <https:////gerrit.fd.io/r/c/vpp/+/38082>`_ [VeC 129]: lb: fix flow table update vector handing with ASAN
  | `38071 <https:////gerrit.fd.io/r/c/vpp/+/38071>`_ [veC 130]: vppinfra: fix preallocated pool_put OOB with ASAN
  | `38070 <https:////gerrit.fd.io/r/c/vpp/+/38070>`_ [veC 130]: lb: fix flow table update vector handing with ASAN
  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VeC 133]: stats: fix node name compatison

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 52]: dpdk: use adapter MTU in max_frame_size setting

**GaoChX** <chiso.gao@gmail.com>:

  | `37010 <https:////gerrit.fd.io/r/c/vpp/+/37010>`_ [VeC 150]: interface: fix crash if vnet_hw_if_get_rx_queue return zero

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VeC 105]: ip: fix update checksum in ip4_ttl_inc

**Huawei LI** <lihuawei_zzu@163.com>:

  | `37727 <https:////gerrit.fd.io/r/c/vpp/+/37727>`_ [Vec 177]: nat: make nat44 session limit api reinit flow_hash with new buckets.

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 85]: nat: fix address resolution

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [Vec 116]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Maxime Peim** <mpeim@cisco.com>:

  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VEc 8]: ipsec: huge anti-replay window support
  | `38528 <https:////gerrit.fd.io/r/c/vpp/+/38528>`_ [VeC 71]: ipsec: manually binding an SA to a worker
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VeC 140]: classify: bypass drop filter on specific error

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 70]: nat: fix tcp session reopen in nat44-ed

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 67]: cnat: remove rwlock on ts
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [VeC 67]: cnat: dont compute offloaded cksums
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 67]: cnat: flag to disable rsession
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 67]: cnat: add ip/client bihash
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 95]: vppinfra: improve & test abstract socket

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [vEc 21]: ip: IP address family common input node
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VeC 106]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 106]: ip: IPv6 validate input packet's header length does not exist buffer size

**Ondrej Fabry** <ondrej@fabry.dev>:

  | `38654 <https:////gerrit.fd.io/r/c/vpp/+/38654>`_ [VeC 35]: api: Mark old message versions as deprecated
  | `38639 <https:////gerrit.fd.io/r/c/vpp/+/38639>`_ [VeC 43]: api: Mark old message versions as deprecated
  | `38643 <https:////gerrit.fd.io/r/c/vpp/+/38643>`_ [VeC 43]: api: Mark old message versions as deprecated
  | `38644 <https:////gerrit.fd.io/r/c/vpp/+/38644>`_ [VeC 43]: api: Mark old message versions as deprecated
  | `38648 <https:////gerrit.fd.io/r/c/vpp/+/38648>`_ [VeC 43]: api: Mark old message versions as deprecated
  | `38646 <https:////gerrit.fd.io/r/c/vpp/+/38646>`_ [VeC 43]: api: Mark old message versions as deprecated
  | `38650 <https:////gerrit.fd.io/r/c/vpp/+/38650>`_ [VeC 43]: api: Mark old message versions as deprecated
  | `38649 <https:////gerrit.fd.io/r/c/vpp/+/38649>`_ [VeC 43]: api: Mark old message versions as deprecated
  | `38651 <https:////gerrit.fd.io/r/c/vpp/+/38651>`_ [VeC 43]: api: Mark old message versions as deprecated
  | `38641 <https:////gerrit.fd.io/r/c/vpp/+/38641>`_ [VeC 56]: api: Mark old message versions as deprecated

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [VEc 30]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38408 <https:////gerrit.fd.io/r/c/vpp/+/38408>`_ [VeC 93]: ipsec: fix logic in ext_hdr_is_pre_esp
  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [VeC 93]: ipsec: intorduce function esp_prepare_packet_for_enc
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VeC 93]: ipsec: esp_encrypt prefetch and unroll

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [veC 71]: gtpu: support non-G-PDU packets and PDU Session

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 39]: linux-cp: auto select tap id when creating lcp pair

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [Vec 44]: srv6-mobile: Implement SRv6 mobile API funcs

**Ting Xu** <ting.xu@intel.com>:

  | `38708 <https:////gerrit.fd.io/r/c/vpp/+/38708>`_ [VEc 16]: idpf: add native idpf driver plugin

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [Vec 57]: mpls: fix possible crashes on tunnel create/delete
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 70]: nat: fix nat44_ed set_session_limit crash
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VeC 70]: nat: improve nat44-ed outside address distribution
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VeC 81]: api: fix mp-safe mark for some messages and add more
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 83]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VeC 83]: fib: fix freed mpls label disposition dpo access

**Vratko Polak** <vrpolak@cisco.com>:

  | `22575 <https:////gerrit.fd.io/r/c/vpp/+/22575>`_ [Vec 144]: api: fix vl_socket_write_ready

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38733 <https:////gerrit.fd.io/r/c/vpp/+/38733>`_ [VeC 37]: ipsec: improve fast path policy searching performance
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 42]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 44]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VeC 79]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VeC 84]: ipsec: missing linear search when flow cache search failed
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 95]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [Vec 105]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VeC 106]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VeC 119]: misc: fix feature dispatch possible crashed when feature config changed by user
  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [Vec 142]: api: fix api msg thread safe setting not work

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 50]: af_xdp: optimizing send performance
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VeC 107]: tap: add interface type check

**Yulong Pei** <yulong.pei@intel.com>:

  | `38135 <https:////gerrit.fd.io/r/c/vpp/+/38135>`_ [vec 67]: af_xdp: change default queue size as kernel xsk default

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vEC 15]: vrrp: dump vrrp vr peer

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 70]: nat: add local addresses correctly in nat lb static mapping

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
authors          76
maintainers      30
committers       0
abandoned        0
================ ===

