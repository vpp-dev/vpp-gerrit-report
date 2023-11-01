
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Wednesday 2023-11-01, 02:02:48
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

bonding: **Steven Luong** <sluong@cisco.com>
  | `39686 <https:////gerrit.fd.io/r/c/vpp/+/39686>`_ [VECr 14]: bonding: add checks for sw_if_index in api

buffers: **Damjan Marion** <damarion@cisco.com>, **Dave Barach** <vpp@barachs.net>
  | `39807 <https:////gerrit.fd.io/r/c/vpp/+/39807>`_ [VECr 0]: misc: silence -Wmaybe-uninitialized warnings

build: **Damjan Marion** <damarion@cisco.com>
  | `39808 <https:////gerrit.fd.io/r/c/vpp/+/39808>`_ [VECr 0]: build: disable bogus warnings for GCC 12
  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VECr 22]: build: Enable building on AlmaLinux 9

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39581 <https:////gerrit.fd.io/r/c/vpp/+/39581>`_ [VECr 1]: dpdk: correct the printing of Rx offloading flags

fib: **Neale Ranns** <neale@graphiant.com>
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 6]: fib: log an error when destroying non-empty tables
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 28]: nat: fix nat44-ed address removal from fib

flowprobe: **Ole Troan** <otroan@employees.org>
  | `39772 <https:////gerrit.fd.io/r/c/vpp/+/39772>`_ [VECr 5]: flowprobe: fix clearing interface state on feature disabling

gtpu: **Hongjun Ni** <hongjun.ni@intel.com>
  | `38573 <https:////gerrit.fd.io/r/c/vpp/+/38573>`_ [VECr 27]: gtpu: support non-G-PDU packets and PDU Session

interface: **Dave Barach** <vpp@barachs.net>
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 14]: interface: check sw_if_index more thoroughly

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VECr 6]: ip6: ECMP hash support for ipv6 fragments
  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VECr 26]: ip: fix crash in ip4_neighbor_advertise

l2: **John Lo** <lojultra2020@outlook.com>, **Steven Luong** <sluong@cisco.com>
  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VECr 26]: l2: fix crash while sending traffic out orphan BVI

libmemif: **Damjan Marion** <damarion@cisco.com>
  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VECr 30]: libmemif: added tests
  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VECr 30]: libmemif: fix segfault and buffer overflow in examples

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39622 <https:////gerrit.fd.io/r/c/vpp/+/39622>`_ [VECr 15]: linux-cp: Fix looping netlink messages

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VECr 6]: ping:mark ipv6 packets as locally originated

policer: **Neale Ranns** <neale@graphiant.com>
  | `39807 <https:////gerrit.fd.io/r/c/vpp/+/39807>`_ [VECr 0]: misc: silence -Wmaybe-uninitialized warnings

tcp: **Florin Coras** <fcoras@cisco.com>
  | `39807 <https:////gerrit.fd.io/r/c/vpp/+/39807>`_ [VECr 0]: misc: silence -Wmaybe-uninitialized warnings
  | `39797 <https:////gerrit.fd.io/r/c/vpp/+/39797>`_ [VECr 0]: tcp: postpone cleanup on connect failures

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39812 <https:////gerrit.fd.io/r/c/vpp/+/39812>`_ [VECr 0]: tests: added a simple perfmon plugin test
  | `39772 <https:////gerrit.fd.io/r/c/vpp/+/39772>`_ [VECr 5]: flowprobe: fix clearing interface state on feature disabling
  | `39761 <https:////gerrit.fd.io/r/c/vpp/+/39761>`_ [VECr 7]: tests: skip vcl tests with ASAN
  | `39662 <https:////gerrit.fd.io/r/c/vpp/+/39662>`_ [VECr 15]: tests: allow explicit defaults for arg types
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 19]: vlib: allow overlapping cli subcommands
  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VECr 28]: nat: fix nat44-ed address removal from fib

vcl: **Florin Coras** <fcoras@cisco.com>
  | `39807 <https:////gerrit.fd.io/r/c/vpp/+/39807>`_ [VECr 0]: misc: silence -Wmaybe-uninitialized warnings
  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [VECr 29]: misc: patch to test CI infra changes

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 19]: vlib: allow overlapping cli subcommands

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VECr 4]: vppinfra: fix memory overrun in mhash_set_mem

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 55]: nat: nat44-ed get out2in workers failed for static mapping without port

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 95]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 95]: api trace: the api trace info about barrier is opposite

**Adrian Villin** <avillin@cisco.com>:

  | `39811 <https:////gerrit.fd.io/r/c/vpp/+/39811>`_ [vEC 0]: tests: added simple CT6 plugin tests

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 89]: linux-cp: Fix update on IPv4 routes

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [veC 46]: ena: add tx checksum offloads and tso support
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VeC 54]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 84]: ip: add support for buffer offload metadata in ip midchain

**Damjan Marion** <dmarion@0xa5.net>:

  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [veC 47]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 153]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 55]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 153]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dave Wallace** <dwallacelf@gmail.com>:

  | `39457 <https:////gerrit.fd.io/r/c/vpp/+/39457>`_ [vEC 0]: tests: refactor asf framework code
  | `39806 <https:////gerrit.fd.io/r/c/vpp/+/39806>`_ [vEC 1]: tests: remove packet debug output from npt66 testcases

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [vEC 0]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 42]: tests: fix issues found when enabling DMAC check
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [Vec 43]: ethernet: check dmacs_bad in the fastpath case

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 33]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 33]: interface dpdk: refactor RSS queues feature

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 69]: sr: SRv6 Path Tracing source node behavior

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 39]: linux-cp: Add VRF synchronization

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 96]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 55]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39813 <https:////gerrit.fd.io/r/c/vpp/+/39813>`_ [vEC 0]: vnet: IPsec fix constant propgagation

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `35934 <https:////gerrit.fd.io/r/c/vpp/+/35934>`_ [vEC 0]: devices: add cli support to enable disable qdisc bypass
  | `39778 <https:////gerrit.fd.io/r/c/vpp/+/39778>`_ [vEC 0]: devices: add support to check host interface offload capabilities
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 55]: geneve: add support for layer 3

**Naveen Joy** <najoy@cisco.com>:

  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VeC 35]: tests: memif ethernet type interface tests

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VEc 23]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 60]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 60]: ip: Set the buffer error in ip6-input

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 41]: geneve: support custom options in decap

**Nobuhiro Miki** <nmiki@yahoo-corp.jp>:

  | `39586 <https:////gerrit.fd.io/r/c/vpp/+/39586>`_ [VeC 35]: dpdk: fix description for mlx5_pci driver

**Ole Troan** <otroan@employees.org>:

  | `39718 <https:////gerrit.fd.io/r/c/vpp/+/39718>`_ [vEC 12]: dhcp: api to enable client detect on interface

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 97]: ipsec: introduce function esp_prepare_packet_for_enc
  | `38407 <https:////gerrit.fd.io/r/c/vpp/+/38407>`_ [Vec 174]: ipsec: esp_encrypt prefetch and unroll - introduce new types

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 160]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 84]: ip: flow hash ignore tcp/udp ports when fragmented
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 92]: dpdk: create and remove interface in runtime

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 95]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 97]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 138]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 78]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vladislav Grishenko** <themiron@mail.ru>:

  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 35]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 35]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 35]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 35]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 34]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 42]: ip-neighbor: add version 3 of neighbor event
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [Vec 48]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 160]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 39]: interface dpdk avf: introducing setting RSS hash key feature
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 159]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 60]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 107]: ipsec: should use praddr_ instead of pladdr_
  | `39229 <https:////gerrit.fd.io/r/c/vpp/+/39229>`_ [VeC 107]: ipsec: delete redundant code

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 48]: vrrp: dump vrrp vr peer

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 77]: dhcp: fix dhcp multiple client request

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
authors          58
maintainers      24
committers       0
abandoned        0
================ ===

