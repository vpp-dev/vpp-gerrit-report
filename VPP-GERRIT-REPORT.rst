
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2023-10-18, 01:59:24
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
  | `39151 <https:////gerrit.fd.io/r/c/vpp/+/39151>`_ [VECr 20]: build: test

avf: **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 25]: interface dpdk avf: introducing setting RSS hash key feature

bonding: **Steven Luong** <sluong@cisco.com>
  | `39686 <https:////gerrit.fd.io/r/c/vpp/+/39686>`_ [VECr 0]: bonding: add checks for sw_if_index in api

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `39683 <https:////gerrit.fd.io/r/c/vpp/+/39683>`_ [VECr 1]: buffers: NULL terminate buffer pool name

build: **Damjan Marion** <damarion@cisco.com>
  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VECr 8]: build: Enable building on AlmaLinux 9

crypto: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>
  | `39614 <https:////gerrit.fd.io/r/c/vpp/+/39614>`_ [VECr 1]: crypto: fix algo selection

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 19]: interface dpdk: refactor RSS queues feature
  | `39586 <https:////gerrit.fd.io/r/c/vpp/+/39586>`_ [VECr 21]: dpdk: fix description for mlx5_pci driver
  | `39581 <https:////gerrit.fd.io/r/c/vpp/+/39581>`_ [VECr 22]: dpdk: correct the printing of Rx offloading flags
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 25]: interface dpdk avf: introducing setting RSS hash key feature

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 19]: interface dpdk: refactor RSS queues feature

fib: **Neale Ranns** <neale@graphiant.com>
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 14]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VECr 21]: fib: fix interface resolve from unlinked fib entries
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VECr 21]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 21]: fib: fix udp encap mp-safe ops and id validation

flowprobe: **Ole Troan** <otroan@employees.org>
  | `39685 <https:////gerrit.fd.io/r/c/vpp/+/39685>`_ [VECr 0]: flowprobe: fix sending L4 fields in L2 template and flows

geneve: **community** vpp-dev@lists.fd.io
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 27]: geneve: support custom options in decap

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [VECr 13]: gtpu: support non-G-PDU packets and PDU Session

hs-test: **Florin Coras** <fcoras@cisco.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Maros Ondrejicka** <maros.ondrejicka@pantheon.tech>
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 1]: hsa: unify echo test setup

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 1]: hsa: unify echo test setup

ikev2: **Damjan Marion** <damarion@cisco.com>, **Neale Ranns** <neale@graphiant.com>, **Filip Tehlar** <ftehlar@cisco.com>, **Benoît Ganne** <bganne@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 4]: ipsec: huge anti-replay window support

interface: **Dave Barach** <vpp@barachs.net>
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 0]: interface: check sw_if_index more thoroughly
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 19]: interface dpdk: refactor RSS queues feature
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 25]: interface dpdk avf: introducing setting RSS hash key feature

ip-neighbor: **Neale Ranns** <neale@graphiant.com>
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 28]: ip-neighbor: add version 3 of neighbor event

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VECr 12]: ip: fix crash in ip4_neighbor_advertise

ipsec: **Neale Ranns** <neale@graphiant.com>, **Radu Nicolau** <radu.nicolau@intel.com>, **Fan Zhang** <fanzhang.oss@gmail.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 4]: ipsec: huge anti-replay window support

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VECr 12]: l2: fix crash while sending traffic out orphan BVI

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VECr 16]: libmemif: added tests
  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VECr 16]: libmemif: fix segfault and buffer overflow in examples

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39622 <https:////gerrit.fd.io/r/c/vpp/+/39622>`_ [VECr 1]: linux-cp: Fix looping netlink messages
  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VECr 25]: linux-cp: Add VRF synchronization

memif: **Damjan Marion** <damarion@cisco.com>
  | `39619 <https:////gerrit.fd.io/r/c/vpp/+/39619>`_ [VECr 4]: memif: contention between memif_disconnect and memif RX/TX threads

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 19]: interface dpdk avf: introducing setting RSS hash key feature
  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VECr 25]: interface dpdk avf: introducing setting RSS hash key feature

mpls: **Neale Ranns** <neale@graphiant.com>
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 21]: mpls: fix crashes on mpls tunnel create/delete

session: **Florin Coras** <fcoras@cisco.com>
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [VECr 27]: session: program rx events only if none are pending

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39685 <https:////gerrit.fd.io/r/c/vpp/+/39685>`_ [VECr 0]: flowprobe: fix sending L4 fields in L2 template and flows
  | `38792 <https:////gerrit.fd.io/r/c/vpp/+/38792>`_ [VECr 0]: ipsec: modify IPsec related tests to send and verify UDP-encapsulated ESP traffics
  | `39480 <https:////gerrit.fd.io/r/c/vpp/+/39480>`_ [VECr 1]: hsa: unify echo test setup
  | `39662 <https:////gerrit.fd.io/r/c/vpp/+/39662>`_ [VECr 1]: tests: allow explicit defaults for arg types
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 4]: ipsec: huge anti-replay window support
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 5]: vlib: allow overlapping cli subcommands
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 14]: nat: fix nat44-ed address removal from fib
  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VECr 21]: tests: memif ethernet type interface tests
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VECr 21]: mpls: fix crashes on mpls tunnel create/delete
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 21]: fib: fix udp encap mp-safe ops and id validation
  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VECr 27]: geneve: support custom options in decap
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VECr 28]: tests: fix issues found when enabling DMAC check
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VECr 28]: ip-neighbor: add version 3 of neighbor event

udp: **Florin Coras** <fcoras@cisco.com>
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VECr 21]: fib: fix udp encap mp-safe ops and id validation

unittest: **Dave Barach** <vpp@barachs.net>, **Florin Coras** <fcoras@cisco.com>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 4]: ipsec: huge anti-replay window support

vcl: **Florin Coras** <fcoras@cisco.com>
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 15]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 5]: vlib: allow overlapping cli subcommands

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `37865 <https:////gerrit.fd.io/r/c/vpp/+/37865>`_ [VECr 4]: ipsec: huge anti-replay window support

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 41]: nat: nat44-ed get out2in workers failed for static mapping without port

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 81]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 81]: api trace: the api trace info about barrier is opposite

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 75]: linux-cp: Fix update on IPv4 routes

**Andrew Yourtchenko** <ayourtch@gmail.com>:

  | `38794 <https:////gerrit.fd.io/r/c/vpp/+/38794>`_ [veC 125]: TEST: remove IKEv2 tests
  | `38788 <https:////gerrit.fd.io/r/c/vpp/+/38788>`_ [veC 145]: TEST: blank out the SVM fifo tests
  | `38781 <https:////gerrit.fd.io/r/c/vpp/+/38781>`_ [veC 155]: TEST: remove the rdma mappings

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [veC 32]: ena: add tx checksum offloads and tso support
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VeC 40]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 70]: ip: add support for buffer offload metadata in ip midchain

**Benoît Ganne** <bganne@cisco.com>:

  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VeC 33]: fib: log an error when destroying non-empty tables
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VeC 62]: ip6: ECMP hash support for ipv6 fragments

**Damjan Marion** <dmarion@0xa5.net>:

  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [veC 33]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 139]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 41]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 139]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Frédéric Perrin** <fred@fperrin.net>:

  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VEc 29]: ethernet: check dmacs_bad in the fastpath case

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 55]: sr: SRv6 Path Tracing source node behavior

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 82]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 41]: nat: fix address resolution

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `35934 <https:////gerrit.fd.io/r/c/vpp/+/35934>`_ [vEC 7]: devices: add cli support to enable disable qdisc bypass
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 41]: geneve: add support for layer 3

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VEc 9]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 46]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 46]: ip: Set the buffer error in ip6-input

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 83]: ipsec: introduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 160]: ipsec: esp_encrypt prefetch and unroll - introduce new types

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 146]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 70]: ip: flow hash ignore tcp/udp ports when fragmented
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 78]: dpdk: create and remove interface in runtime
  | `38456 <https:////gerrit.fd.io/r/c/vpp/+/38456>`_ [VeC 169]: linux-cp: auto select tap id when creating lcp pair

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 81]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 83]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 124]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Ting Xu** <ting.xu@intel.com>:

  | `39198 <https:////gerrit.fd.io/r/c/vpp/+/39198>`_ [VeC 62]: dpdk: fix variable type in pattern parsing

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 64]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [VEc 20]: ip: make running_fragment_id thread safe
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [Vec 34]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 146]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node
  | `38742 <https:////gerrit.fd.io/r/c/vpp/+/38742>`_ [veC 172]: linux-cp: fix compiler error with libnl 3.2.x
  | `38728 <https:////gerrit.fd.io/r/c/vpp/+/38728>`_ [veC 174]: ipsec: remove redundant match in ipsec4-input-feature with decrypted esp/ah packet

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 145]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 46]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 93]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VeC 93]: ipsec: delete redundant code

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 34]: vrrp: dump vrrp vr peer

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 63]: dhcp: fix dhcp multiple client request

**vinay tripathi** <vinayx.tripathi@intel.com>:

  | `38791 <https:////gerrit.fd.io/r/c/vpp/+/38791>`_ [VEc 0]: ipsec: move udp/esp packet processing in the inline function ipsec_udp_encap_esp_packet_process
  | `38793 <https:////gerrit.fd.io/r/c/vpp/+/38793>`_ [Vec 109]: ipsec: separate UDP and UDP-encapsulated ESP packet processing

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
authors          49
maintainers      36
committers       0
abandoned        0
================ ===

