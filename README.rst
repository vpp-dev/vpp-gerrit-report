#################
VPP-GERRIT-REPORT
#################

VPP Gerrit Report categorizes the state of the gerrit.fd.io review queue.  Each gerrit change is labeled with the following status:

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
    - No unresolved comments
    - Review incomplete (Code-Review < +1)
    - 23 days since last update

The report generator sorts the gerrit changes into three categories based on the state and the person or group required to perform the next action:

- Committers:
  Status [VECR xx]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & approved by a maintainer.
  Action: A committer should do a final review and submit the change or provide comment(s).

- Maintainers:
  Status [VECr]: Gerrit Changes that have been verified, are not expired, no unresolved comments, & not reviewed
  Action: The Maintainer should do a code review

- Authors:
  Status <other>: Gerrit Changes that are either not verified, expired, or comments not resolved
  Action: Author should rebase the change, fix verification errors, and/or resolve comments to move the status to [VECr]# Gerrit open patches processing tool

Here is the latest VPP Gerrit Report:
-------------------------------------

==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Tuesday 2023-07-18, 02:43:40
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

build: **Damjan Marion** <damarion@cisco.com>
  | `39224 <https:////gerrit.fd.io/r/c/vpp/+/39224>`_ [VECr 0]: crypto-ipsecmb: bump intel-ipsec-mb version to 1.4
  | `39198 <https:////gerrit.fd.io/r/c/vpp/+/39198>`_ [VECr 13]: dpdk: fix variable type in pattern parsing
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 13]: fateshare: a plugin for managing child processes

classify: **Dave Barach** <vpp@barachs.net>
  | `39196 <https:////gerrit.fd.io/r/c/vpp/+/39196>`_ [VECr 7]: classify: add bpf support to pcap classifier

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 17]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

crypto-ipsecmb: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39224 <https:////gerrit.fd.io/r/c/vpp/+/39224>`_ [VECr 0]: crypto-ipsecmb: bump intel-ipsec-mb version to 1.4

crypto-openssl: **Damjan Marion** <damarion@cisco.com>
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 17]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `39205 <https:////gerrit.fd.io/r/c/vpp/+/39205>`_ [VECr 0]: docs: add api change process from wiki
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 13]: fateshare: a plugin for managing child processes

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39208 <https:////gerrit.fd.io/r/c/vpp/+/39208>`_ [VECr 10]: dpdk: fix signed single bit field
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 25]: dpdk: create and remove interface in runtime

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 4]: ethernet: run callbacks for subifs too when mac changes

fib: **Neale Ranns** <neale@graphiant.com>
  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VECr 28]: fib: Crash when specify a big prefix length from CLI.

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `39157 <https:////gerrit.fd.io/r/c/vpp/+/39157>`_ [VECr 19]: hs-test: improve get stats

interface: **Dave Barach** <vpp@barachs.net>
  | `39196 <https:////gerrit.fd.io/r/c/vpp/+/39196>`_ [VECr 7]: classify: add bpf support to pcap classifier

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VECr 28]: fib: Crash when specify a big prefix length from CLI.

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VECr 1]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VECr 1]: ipsec: delete redundant code
  | `38733 <https:////gerrit.fd.io/r/c/vpp/+/38733>`_ [VECr 1]: ipsec: improve fast path policy searching performance
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 10]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `39174 <https:////gerrit.fd.io/r/c/vpp/+/39174>`_ [VECr 14]: ipsec: fix sa bind cli
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 17]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VECr 25]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `39214 <https:////gerrit.fd.io/r/c/vpp/+/39214>`_ [VECr 4]: l2: fix prefetch

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VECr 5]: linux-cp: Fix update on IPv4 routes

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39241 <https:////gerrit.fd.io/r/c/vpp/+/39241>`_ [VECr 0]: nsh: Fix plugin loading
  | `39196 <https:////gerrit.fd.io/r/c/vpp/+/39196>`_ [VECr 7]: classify: add bpf support to pcap classifier
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 13]: fateshare: a plugin for managing child processes

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `39131 <https:////gerrit.fd.io/r/c/vpp/+/39131>`_ [VECr 4]: vcl: ldp support SO_ORIGINAL_DST

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `39241 <https:////gerrit.fd.io/r/c/vpp/+/39241>`_ [VECr 0]: nsh: Fix plugin loading

session: **Florin Coras** <fcoras@cisco.com>
  | `39131 <https:////gerrit.fd.io/r/c/vpp/+/39131>`_ [VECr 4]: vcl: ldp support SO_ORIGINAL_DST
  | `39158 <https:////gerrit.fd.io/r/c/vpp/+/39158>`_ [VECr 6]: session: use session error type instead of vnet error

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 4]: ethernet: run callbacks for subifs too when mac changes
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 10]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VECr 14]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 17]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC
  | `39134 <https:////gerrit.fd.io/r/c/vpp/+/39134>`_ [VECr 20]: tests: Add checksum offload interface tests

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `39158 <https:////gerrit.fd.io/r/c/vpp/+/39158>`_ [VECr 6]: session: use session error type instead of vnet error
  | `38470 <https:////gerrit.fd.io/r/c/vpp/+/38470>`_ [VECr 17]: ipsec: add support for RFC-4543 ENCR_NULL_AUTH_AES_GMAC

vapi: **Ole Troan** <ot@cisco.com>
  | `38491 <https:////gerrit.fd.io/r/c/vpp/+/38491>`_ [VECr 27]: vppapigen: c++ vapi stream message codegen

vcl: **Florin Coras** <fcoras@cisco.com>
  | `39242 <https:////gerrit.fd.io/r/c/vpp/+/39242>`_ [VECr 0]: vcl: Fix the ldp init check
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 0]: misc: patch to test CI infra changes
  | `39131 <https:////gerrit.fd.io/r/c/vpp/+/39131>`_ [VECr 4]: vcl: ldp support SO_ORIGINAL_DST

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39196 <https:////gerrit.fd.io/r/c/vpp/+/39196>`_ [VECr 7]: classify: add bpf support to pcap classifier

vpp-swan: **Fan Zhang** <roy.fan.zhang@intel.com>, **Gabriel Oginski** <gabrielx.oginski@intel.com>
  | `39215 <https:////gerrit.fd.io/r/c/vpp/+/39215>`_ [VECr 0]: vpp-swan: fix handler API messages
  | `39203 <https:////gerrit.fd.io/r/c/vpp/+/39203>`_ [VECr 6]: vpp-swan: fix incorrect msg ID in register_event
  | `39204 <https:////gerrit.fd.io/r/c/vpp/+/39204>`_ [VECr 6]: vpp-swan: fix function to get sw_if_index

vppapigen: **Ole Troan** <otroan@employees.org>
  | `39205 <https:////gerrit.fd.io/r/c/vpp/+/39205>`_ [VECr 0]: docs: add api change process from wiki

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

**Alexander Kozyrev** <akozyrev@mellanox.com>:

  | `39133 <https:////gerrit.fd.io/r/c/vpp/+/39133>`_ [vEC 20]: dpdk: add Mellanox ConnectX-7 support

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `38011 <https:////gerrit.fd.io/r/c/vpp/+/38011>`_ [veC 171]: wireguard: move buffer when insufficient pre_data left

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38794 <https:////gerrit.fd.io/r/c/vpp/+/38794>`_ [veC 33]: TEST: remove IKEv2 tests
  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [veC 53]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [veC 63]: TEST: remove the rdma mappings
  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 111]: TEST: make test string a test crash, for testing

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 27]: ip: add support for buffer offload metadata in ip midchain

**Damjan Marion** <dmarion@0xa5.net>:

  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [vEC 10]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 47]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 59]: libmemif: added tests
  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 133]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 47]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 133]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `39021 <https:////gerrit.fd.io/r/c/vpp/+/39021>`_ [vEC 7]: tests: save api trace for testcases in json format

**Dmitry Valter** <dvalter@protonmail.com>:

  | `38062 <https:////gerrit.fd.io/r/c/vpp/+/38062>`_ [VeC 171]: stats: fix node name compatison

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 90]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <fivarga@cisco.com>:

  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 55]: nat: nat66 cli bug fix

**GaoChX** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 68]: nat: nat44-ed get out2in workers failed for static mapping without port

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VeC 143]: ip: fix update checksum in ip4_ttl_inc

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [VEc 7]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 123]: nat: fix address resolution

**Matz von Finckenstein** <matz.vf@gmail.com>:

  | `38091 <https:////gerrit.fd.io/r/c/vpp/+/38091>`_ [Vec 154]: stats: Updated go version URL for the install script Added log flag to pass in logging file destination as an alternate logging destination from syslog

**Maxime Peim** <mpeim@cisco.com>:

  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [vEC 0]: ipsec: huge anti-replay window support
  | `37941 <https:////gerrit.fd.io/r/c/vpp/+/37941>`_ [VeC 178]: classify: bypass drop filter on specific error

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 108]: nat: fix tcp session reopen in nat44-ed

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `29748 <https:////gerrit.fd.io/r/c/vpp/+/29748>`_ [VeC 105]: cnat: remove rwlock on ts
  | `31449 <https:////gerrit.fd.io/r/c/vpp/+/31449>`_ [VeC 105]: cnat: dont compute offloaded cksums
  | `34108 <https:////gerrit.fd.io/r/c/vpp/+/34108>`_ [VeC 105]: cnat: flag to disable rsession
  | `32821 <https:////gerrit.fd.io/r/c/vpp/+/32821>`_ [VeC 105]: cnat: add ip/client bihash
  | `34713 <https:////gerrit.fd.io/r/c/vpp/+/34713>`_ [VeC 133]: vppinfra: improve & test abstract socket

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [vec 59]: ip: IP address family common input node
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VeC 144]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 144]: ip: IPv6 validate input packet's header length does not exist buffer size

**Pim van Pelt** <pim@ipng.nl>:

  | `39022 <https:////gerrit.fd.io/r/c/vpp/+/39022>`_ [VeC 34]: mpls: add mpls_interface_dump

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 68]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38408 <https:////gerrit.fd.io/r/c/vpp/+/38408>`_ [VeC 131]: ipsec: fix logic in ext_hdr_is_pre_esp
  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [VeC 131]: ipsec: intorduce function esp_prepare_packet_for_enc
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VeC 131]: ipsec: esp_encrypt prefetch and unroll

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [veC 109]: gtpu: support non-G-PDU packets and PDU Session

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 54]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 77]: linux-cp: auto select tap id when creating lcp pair

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [Vec 82]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 32]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Ting Xu** <ting.xu@intel.com>:

  | `38708 <https:////gerrit.fd.io/r/c/vpp/+/38708>`_ [Vec 54]: idpf: add native idpf driver plugin

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [Vec 95]: mpls: fix possible crashes on tunnel create/delete
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VeC 108]: nat: fix nat44_ed set_session_limit crash
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VeC 108]: nat: improve nat44-ed outside address distribution
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VeC 119]: api: fix mp-safe mark for some messages and add more
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 121]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VeC 121]: fib: fix freed mpls label disposition dpo access

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VeC 56]: ip: make running_fragment_id thread safe

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 54]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 80]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 82]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VeC 117]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VeC 122]: ipsec: missing linear search when flow cache search failed
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 133]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [Vec 143]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VeC 144]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0
  | `38214 <https:////gerrit.fd.io/r/c/vpp/+/38214>`_ [VeC 157]: misc: fix feature dispatch possible crashed when feature config changed by user

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VeC 42]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 42]: interface dpdk avf: introducing setting RSS hash key feature
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 53]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 88]: af_xdp: optimizing send performance
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VeC 145]: tap: add interface type check

**Yulong Pei** <yulong.pei@intel.com>:

  | `38135 <https:////gerrit.fd.io/r/c/vpp/+/38135>`_ [vec 105]: af_xdp: change default queue size as kernel xsk default

**grimlock** <realbaseball2008@gmail.com>:

  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VeC 47]: nat: nat44-ed bug fix
  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VeC 49]: nat: nat44-ed cli bug fix

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [veC 53]: vrrp: dump vrrp vr peer

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 108]: nat: add local addresses correctly in nat lb static mapping

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [VEc 17]: ipsec: separate UDP and UDP-encapsulated ESP packet processing

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `37820 <https:////gerrit.fd.io/r/c/vpp/+/37820>`_ [A 180]: api: fix api msg thread safe setting not work

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
maintainers      30
committers       0
abandoned        1
================ ===

