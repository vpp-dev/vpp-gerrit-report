
==============================================
FD.io VPP (master branch) Gerrit Change Report
==============================================
--------------------------------------------
generated on Saturday 2023-11-11, 02:33:51
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

dhcp: **Dave Barach** <vpp@barachs.net>, **Neale Ranns** <neale@graphiant.com>
  | `39718 <https:////gerrit.fd.io/r/c/vpp/+/39718>`_ [VECr 2]: dhcp: api to enable client detect on interface

docs: **John DeNisco** <jdenisco@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>
  | `39844 <https:////gerrit.fd.io/r/c/vpp/+/39844>`_ [VECr 2]: docs: Remove references to vlan-strip-offload as it is deprecated

fib: **Neale Ranns** <neale@graphiant.com>
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 16]: fib: log an error when destroying non-empty tables

flowprobe: **Ole Troan** <otroan@employees.org>
  | `39848 <https:////gerrit.fd.io/r/c/vpp/+/39848>`_ [VECr 2]: flowprobe: fix tx flows generated for rewritten traffic

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `37610 <https:////gerrit.fd.io/r/c/vpp/+/37610>`_ [VECr 2]: http: unify client/server state machines

http: **Florin Coras** <fcoras@cisco.com>
  | `37610 <https:////gerrit.fd.io/r/c/vpp/+/37610>`_ [VECr 2]: http: unify client/server state machines

interface: **Dave Barach** <vpp@barachs.net>
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 24]: interface: check sw_if_index more thoroughly

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VECr 16]: ip6: ECMP hash support for ipv6 fragments

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39622 <https:////gerrit.fd.io/r/c/vpp/+/39622>`_ [VECr 25]: linux-cp: Fix looping netlink messages

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VECr 16]: ping:mark ipv6 packets as locally originated

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39858 <https:////gerrit.fd.io/r/c/vpp/+/39858>`_ [VECr 0]: tests: http static - Added a check if test is running with root privileges
  | `39851 <https:////gerrit.fd.io/r/c/vpp/+/39851>`_ [VECr 2]: tests: retry unlinking pcap files on os error
  | `39848 <https:////gerrit.fd.io/r/c/vpp/+/39848>`_ [VECr 2]: flowprobe: fix tx flows generated for rewritten traffic
  | `39761 <https:////gerrit.fd.io/r/c/vpp/+/39761>`_ [VECr 17]: tests: skip vcl tests with ASAN
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 29]: vlib: allow overlapping cli subcommands

vlib: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VECr 29]: vlib: allow overlapping cli subcommands

vpp_config: **John DeNisco** <jdenisco@cisco.com>
  | `39844 <https:////gerrit.fd.io/r/c/vpp/+/39844>`_ [VECr 2]: docs: Remove references to vlan-strip-offload as it is deprecated

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `39862 <https:////gerrit.fd.io/r/c/vpp/+/39862>`_ [VECr 0]: vppinfra: change fchmod to umask for unix socket
  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VECr 6]: vppinfra: fix memory overrun in mhash_set_mem

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 65]: nat: nat44-ed get out2in workers failed for static mapping without port

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 105]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 105]: api trace: the api trace info about barrier is opposite

**Adrian Villin** <avillin@cisco.com>:

  | `39861 <https:////gerrit.fd.io/r/c/vpp/+/39861>`_ [vEC 0]: tests: Added tracedump plugin tests
  | `39856 <https:////gerrit.fd.io/r/c/vpp/+/39856>`_ [VEc 0]: tests: Improved L2TP code coverage

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 99]: linux-cp: Fix update on IPv4 routes

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [veC 56]: ena: add tx checksum offloads and tso support
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VeC 64]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 94]: ip: add support for buffer offload metadata in ip midchain

**Damjan Marion** <dmarion@0xa5.net>:

  | `38819 <https:////gerrit.fd.io/r/c/vpp/+/38819>`_ [veC 57]: ena: Amazon Elastic Network Adapter (ENA) native driver (experimental)
  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 163]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 40]: libmemif: added tests
  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 65]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 163]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [vEC 4]: misc: patch to test CI infra changes

**Florin Coras** <florin.coras@gmail.com>:

  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [vEC 10]: session: program rx events only if none are pending

**Frédéric Perrin** <fred@fperrin.net>:

  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VeC 52]: tests: fix issues found when enabling DMAC check
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [Vec 53]: ethernet: check dmacs_bad in the fastpath case

**Gabriel Oginski** <gabrielx.oginski@intel.com>:

  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VeC 43]: interface dpdk avf: introducing setting RSS hash key feature
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VeC 43]: interface dpdk: refactor RSS queues feature

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 36]: ip: fix crash in ip4_neighbor_advertise

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 79]: sr: SRv6 Path Tracing source node behavior

**Kaj Niemi** <kajtzu@a51.org>:

  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VeC 32]: build: Enable building on AlmaLinux 9

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 49]: linux-cp: Add VRF synchronization

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 106]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 65]: nat: fix address resolution

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39778 <https:////gerrit.fd.io/r/c/vpp/+/39778>`_ [vEC 9]: devices: add support to check host interface offload capabilities
  | `35934 <https:////gerrit.fd.io/r/c/vpp/+/35934>`_ [vEC 9]: devices: add cli support to enable disable qdisc bypass
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 65]: geneve: add support for layer 3

**Naveen Joy** <najoy@cisco.com>:

  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VeC 45]: tests: memif ethernet type interface tests

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VEc 3]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 70]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 70]: ip: Set the buffer error in ip6-input

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 51]: geneve: support custom options in decap

**Nobuhiro Miki** <nmiki@yahoo-corp.jp>:

  | `39586 <https:////gerrit.fd.io/r/c/vpp/+/39586>`_ [VeC 45]: dpdk: fix description for mlx5_pci driver

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 107]: ipsec: introduce function esp_prepare_packet_for_enc

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 170]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 94]: ip: flow hash ignore tcp/udp ports when fragmented
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VeC 102]: dpdk: create and remove interface in runtime

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 36]: l2: fix crash while sending traffic out orphan BVI
  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 105]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 108]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 148]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Tianyu Li** <tianyu.li@arm.com>:

  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VeC 40]: libmemif: fix segfault and buffer overflow in examples

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 88]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vladislav Grishenko** <themiron@mail.ru>:

  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 38]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 45]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 45]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 45]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 45]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 44]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 52]: ip-neighbor: add version 3 of neighbor event
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [Vec 58]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 170]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 49]: interface dpdk avf: introducing setting RSS hash key feature
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 169]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 70]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 117]: ipsec: should use praddr_ instead of pladdr_

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 58]: vrrp: dump vrrp vr peer

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 87]: dhcp: fix dhcp multiple client request

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
authors          60
maintainers      15
committers       0
abandoned        0
================ ===

