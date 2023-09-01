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
generated on Friday 2023-09-01, 02:01:32
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
  | `39140 <https:////gerrit.fd.io/r/c/vpp/+/39140>`_ [VECr 30]: adl: stabilize the API

af_xdp: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 12]: ethernet: check dmacs_bad in the fastpath case

avf: **Damjan Marion** <damarion@cisco.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 12]: ethernet: check dmacs_bad in the fastpath case
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 28]: interface dpdk avf: introducing setting RSS hash key feature

build: **Damjan Marion** <damarion@cisco.com>
  | `39198 <https:////gerrit.fd.io/r/c/vpp/+/39198>`_ [VECr 15]: dpdk: fix variable type in pattern parsing
  | `39353 <https:////gerrit.fd.io/r/c/vpp/+/39353>`_ [VECr 15]: build: add multi-arch support for Neoverse N2 CPU

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `39386 <https:////gerrit.fd.io/r/c/vpp/+/39386>`_ [VECr 8]: crypto: allow changing dispatch mode

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VECr 16]: dhcp: fix dhcp multiple client request

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 12]: ethernet: check dmacs_bad in the fastpath case
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 28]: interface dpdk avf: introducing setting RSS hash key feature

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 9]: ethernet: run callbacks for subifs too when mac changes
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 12]: ethernet: check dmacs_bad in the fastpath case

flow: **Damjan Marion** <damarion@cisco.com>
  | `39143 <https:////gerrit.fd.io/r/c/vpp/+/39143>`_ [VECr 30]: flow: mark API as production

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 10]: ipsec: huge anti-replay window support

interface: **Dave Barach** <vpp@barachs.net>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 12]: ethernet: check dmacs_bad in the fastpath case
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 28]: interface dpdk avf: introducing setting RSS hash key feature
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 30]: interface: check sw_if_index more thoroughly

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 27]: ip-neighbor: add version 3 of neighbor event

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VECr 15]: ip6: ECMP hash support for ipv6 fragments
  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VECr 23]: ip: flow hash ignore tcp/udp ports when fragmented

ip6-nd: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VECr 17]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `38733 <https:////gerrit.fd.io/r/c/vpp/+/38733>`_ [VECr 10]: ipsec: improve fast path policy searching performance
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 10]: ipsec: huge anti-replay window support
  | `39238 <https:////gerrit.fd.io/r/c/vpp/+/39238>`_ [VECr 13]: ipsec: clear L4-cksum flags when decap'ing packets
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 17]: ipsec: allow receiving encrypted IP packets with TFC padding

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VECr 24]: libmemif: fix segfault and buffer overflow in examples

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 12]: ethernet: check dmacs_bad in the fastpath case
  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VECr 28]: linux-cp: Fix update on IPv4 routes

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39370 <https:////gerrit.fd.io/r/c/vpp/+/39370>`_ [VECr 10]: crypto-sw-scheduler: improve function indentation
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 28]: interface dpdk avf: introducing setting RSS hash key feature
  | `39141 <https:////gerrit.fd.io/r/c/vpp/+/39141>`_ [VECr 30]: crypto-sw-scheduler: stabilize the API

nat: **Ole Troan** <ot@cisco.com>, **Filip Varga** <fivarga@cisco.com>, **Klement Sekera** <klement.sekera@gmail.com>
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 14]: nat: fix nat44_ed set_session_limit crash

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 12]: ethernet: check dmacs_bad in the fastpath case

sr: **Pablo Camarillo** <pcamaril@cisco.com>, **Ahmed Abdelsalam** <ahabdels@cisco.com>
  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VECr 8]: sr: SRv6 Path Tracing source node behavior
  | `39144 <https:////gerrit.fd.io/r/c/vpp/+/39144>`_ [VECr 30]: sr: mark sr_policies_v2_details message as production

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `38860 <https:////gerrit.fd.io/r/c/vpp/+/38860>`_ [VECr 9]: ethernet: run callbacks for subifs too when mac changes
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 10]: ipsec: huge anti-replay window support
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 12]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VECr 13]: tests: fix issues found when enabling DMAC check
  | `37241 <https:////gerrit.fd.io/r/c/vpp/+/37241>`_ [VECr 14]: nat: fix nat44_ed set_session_limit crash
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VECr 17]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VECr 23]: ip: flow hash ignore tcp/udp ports when fragmented
  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VECr 24]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VECr 24]: tests: memif ethernet type interface tests
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 27]: ip-neighbor: add version 3 of neighbor event

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 10]: ipsec: huge anti-replay window support

vapi: **Ole Troan** <ot@cisco.com>
  | `39292 <https:////gerrit.fd.io/r/c/vpp/+/39292>`_ [VECr 9]: vapi: fix verification for reply message

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 0]: misc: patch to test CI infra changes

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 10]: ipsec: huge anti-replay window support
  | `39353 <https:////gerrit.fd.io/r/c/vpp/+/39353>`_ [VECr 15]: build: add multi-arch support for Neoverse N2 CPU

wireguard: **Artem Glazychev** <artem.glazychev@xored.com>, **Fan Zhang** <roy.fan.zhang@intel.com>
  | `39142 <https:////gerrit.fd.io/r/c/vpp/+/39142>`_ [VECr 30]: wireguard: stabilize the API

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 34]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 34]: api trace: the api trace info about barrier is opposite

**Alexander Kozyrev** <akozyrev@mellanox.com>:

  | `39133 <https:////gerrit.fd.io/r/c/vpp/+/39133>`_ [vEc 13]: dpdk: add Mellanox ConnectX-7 support

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `37656 <https:////gerrit.fd.io/r/c/vpp/+/37656>`_ [vEc 0]: arp: fix arp request for ip4-glean node
  | `39459 <https:////gerrit.fd.io/r/c/vpp/+/39459>`_ [vEC 0]: arp: fix arp request for ip4-glean node
  | `39241 <https:////gerrit.fd.io/r/c/vpp/+/39241>`_ [VeC 41]: nsh: Fix plugin loading

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38794 <https:////gerrit.fd.io/r/c/vpp/+/38794>`_ [veC 78]: TEST: remove IKEv2 tests
  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [veC 98]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [veC 108]: TEST: remove the rdma mappings
  | `38567 <https:////gerrit.fd.io/r/c/vpp/+/38567>`_ [veC 156]: TEST: make test string a test crash, for testing

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [VEc 23]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `39415 <https:////gerrit.fd.io/r/c/vpp/+/39415>`_ [vEC 0]: build: add vpp_plugins include directory

**Damjan Marion** <dmarion@0xa5.net>:

  | `39462 <https:////gerrit.fd.io/r/c/vpp/+/39462>`_ [vEC 0]: build: add option to specify native -march= flag with VPP_BUILD_NATIVE_ARCH
  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [vEC 24]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 92]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 104]: libmemif: added tests
  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 178]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 92]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm
  | `37060 <https:////gerrit.fd.io/r/c/vpp/+/37060>`_ [VeC 178]: ipsec: esp_encrypt prefetch and unroll

**Dave Wallace** <dwallacelf@gmail.com>:

  | `39411 <https:////gerrit.fd.io/r/c/vpp/+/39411>`_ [vEC 0]: hsa: fix coverity issue CID-313635
  | `39413 <https:////gerrit.fd.io/r/c/vpp/+/39413>`_ [vEC 2]: api: fix vlibmemory coverity warning CID-300152
  | `39412 <https:////gerrit.fd.io/r/c/vpp/+/39412>`_ [vEC 2]: vppinfra: fix coverity warning CID-313632
  | `39410 <https:////gerrit.fd.io/r/c/vpp/+/39410>`_ [vEC 2]: vapi: fix coverity warnings
  | `39409 <https:////gerrit.fd.io/r/c/vpp/+/39409>`_ [vEC 2]: pci: fix coverity issue CID-322372

**Dzmitry Sautsa** <dzmitry.sautsa@nokia.com>:

  | `37296 <https:////gerrit.fd.io/r/c/vpp/+/37296>`_ [VeC 135]: dpdk: use adapter MTU in max_frame_size setting

**Filip Tehlar** <ftehlar@cisco.com>:

  | `39461 <https:////gerrit.fd.io/r/c/vpp/+/39461>`_ [vEC 0]: hs-test: log external apps
  | `39460 <https:////gerrit.fd.io/r/c/vpp/+/39460>`_ [vEC 0]: hs-test: use capital letters for functions

**Filip Varga** <fivarga@cisco.com>:

  | `35903 <https:////gerrit.fd.io/r/c/vpp/+/35903>`_ [VeC 100]: nat: nat66 cli bug fix

**Florian Gavril** <gflorian@3nets.io>:

  | `39076 <https:////gerrit.fd.io/r/c/vpp/+/39076>`_ [VeC 73]: fib: Crash when specify a big prefix length from CLI.

**Florin Coras** <florin.coras@gmail.com>:

  | `39448 <https:////gerrit.fd.io/r/c/vpp/+/39448>`_ [vEC 0]: vcl: set min threshold for tx ntf
  | `39467 <https:////gerrit.fd.io/r/c/vpp/+/39467>`_ [vEC 0]: session: fix allocation of proxy fifos
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [vEC 0]: session: program rx events only if none are pending

**GaoChX** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 113]: nat: nat44-ed get out2in workers failed for static mapping without port

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 35]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 168]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39304 <https:////gerrit.fd.io/r/c/vpp/+/39304>`_ [vEC 0]: map: test fix feature disabling
  | `39213 <https:////gerrit.fd.io/r/c/vpp/+/39213>`_ [vEC 0]: tracenode: filtering feature

**Miklos Tirpak** <miklos.tirpak@gmail.com>:

  | `36021 <https:////gerrit.fd.io/r/c/vpp/+/36021>`_ [VeC 153]: nat: fix tcp session reopen in nat44-ed

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `36725 <https:////gerrit.fd.io/r/c/vpp/+/36725>`_ [VEc 0]: virtio: add support for tx-queue-size
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [vEC 0]: geneve: add support for layer 3

**Naveen Joy** <najoy@cisco.com>:

  | `39437 <https:////gerrit.fd.io/r/c/vpp/+/39437>`_ [vEC 0]: tests: remove unsupported qemu feature

**Neale Ranns** <neale@graphiant.com>:

  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [vEC 0]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [vEC 0]: ip: Set the buffer error in ip6-input
  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [vEC 0]: ip: IP address family common input node

**Ole Troan** <otroan@employees.org>:

  | `39458 <https:////gerrit.fd.io/r/c/vpp/+/39458>`_ [vEC 0]: arping: api to return responder mac address

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 36]: ipsec: introduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 113]: ipsec: esp_encrypt prefetch and unroll - introduce new types
  | `38410 <https:////gerrit.fd.io/r/c/vpp/+/38410>`_ [VeC 176]: ipsec: esp_encrypt prefetch and unroll

**Rune Jensen** <runeerle@wgtwo.com>:

  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [vEC 20]: gtpu: support non-G-PDU packets and PDU Session

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 99]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 31]: dpdk: create and remove interface in runtime
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 122]: linux-cp: auto select tap id when creating lcp pair

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 34]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 36]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 77]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [Vec 140]: mpls: fix possible crashes on tunnel create/delete
  | `38521 <https:////gerrit.fd.io/r/c/vpp/+/38521>`_ [VeC 153]: nat: improve nat44-ed outside address distribution
  | `38525 <https:////gerrit.fd.io/r/c/vpp/+/38525>`_ [VeC 164]: api: fix mp-safe mark for some messages and add more
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 166]: fib: fix interface resolve from unlinked fib entries
  | `38515 <https:////gerrit.fd.io/r/c/vpp/+/38515>`_ [VeC 166]: fib: fix freed mpls label disposition dpo access

**Vratko Polak** <vrpolak@cisco.com>:

  | `39436 <https:////gerrit.fd.io/r/c/vpp/+/39436>`_ [vEC 2]: vlib: deuglify the offset finding loop in pci.c
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [VEc 13]: vppapigen: recognize also _event as to_network
  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VeC 101]: ip: make running_fragment_id thread safe

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 99]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 125]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 127]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet
  | `38535 <https:////gerrit.fd.io/r/c/vpp/+/38535>`_ [VeC 162]: ipsec: fix non-esp packet may be matched as esp packet if flow cache enabled
  | `38500 <https:////gerrit.fd.io/r/c/vpp/+/38500>`_ [VeC 167]: ipsec: missing linear search when flow cache search failed
  | `37492 <https:////gerrit.fd.io/r/c/vpp/+/37492>`_ [VeC 178]: api: fix memory error with pending_rpc_requests in multi-thread environment

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38901 <https:////gerrit.fd.io/r/c/vpp/+/38901>`_ [VeC 87]: flow dpdk avf: add support for using l2tpv3 as RSS type
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 98]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [VEc 15]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 46]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VeC 46]: ipsec: delete redundant code

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [veC 98]: vrrp: dump vrrp vr peer

**mahdi varasteh** <mahdy.varasteh@gmail.com>:

  | `36726 <https:////gerrit.fd.io/r/c/vpp/+/36726>`_ [veC 153]: nat: add local addresses correctly in nat lb static mapping

**ranjan raj** <ranjanx.raj@intel.com>:

  | `39224 <https:////gerrit.fd.io/r/c/vpp/+/39224>`_ [VEc 8]: crypto-ipsecmb: bump intel-ipsec-mb version to 1.4

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [Vec 62]: ipsec: separate UDP and UDP-encapsulated ESP packet processing
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VeC 70]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process

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
authors          79
maintainers      31
committers       0
abandoned        0
================ ===

