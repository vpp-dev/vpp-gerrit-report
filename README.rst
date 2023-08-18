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
generated on Friday 2023-08-18, 01:54:03
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

adl: **Dave Barach** <vpp@barachs.net>
  | `39140 <https:////gerrit.fd.io/r/c/vpp/+/39140>`_ [VECr 16]: adl: stabilize the API

api: **Dave Barach** <vpp@barachs.net>
  | `39021 <https:////gerrit.fd.io/r/c/vpp/+/39021>`_ [VECr 9]: tests: save api trace for testcases in json format

avf: **Damjan Marion** <damarion@cisco.com>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 14]: interface dpdk avf: introducing setting RSS hash key feature

build: **Damjan Marion** <damarion@cisco.com>
  | `39198 <https:////gerrit.fd.io/r/c/vpp/+/39198>`_ [VECr 1]: dpdk: fix variable type in pattern parsing
  | `39353 <https:////gerrit.fd.io/r/c/vpp/+/39353>`_ [VECr 1]: build: add multi-arch support for Neoverse N2 CPU
  | `39224 <https:////gerrit.fd.io/r/c/vpp/+/39224>`_ [VECr 8]: crypto-ipsecmb: bump intel-ipsec-mb version to 1.4
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 21]: fateshare: a plugin for managing child processes

crypto-ipsecmb: **Neale Ranns** <neale@graphiant.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39224 <https:////gerrit.fd.io/r/c/vpp/+/39224>`_ [VECr 8]: crypto-ipsecmb: bump intel-ipsec-mb version to 1.4

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VECr 2]: dhcp: fix dhcp multiple client request

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `39213 <https:////gerrit.fd.io/r/c/vpp/+/39213>`_ [VECr 3]: tracenode: filtering feature
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 21]: fateshare: a plugin for managing child processes

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 14]: interface dpdk avf: introducing setting RSS hash key feature
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 17]: dpdk: create and remove interface in runtime

dpdk-cryptodev: **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39346 <https:////gerrit.fd.io/r/c/vpp/+/39346>`_ [VECr 6]: dpdk-cryptodev: improve cryptodev cache ring implementation

flow: **Damjan Marion** <damarion@cisco.com>
  | `39143 <https:////gerrit.fd.io/r/c/vpp/+/39143>`_ [VECr 16]: flow: mark API as production

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 24]: ipsec: huge anti-replay window support

interface: **Dave Barach** <vpp@barachs.net>
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 14]: interface dpdk avf: introducing setting RSS hash key feature
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 16]: interface: check sw_if_index more thoroughly

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 13]: ip-neighbor: add version 3 of neighbor event

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VECr 1]: ip6: ECMP hash support for ipv6 fragments
  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VECr 9]: ip: flow hash ignore tcp/udp ports when fragmented

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VECr 3]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 3]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 24]: ipsec: huge anti-replay window support
  | `38733 <https:////gerrit.fd.io/r/c/vpp/+/38733>`_ [VECr 30]: ipsec: improve fast path policy searching performance

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VECr 10]: libmemif: fix segfault and buffer overflow in examples

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VECr 14]: linux-cp: Fix update on IPv4 routes

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39370 <https:////gerrit.fd.io/r/c/vpp/+/39370>`_ [VECr 0]: crypto-sw-scheduler: improve function indentation
  | `39213 <https:////gerrit.fd.io/r/c/vpp/+/39213>`_ [VECr 3]: tracenode: filtering feature
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 14]: interface dpdk avf: introducing setting RSS hash key feature
  | `39141 <https:////gerrit.fd.io/r/c/vpp/+/39141>`_ [VECr 16]: crypto-sw-scheduler: stabilize the API
  | `35638 <https:////gerrit.fd.io/r/c/vpp/+/35638>`_ [VECr 21]: fateshare: a plugin for managing child processes
  | `39241 <https:////gerrit.fd.io/r/c/vpp/+/39241>`_ [VECr 27]: nsh: Fix plugin loading

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 0]: nat: fix nat44_ed set_session_limit crash

nsh: **Hongjun Ni** <hongjun.ni@intel.com>, **Vengada** <venggovi@cisco.com>
  | `39241 <https:////gerrit.fd.io/r/c/vpp/+/39241>`_ [VECr 27]: nsh: Fix plugin loading

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `39367 <https:////gerrit.fd.io/r/c/vpp/+/39367>`_ [VECr 3]: sr: SRv6 Path Tracing midpoint processing performance improvement
  | `39144 <https:////gerrit.fd.io/r/c/vpp/+/39144>`_ [VECr 16]: sr: mark sr_policies_v2_details message as production
  | `39257 <https:////gerrit.fd.io/r/c/vpp/+/39257>`_ [VECr 24]: sr: SRv6 Path Tracing source behavior

srv6-mobile: **Tetsuya Murakami** <tetsuya.mrk@gmail.com>, **Satoru Matsushima** <satoru.matsushima@gmail.com>
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 22]: srv6-mobile: Implement SRv6 mobile API funcs

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39395 <https:////gerrit.fd.io/r/c/vpp/+/39395>`_ [VECr 0]: tests: more descriptive error message
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 0]: nat: fix nat44_ed set_session_limit crash
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 3]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `39304 <https:////gerrit.fd.io/r/c/vpp/+/39304>`_ [VECr 3]: map: test fix feature disabling
  | `39213 <https:////gerrit.fd.io/r/c/vpp/+/39213>`_ [VECr 3]: tracenode: filtering feature
  | `39021 <https:////gerrit.fd.io/r/c/vpp/+/39021>`_ [VECr 9]: tests: save api trace for testcases in json format
  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VECr 9]: ip: flow hash ignore tcp/udp ports when fragmented
  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VECr 10]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VECr 10]: tests: memif ethernet type interface tests
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 13]: ip-neighbor: add version 3 of neighbor event
  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VECr 22]: srv6-mobile: Implement SRv6 mobile API funcs
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 24]: ipsec: huge anti-replay window support

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 24]: ipsec: huge anti-replay window support

vapi: **Ole Troan** <ot@cisco.com>
  | `38491 <https:////gerrit.fd.io/r/c/vpp/+/38491>`_ [VECr 9]: vapi: support services
  | `39343 <https:////gerrit.fd.io/r/c/vpp/+/39343>`_ [VECr 9]: vapi: improve vl_api_string_t handling
  | `39292 <https:////gerrit.fd.io/r/c/vpp/+/39292>`_ [VECr 17]: vapi: fix verification for reply message

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 2]: misc: patch to test CI infra changes

vppapigen: **Ole Troan** <otroan@employees.org>
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VECr 14]: vppapigen: recognize also _event as to_network

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `39353 <https:////gerrit.fd.io/r/c/vpp/+/39353>`_ [VECr 1]: build: add multi-arch support for Neoverse N2 CPU
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 24]: ipsec: huge anti-replay window support

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39142 <https:////gerrit.fd.io/r/c/vpp/+/39142>`_ [VECr 16]: wireguard: stabilize the API

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [vEC 20]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [vEC 20]: api trace: the api trace info about barrier is opposite

**Alexander Chernavin** <achernavin@netgate.com>:

  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VeC 35]: ethernet: run callbacks for subifs too when mac changes

**Alexander Kozyrev** <akozyrev@mellanox.com>:

  | `39133 <https:////gerrit.fd.io/r/c/vpp/+/39133>`_ [vEC 21]: dpdk: add Mellanox ConnectX-7 support

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [vEc 29]: arp: fix arp request for ip4-glean node

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38794 <https:////gerrit.fd.io/r/c/vpp/+/38794>`_ [veC 64]: TEST: remove IKEv2 tests
  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [veC 84]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [veC 94]: TEST: remove the rdma mappings
  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 142]: TEST: make test string a test crash, for testing

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 9]: ip: add support for buffer offload metadata in ip midchain

**Damjan Marion** <dmarion@0xa5.net>:

  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [vEC 10]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 78]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 90]: libmemif: added tests
  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 164]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 78]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 164]: ipsec: esp_encrypt prefetch and unroll

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 121]: dpdk: use adapter MTU in max_frame_size setting

**Filip Varga** <fivarga@cisco.com>:

  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 86]: nat: nat66 cli bug fix

**Florian Gavril** <gflorian@3nets.io>:

  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VeC 59]: fib: Crash when specify a big prefix length from CLI.

**GaoChX** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 99]: nat: nat44-ed get out2in workers failed for static mapping without port

**Guangming Zhang** <zhangguangming@baicells.com>:

  | `38285 <https:////gerrit.fd.io/r/c/vpp/+/38285>`_ [VeC 174]: ip: fix update checksum in ip4_ttl_inc

**Hedi Bouattour** <hedibouattour2010@gmail.com>:

  | `39387 <https:////gerrit.fd.io/r/c/vpp/+/39387>`_ [VEc 0]: cnat: add host tag to bitmap in cnat snat

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [VEc 21]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 154]: nat: fix address resolution

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 139]: nat: fix tcp session reopen in nat44-ed

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [vec 90]: ip: IP address family common input node
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [VeC 175]: ip: Set the buffer error in ip6-input
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 175]: ip: IPv6 validate input packet's header length does not exist buffer size

**Ole Troan** <otroan@employees.org>:

  | `39393 <https:////gerrit.fd.io/r/c/vpp/+/39393>`_ [vEc 0]: npt66: network prefix translation for ipv6

**Pim van Pelt** <pim@ipng.nl>:

  | `39022 <https:////gerrit.fd.io/r/c/vpp/+/39022>`_ [VeC 65]: mpls: add mpls_interface_dump

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [vEC 22]: ipsec: introduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 99]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VeC 162]: ipsec: esp_encrypt prefetch and unroll

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [vEC 6]: gtpu: support non-G-PDU packets and PDU Session

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 85]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 108]: linux-cp: auto select tap id when creating lcp pair

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [vEC 20]: api: ip - set punt reason max length to fix VAPI generation

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 63]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [Vec 126]: mpls: fix possible crashes on tunnel create/delete
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VeC 139]: nat: improve nat44-ed outside address distribution
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VeC 150]: api: fix mp-safe mark for some messages and add more
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 152]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VeC 152]: fib: fix freed mpls label disposition dpo access

**Vratko Polak** <vrpolak@cisco.com>:

  | `39386 <https:////gerrit.fd.io/r/c/vpp/+/39386>`_ [vEC 0]: crypto: allow changing dispatch mode
  | `39214 <https:////gerrit.fd.io/r/c/vpp/+/39214>`_ [VeC 34]: l2: fix prefetch
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VeC 87]: ip: make running_fragment_id thread safe

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 85]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 111]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 113]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VeC 148]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VeC 153]: ipsec: missing linear search when flow cache search failed
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 164]: api: fix memory error with pending_rpc_requests in multi-thread environment
  | `38336 <https:////gerrit.fd.io/r/c/vpp/+/38336>`_ [Vec 174]: ip: IPv4 Fragmentation - fix fragment id alloc not multi-thread safe
  | `36018 <https:////gerrit.fd.io/r/c/vpp/+/36018>`_ [VeC 175]: ip: fix ip4_ttl_inc calc checksum error when checksum is 0

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VeC 73]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 84]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VEc 1]: af_xdp: optimizing send performance
  | `38312 <https:////gerrit.fd.io/r/c/vpp/+/38312>`_ [VeC 176]: tap: add interface type check

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 32]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VeC 32]: ipsec: delete redundant code

**grimlock** <realbaseball2008@gmail.com>:

  | `38442 <https:////gerrit.fd.io/r/c/vpp/+/38442>`_ [VeC 78]: nat: nat44-ed bug fix
  | `38440 <https:////gerrit.fd.io/r/c/vpp/+/38440>`_ [VeC 80]: nat: nat44-ed cli bug fix

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [veC 84]: vrrp: dump vrrp vr peer

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 139]: nat: add local addresses correctly in nat lb static mapping

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [Vec 48]: ipsec: separate UDP and UDP-encapsulated ESP packet processing
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VeC 56]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process

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
authors          66
maintainers      40
committers       0
abandoned        0
================ ===

