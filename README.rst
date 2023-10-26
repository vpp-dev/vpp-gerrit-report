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
generated on Thursday 2023-10-26, 01:56:54
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

acl: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `39151 <https:////gerrit.fd.io/r/c/vpp/+/39151>`_ [VECr 28]: build: test

avf: **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 27]: interface dpdk avf: introducing setting RSS hash key feature

bonding: **Steven Luong** <sluong@cisco.com>
  | `39686 <https:////gerrit.fd.io/r/c/vpp/+/39686>`_ [VECr 8]: bonding: add checks for sw_if_index in api

build: **Damjan Marion** <damarion@cisco.com>
  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VECr 16]: build: Enable building on AlmaLinux 9

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 27]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 27]: interface dpdk: refactor RSS queues feature
  | `39586 <https:////gerrit.fd.io/r/c/vpp/+/39586>`_ [VECr 29]: dpdk: fix description for mlx5_pci driver
  | `39581 <https:////gerrit.fd.io/r/c/vpp/+/39581>`_ [VECr 30]: dpdk: correct the printing of Rx offloading flags

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 27]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 27]: interface dpdk: refactor RSS queues feature

fib: **Neale Ranns** <neale@graphiant.com>
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 0]: fib: log an error when destroying non-empty tables
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 22]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VECr 29]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VECr 29]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 29]: fib: fix udp encap mp-safe ops and id validation

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [VECr 21]: gtpu: support non-G-PDU packets and PDU Session

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 2]: hsa: unify echo test setup

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `39767 <https:////gerrit.fd.io/r/c/vpp/+/39767>`_ [VECr 0]: hsa: preallocate sessions on server side
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 2]: hsa: unify echo test setup

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 1]: ipsec: huge anti-replay window support

interface: **Dave Barach** <vpp@barachs.net>
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 8]: interface: check sw_if_index more thoroughly
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 27]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 27]: interface dpdk: refactor RSS queues feature

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VECr 0]: ip6: ECMP hash support for ipv6 fragments
  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VECr 20]: ip: fix crash in ip4_neighbor_advertise

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 1]: ipsec: huge anti-replay window support
  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VECr 5]: ipsec: move udp/esp packet processing in the inline function ipsec_esp_packet_process

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VECr 20]: l2: fix crash while sending traffic out orphan BVI

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VECr 24]: libmemif: added tests
  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VECr 24]: libmemif: fix segfault and buffer overflow in examples

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39622 <https:////gerrit.fd.io/r/c/vpp/+/39622>`_ [VECr 9]: linux-cp: Fix looping netlink messages

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 27]: interface dpdk avf: introducing setting RSS hash key feature

mpls: **Neale Ranns** <neale@graphiant.com>
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 29]: mpls: fix crashes on mpls tunnel create/delete

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VECr 0]: ping:mark ipv6 packets as locally originated

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39765 <https:////gerrit.fd.io/r/c/vpp/+/39765>`_ [VECr 0]: tests: Added bufmon plugin test
  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VECr 0]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 1]: ipsec: huge anti-replay window support
  | `39761 <https:////gerrit.fd.io/r/c/vpp/+/39761>`_ [VECr 1]: tests: skip vcl tests with ASAN
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 2]: hsa: unify echo test setup
  | `39662 <https:////gerrit.fd.io/r/c/vpp/+/39662>`_ [VECr 9]: tests: allow explicit defaults for arg types
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 13]: vlib: allow overlapping cli subcommands
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 22]: nat: fix nat44-ed address removal from fib
  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VECr 29]: tests: memif ethernet type interface tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 29]: mpls: fix crashes on mpls tunnel create/delete
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 29]: fib: fix udp encap mp-safe ops and id validation

udp: **Florin Coras** <fcoras@cisco.com>
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 29]: fib: fix udp encap mp-safe ops and id validation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 1]: ipsec: huge anti-replay window support

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 23]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 13]: vlib: allow overlapping cli subcommands

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VECr 0]: vppinfra: fix memory overrun in mhash_set_mem
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 1]: ipsec: huge anti-replay window support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 49]: nat: nat44-ed get out2in workers failed for static mapping without port

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 89]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 89]: api trace: the api trace info about barrier is opposite

**Adrian Villin** <avillin@cisco.com>:

  | `39760 <https:////gerrit.fd.io/r/c/vpp/+/39760>`_ [vEC 0]: tests: Added http static server tests.

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 83]: linux-cp: Fix update on IPv4 routes

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `39152 <https:////gerrit.fd.io/r/c/vpp/+/39152>`_ [vEC 0]: build: allow for reproducible builds

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [veC 40]: ena: add tx checksum offloads and tso support
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VeC 48]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 78]: ip: add support for buffer offload metadata in ip midchain

**Damjan Marion** <dmarion@0xa5.net>:

  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [veC 41]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 147]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 49]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 147]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dave Wallace** <dwallacelf@gmail.com>:

  | `39457 <https:////gerrit.fd.io/r/c/vpp/+/39457>`_ [vEC 1]: tests: refactor asf framework code

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [VeC 35]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 36]: tests: fix issues found when enabling DMAC check
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [Vec 37]: ethernet: check dmacs_bad in the fastpath case

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 63]: sr: SRv6 Path Tracing source node behavior

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 33]: linux-cp: Add VRF synchronization

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 90]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 49]: nat: fix address resolution

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `35934 <https:////gerrit.fd.io/r/c/vpp/+/35934>`_ [vEC 15]: devices: add cli support to enable disable qdisc bypass
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 49]: geneve: add support for layer 3

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VEc 17]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 54]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 54]: ip: Set the buffer error in ip6-input

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 35]: geneve: support custom options in decap

**Ole Troan** <otroan@employees.org>:

  | `39718 <https:////gerrit.fd.io/r/c/vpp/+/39718>`_ [vEC 6]: dhcp: api to enable client detect on interface

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 91]: ipsec: introduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 168]: ipsec: esp_encrypt prefetch and unroll - introduce new types

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 154]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 78]: ip: flow hash ignore tcp/udp ports when fragmented
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 86]: dpdk: create and remove interface in runtime
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 177]: linux-cp: auto select tap id when creating lcp pair

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 89]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 91]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 132]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 72]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VEc 28]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 36]: ip-neighbor: add version 3 of neighbor event
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [Vec 42]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 154]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 33]: interface dpdk avf: introducing setting RSS hash key feature
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 153]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 54]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 101]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VeC 101]: ipsec: delete redundant code

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 42]: vrrp: dump vrrp vr peer

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 71]: dhcp: fix dhcp multiple client request

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [VEc 7]: ipsec: separate UDP and UDP-encapsulated ESP packet processing

Abandoned:
----------
**The following gerrit changes have not been updated in over 180 days and have been abandoned.**

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [A 180]: linux-cp: fix compiler error with libnl 3.2.x

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
authors          50
maintainers      34
committers       0
abandoned        1
================ ===

