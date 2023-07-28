
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Friday 2023-07-28, 02:09:10
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
  | `39021 <https:////gerrit.fd.io/r/c/vpp/+/39021>`_ [VECr 3]: tests: save api trace for testcases in json format

build: **Damjan Marion** <damarion@cisco.com>
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 0]: fateshare: a plugin for managing child processes
  | `39224 <https:////gerrit.fd.io/r/c/vpp/+/39224>`_ [VECr 3]: crypto-ipsecmb: bump intel-ipsec-mb version to 1.4
  | `39198 <https:////gerrit.fd.io/r/c/vpp/+/39198>`_ [VECr 23]: dpdk: fix variable type in pattern parsing

classify: **Dave Barach** <vpp@barachs.net>
  | `39213 <https:////gerrit.fd.io/r/c/vpp/+/39213>`_ [VECr 0]: classify: filtering node

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 0]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

crypto-ipsecmb: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39224 <https:////gerrit.fd.io/r/c/vpp/+/39224>`_ [VECr 3]: crypto-ipsecmb: bump intel-ipsec-mb version to 1.4

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 0]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 0]: fateshare: a plugin for managing child processes
  | `39271 <https:////gerrit.fd.io/r/c/vpp/+/39271>`_ [VECr 1]: docs:Improve the compilation process description of vpp docs

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 14]: ethernet: run callbacks for subifs too when mac changes

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `39157 <https:////gerrit.fd.io/r/c/vpp/+/39157>`_ [VECr 29]: hs-test: improve get stats

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 3]: ipsec: huge anti-replay window support

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 0]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 3]: ipsec: huge anti-replay window support
  | `38733 <https:////gerrit.fd.io/r/c/vpp/+/38733>`_ [VECr 9]: ipsec: improve fast path policy searching performance
  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VECr 11]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VECr 11]: ipsec: delete redundant code

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `39214 <https:////gerrit.fd.io/r/c/vpp/+/39214>`_ [VECr 13]: l2: fix prefetch

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `39139 <https:////gerrit.fd.io/r/c/vpp/+/39139>`_ [VECr 0]: libmemif: add support for buffer size
  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VECr 2]: libmemif: fix segfault and buffer overflow in examples

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VECr 15]: linux-cp: Fix update on IPv4 routes

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 0]: fateshare: a plugin for managing child processes
  | `39213 <https:////gerrit.fd.io/r/c/vpp/+/39213>`_ [VECr 0]: classify: filtering node
  | `39241 <https:////gerrit.fd.io/r/c/vpp/+/39241>`_ [VECr 6]: nsh: Fix plugin loading

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `39241 <https:////gerrit.fd.io/r/c/vpp/+/39241>`_ [VECr 6]: nsh: Fix plugin loading

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `39257 <https:////gerrit.fd.io/r/c/vpp/+/39257>`_ [VECr 3]: sr: SRv6 Path Tracing source behavior

srv6-mobile: **Tetsuya Murakami** <tetsuya.mrk@gmail.com>, **Satoru Matsushima** <satoru.matsushima@gmail.com>
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 1]: srv6-mobile: Implement SRv6 mobile API funcs

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 0]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `39213 <https:////gerrit.fd.io/r/c/vpp/+/39213>`_ [VECr 0]: classify: filtering node
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 1]: srv6-mobile: Implement SRv6 mobile API funcs
  | `39021 <https:////gerrit.fd.io/r/c/vpp/+/39021>`_ [VECr 3]: tests: save api trace for testcases in json format
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 3]: ipsec: huge anti-replay window support
  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VECr 8]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 14]: ethernet: run callbacks for subifs too when mac changes

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 0]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 3]: ipsec: huge anti-replay window support

vcl: **Florin Coras** <fcoras@cisco.com>
  | `39242 <https:////gerrit.fd.io/r/c/vpp/+/39242>`_ [VECr 1]: vcl: Fix the ldp init check
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 6]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39277 <https:////gerrit.fd.io/r/c/vpp/+/39277>`_ [VECr 0]: vppinfra: silence GCC 11 -Wmaybe-uinitialized warning

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 3]: ipsec: huge anti-replay window support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `37066 <https:////gerrit.fd.io/r/c/vpp/+/37066>`_ [vEC 0]: api trace data about is_mp_safe is opposite，when is_mp_safe is 1, the ed->barrier is 0, so enum_strings[0] shoud be "mp-safe".

**Alexander Kozyrev** <akozyrev@mellanox.com>:

  | `39133 <https:////gerrit.fd.io/r/c/vpp/+/39133>`_ [vEC 0]: dpdk: add Mellanox ConnectX-7 support

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [vEc 8]: arp: fix arp request for ip4-glean node

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `39138 <https:////gerrit.fd.io/r/c/vpp/+/39138>`_ [vEC 0]: ikev2: init uninitialized values
  | `38794 <https:////gerrit.fd.io/r/c/vpp/+/38794>`_ [veC 43]: TEST: remove IKEv2 tests
  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [veC 63]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [veC 73]: TEST: remove the rdma mappings
  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 121]: TEST: make test string a test crash, for testing

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VEc 0]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 37]: ip: add support for buffer offload metadata in ip midchain

**Damjan Marion** <dmarion@0xa5.net>:

  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [vEC 20]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 57]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 69]: libmemif: added tests
  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 143]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 57]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 143]: ipsec: esp_encrypt prefetch and unroll

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 100]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <fivarga@cisco.com>:

  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 65]: nat: nat66 cli bug fix

**Florian Gavril** <gflorian@3nets.io>:

  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VeC 38]: fib: Crash when specify a big prefix length from CLI.

**GaoChX** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 78]: nat: nat44-ed get out2in workers failed for static mapping without port

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VeC 153]: ip: fix update checksum in ip4_ttl_inc

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [VEc 0]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 133]: nat: fix address resolution

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [Vec 164]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 118]: nat: fix tcp session reopen in nat44-ed

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 115]: cnat: remove rwlock on ts
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [VeC 115]: cnat: dont compute offloaded cksums
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 115]: cnat: flag to disable rsession
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 115]: cnat: add ip/client bihash
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 143]: vppinfra: improve & test abstract socket

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [vec 69]: ip: IP address family common input node
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VeC 154]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 154]: ip: IPv6 validate input packet's header length does not exist buffer size

**Pim van Pelt** <pim@ipng.nl>:

  | `39022 <https:////gerrit.fd.io/r/c/vpp/+/39022>`_ [VeC 44]: mpls: add mpls_interface_dump

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [vEC 1]: ipsec: introduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 78]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VeC 141]: ipsec: esp_encrypt prefetch and unroll

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [veC 119]: gtpu: support non-G-PDU packets and PDU Session

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 64]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 35]: dpdk: create and remove interface in runtime
  | `38491 <https:////gerrit.fd.io/r/c/vpp/+/38491>`_ [VeC 37]: vppapigen: c++ vapi stream message codegen
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 87]: linux-cp: auto select tap id when creating lcp pair

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 42]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Ting Xu** <ting.xu@intel.com>:

  | `38708 <https:////gerrit.fd.io/r/c/vpp/+/38708>`_ [Vec 64]: idpf: add native idpf driver plugin

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [Vec 105]: mpls: fix possible crashes on tunnel create/delete
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 118]: nat: fix nat44_ed set_session_limit crash
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VeC 118]: nat: improve nat44-ed outside address distribution
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VeC 129]: api: fix mp-safe mark for some messages and add more
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 131]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VeC 131]: fib: fix freed mpls label disposition dpo access

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VeC 66]: ip: make running_fragment_id thread safe

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 64]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 90]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 92]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VeC 127]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VeC 132]: ipsec: missing linear search when flow cache search failed
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 143]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [Vec 153]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VeC 154]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VeC 167]: misc: fix feature dispatch possible crashed when feature config changed by user

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VeC 52]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 52]: interface dpdk avf: introducing setting RSS hash key feature
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 63]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 98]: af_xdp: optimizing send performance
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VeC 155]: tap: add interface type check

**grimlock** <realbaseball2008@gmail.com>:

  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VeC 57]: nat: nat44-ed bug fix
  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VeC 59]: nat: nat44-ed cli bug fix

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [veC 63]: vrrp: dump vrrp vr peer

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 118]: nat: add local addresses correctly in nat lb static mapping

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [VEc 27]: ipsec: separate UDP and UDP-encapsulated ESP packet processing
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VeC 35]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process

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
authors          71
maintainers      24
committers       0
abandoned        0
================ ===

