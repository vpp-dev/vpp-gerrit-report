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
generated on Saturday 2023-11-18, 02:02:14
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
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 6]: ethernet: check dmacs_bad in the fastpath case

avf: **Damjan Marion** <damarion@cisco.com>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 2]: interface dpdk avf: introducing setting RSS hash key feature
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 6]: ethernet: check dmacs_bad in the fastpath case

dev: **Damjan Marion** <damarion@cisco.com>
  | `39938 <https:////gerrit.fd.io/r/c/vpp/+/39938>`_ [VECr 1]: dev: fix null dereference of arg list

dpdk: **Damjan Marion** <damarion@cisco.com>, **Mohammed Hawari** <mohammed@hawari.fr>
  | `39121 <https:////gerrit.fd.io/r/c/vpp/+/39121>`_ [VECr 0]: dpdk: create and remove interface in runtime
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 2]: interface dpdk: refactor RSS queues feature
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 2]: interface dpdk avf: introducing setting RSS hash key feature
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 6]: ethernet: check dmacs_bad in the fastpath case

ethernet: **Dave Barach** <vpp@barachs.net>, **Damjan Marion** <damarion@cisco.com>
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 2]: interface dpdk: refactor RSS queues feature
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 2]: interface dpdk avf: introducing setting RSS hash key feature
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 6]: ethernet: check dmacs_bad in the fastpath case

fib: **Neale Ranns** <neale@graphiant.com>
  | `39525 <https:////gerrit.fd.io/r/c/vpp/+/39525>`_ [VECr 23]: fib: log an error when destroying non-empty tables

hsa: **Florin Coras** <fcoras@cisco.com>, **Dave Wallace** <dwallacelf@gmail.com>, **Aloys Augustin** <aloaugus@cisco.com>, **Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>
  | `37610 <https:////gerrit.fd.io/r/c/vpp/+/37610>`_ [VECr 2]: http: unify client/server state machines

http: **Florin Coras** <fcoras@cisco.com>
  | `37610 <https:////gerrit.fd.io/r/c/vpp/+/37610>`_ [VECr 2]: http: unify client/server state machines

interface: **Dave Barach** <vpp@barachs.net>
  | `39590 <https:////gerrit.fd.io/r/c/vpp/+/39590>`_ [VECr 2]: interface dpdk: refactor RSS queues feature
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 2]: interface dpdk avf: introducing setting RSS hash key feature
  | `39305 <https:////gerrit.fd.io/r/c/vpp/+/39305>`_ [VECr 3]: interface: check sw_if_index more thoroughly
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 6]: ethernet: check dmacs_bad in the fastpath case

ip6: **Neale Ranns** <neale@graphiant.com>, **Jon Loeliger** <jdl@netgate.com>
  | `39309 <https:////gerrit.fd.io/r/c/vpp/+/39309>`_ [VECr 23]: ip6: ECMP hash support for ipv6 fragments

linux-cp: **Neale Ranns** <neale@graphiant.com>, **Matthew Smith** <mgsmith@netgate.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 6]: ethernet: check dmacs_bad in the fastpath case

misc: **vpp-dev Mailing List** <vpp-dev@fd.io>
  | `39549 <https:////gerrit.fd.io/r/c/vpp/+/39549>`_ [VECr 2]: interface dpdk avf: introducing setting RSS hash key feature

ping: **Andrew Yourtchenko** <ayourtch@gmail.com>
  | `39777 <https:////gerrit.fd.io/r/c/vpp/+/39777>`_ [VECr 23]: ping:mark ipv6 packets as locally originated

rdma: **Benoît Ganne** <bganne@cisco.com>, **Damjan Marion** <damarion@cisco.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 6]: ethernet: check dmacs_bad in the fastpath case

tests: **Klement Sekera** <klement.sekera@gmail.com>, **Paul Vinciguerra** <pvinci@vinciconsulting.com>
  | `39251 <https:////gerrit.fd.io/r/c/vpp/+/39251>`_ [VECr 6]: ethernet: check dmacs_bad in the fastpath case
  | `39321 <https:////gerrit.fd.io/r/c/vpp/+/39321>`_ [VECr 6]: tests: fix issues found when enabling DMAC check
  | `39761 <https:////gerrit.fd.io/r/c/vpp/+/39761>`_ [VECr 24]: tests: skip vcl tests with ASAN

virtio: **Mohsin Kazmi** <mohsin.kazmi14@gmail.com>, **Damjan Marion** <damarion@cisco.com>
  | `39872 <https:////gerrit.fd.io/r/c/vpp/+/39872>`_ [VECr 2]: virtio: fix cli parsing for tx-queue-size

vppinfra: **Dave Barach** <vpp@barachs.net>
  | `39862 <https:////gerrit.fd.io/r/c/vpp/+/39862>`_ [VECr 7]: vppinfra: change fchmod to umask for unix socket
  | `39776 <https:////gerrit.fd.io/r/c/vpp/+/39776>`_ [VECr 13]: vppinfra: fix memory overrun in mhash_set_mem

Authors:
--------
**Please rebase and fix verification failures on these gerrit changes.**

** Chiso Gao** <chiso.gao@gmail.com>:

  | `37153 <https:////gerrit.fd.io/r/c/vpp/+/37153>`_ [VeC 72]: nat: nat44-ed get out2in workers failed for static mapping without port

** Lawrence chen** <326942298@qq.com>:

  | `39282 <https:////gerrit.fd.io/r/c/vpp/+/39282>`_ [veC 112]: api trace: the api trace info about barrier is opposite
  | `39281 <https:////gerrit.fd.io/r/c/vpp/+/39281>`_ [veC 112]: api trace: the api trace info about barrier is opposite

**Adrian Villin** <avillin@cisco.com>:

  | `39900 <https:////gerrit.fd.io/r/c/vpp/+/39900>`_ [vEC 1]: tests: Added NSIM plugin tests
  | `39856 <https:////gerrit.fd.io/r/c/vpp/+/39856>`_ [VEc 2]: tests: Improved L2TP code coverage
  | `39861 <https:////gerrit.fd.io/r/c/vpp/+/39861>`_ [vEC 7]: tests: Added tracedump plugin tests

**Alexander Skorichenko** <askorichenko@netgate.com>:

  | `39220 <https:////gerrit.fd.io/r/c/vpp/+/39220>`_ [VeC 106]: linux-cp: Fix update on IPv4 routes

**Arthur de Kerhor** <arthurdekerhor@gmail.com>:

  | `39532 <https:////gerrit.fd.io/r/c/vpp/+/39532>`_ [veC 63]: ena: add tx checksum offloads and tso support
  | `39163 <https:////gerrit.fd.io/r/c/vpp/+/39163>`_ [VeC 71]: ipsec: allow receiving encrypted IP packets with TFC padding
  | `32695 <https:////gerrit.fd.io/r/c/vpp/+/32695>`_ [Vec 101]: ip: add support for buffer offload metadata in ip midchain

**Damjan Marion** <dmarion@0xa5.net>:

  | `38917 <https:////gerrit.fd.io/r/c/vpp/+/38917>`_ [Vec 170]: vlib: add vlib_buffer_is_chained() and use it where possible

**Daniel Beres** <dberes@cisco.com>:

  | `37953 <https:////gerrit.fd.io/r/c/vpp/+/37953>`_ [VeC 47]: libmemif: added tests
  | `37071 <https:////gerrit.fd.io/r/c/vpp/+/37071>`_ [Vec 72]: ebuild: adding libmemif to debian packages

**Dastin Wilski** <dastin.wilski@gmail.com>:

  | `37835 <https:////gerrit.fd.io/r/c/vpp/+/37835>`_ [Vec 170]: crypto-ipsecmb: crypto_key prefetch and unrolling for aes-gcm

**Dave Wallace** <dwallacelf@gmail.com>:

  | `37088 <https:////gerrit.fd.io/r/c/vpp/+/37088>`_ [vEC 11]: misc: patch to test CI infra changes

**Florin Coras** <florin.coras@gmail.com>:

  | `39941 <https:////gerrit.fd.io/r/c/vpp/+/39941>`_ [vEC 0]: session: add session lookup cli for stats
  | `39449 <https:////gerrit.fd.io/r/c/vpp/+/39449>`_ [vEC 17]: session: program rx events only if none are pending

**Ivan Shvedunov** <ivan4th@gmail.com>:

  | `39615 <https:////gerrit.fd.io/r/c/vpp/+/39615>`_ [VeC 43]: ip: fix crash in ip4_neighbor_advertise

**Julian Klaiber** <julian@klaiber.me>:

  | `39408 <https:////gerrit.fd.io/r/c/vpp/+/39408>`_ [VeC 86]: sr: SRv6 Path Tracing source node behavior

**Kaj Niemi** <kajtzu@a51.org>:

  | `39629 <https:////gerrit.fd.io/r/c/vpp/+/39629>`_ [VeC 39]: build: Enable building on AlmaLinux 9

**Konstantin Kogdenko** <k.kogdenko@gmail.com>:

  | `39518 <https:////gerrit.fd.io/r/c/vpp/+/39518>`_ [VeC 56]: linux-cp: Add VRF synchronization

**Liangxing Wang** <liangxing.wang@arm.com>:

  | `39095 <https:////gerrit.fd.io/r/c/vpp/+/39095>`_ [Vec 113]: memif: use VPP cache line size macro instead of hard coded 64 bytes

**Maros Ondrejicka** <mondreji@cisco.com>:

  | `38461 <https:////gerrit.fd.io/r/c/vpp/+/38461>`_ [VeC 72]: nat: fix address resolution

**Maxime Peim** <mpeim@cisco.com>:

  | `39871 <https:////gerrit.fd.io/r/c/vpp/+/39871>`_ [vEC 3]: tests: preload api files

**Mohsin Kazmi** <sykazmi@cisco.com>:

  | `39778 <https:////gerrit.fd.io/r/c/vpp/+/39778>`_ [vEC 16]: devices: add support to check host interface offload capabilities
  | `35934 <https:////gerrit.fd.io/r/c/vpp/+/35934>`_ [vEC 16]: devices: add cli support to enable disable qdisc bypass
  | `39146 <https:////gerrit.fd.io/r/c/vpp/+/39146>`_ [Vec 72]: geneve: add support for layer 3

**Nathan Skrzypczak** <nathan.skrzypczak@gmail.com>:

  | `32819 <https:////gerrit.fd.io/r/c/vpp/+/32819>`_ [VeC 36]: vlib: allow overlapping cli subcommands

**Naveen Joy** <najoy@cisco.com>:

  | `39319 <https:////gerrit.fd.io/r/c/vpp/+/39319>`_ [VeC 52]: tests: memif ethernet type interface tests

**Neale Ranns** <neale@graphiant.com>:

  | `38092 <https:////gerrit.fd.io/r/c/vpp/+/38092>`_ [VEc 10]: ip: IP address family common input node
  | `38116 <https:////gerrit.fd.io/r/c/vpp/+/38116>`_ [VeC 77]: ip: IPv6 validate input packet's header length does not exist buffer size
  | `38095 <https:////gerrit.fd.io/r/c/vpp/+/38095>`_ [veC 77]: ip: Set the buffer error in ip6-input

**Nick Zavaritsky** <nick.zavaritsky@emnify.com>:

  | `39477 <https:////gerrit.fd.io/r/c/vpp/+/39477>`_ [VeC 58]: geneve: support custom options in decap

**Nobuhiro Miki** <nmiki@yahoo-corp.jp>:

  | `39586 <https:////gerrit.fd.io/r/c/vpp/+/39586>`_ [VEc 0]: dpdk: fix description for mlx5_pci driver

**Pim van Pelt** <pim@ipng.nl>:

  | `39622 <https:////gerrit.fd.io/r/c/vpp/+/39622>`_ [VeC 32]: linux-cp: Fix looping netlink messages

**Piotr Bronowski** <piotrx.bronowski@intel.com>:

  | `38409 <https:////gerrit.fd.io/r/c/vpp/+/38409>`_ [veC 114]: ipsec: introduce function esp_prepare_packet_for_enc

**Simon Zolin** <steelum@gmail.com>:

  | `38850 <https:////gerrit.fd.io/r/c/vpp/+/38850>`_ [VeC 177]: fib: don't leave default 'dpo-drop' rule after 'sr steer'

**Stanislav Zaikin** <zstaseg@gmail.com>:

  | `39317 <https:////gerrit.fd.io/r/c/vpp/+/39317>`_ [VeC 101]: ip: flow hash ignore tcp/udp ports when fragmented

**Sylvain C** <sylvain.cadilhac@freepro.com>:

  | `39613 <https:////gerrit.fd.io/r/c/vpp/+/39613>`_ [VeC 43]: l2: fix crash while sending traffic out orphan BVI
  | `39294 <https:////gerrit.fd.io/r/c/vpp/+/39294>`_ [veC 112]: api: ip - set punt reason max length to fix VAPI generation

**Takeru Hayasaka** <hayatake396@gmail.com>:

  | `37628 <https:////gerrit.fd.io/r/c/vpp/+/37628>`_ [VeC 114]: srv6-mobile: Implement SRv6 mobile API funcs

**Ted Chen** <znscnchen@gmail.com>:

  | `39062 <https:////gerrit.fd.io/r/c/vpp/+/39062>`_ [veC 155]: ethernet: fix fastpath does not drop the packet with incorrect destination MAC

**Tianyu Li** <tianyu.li@arm.com>:

  | `39266 <https:////gerrit.fd.io/r/c/vpp/+/39266>`_ [VeC 47]: libmemif: fix segfault and buffer overflow in examples

**Vladimir Ratnikov** <vratnikov@netgate.com>:

  | `39287 <https:////gerrit.fd.io/r/c/vpp/+/39287>`_ [VeC 95]: ip6-nd: Revert "ip6-nd: initialize radv_info->send_radv to 1"

**Vladislav Grishenko** <themiron@mail.ru>:

  | `39555 <https:////gerrit.fd.io/r/c/vpp/+/39555>`_ [VeC 45]: nat: fix nat44-ed address removal from fib
  | `38524 <https:////gerrit.fd.io/r/c/vpp/+/38524>`_ [VeC 52]: fib: fix interface resolve from unlinked fib entries
  | `38245 <https:////gerrit.fd.io/r/c/vpp/+/38245>`_ [VeC 52]: mpls: fix crashes on mpls tunnel create/delete
  | `39579 <https:////gerrit.fd.io/r/c/vpp/+/39579>`_ [VeC 52]: fib: ensure mpls dpo index is valid for its next node
  | `39580 <https:////gerrit.fd.io/r/c/vpp/+/39580>`_ [VeC 52]: fib: fix udp encap mp-safe ops and id validation

**Vratko Polak** <vrpolak@cisco.com>:

  | `38797 <https:////gerrit.fd.io/r/c/vpp/+/38797>`_ [Vec 51]: ip: make running_fragment_id thread safe
  | `39316 <https:////gerrit.fd.io/r/c/vpp/+/39316>`_ [VeC 59]: ip-neighbor: add version 3 of neighbor event
  | `39315 <https:////gerrit.fd.io/r/c/vpp/+/39315>`_ [Vec 65]: vppapigen: recognize also _event as to_network

**Xiaoming Jiang** <jiangxiaoming@outlook.com>:

  | `38871 <https:////gerrit.fd.io/r/c/vpp/+/38871>`_ [VeC 177]: nsh: fix plugin load failed due to undefined symbol: gre4_input_node

**Xinyao Cai** <xinyao.cai@intel.com>:

  | `38304 <https:////gerrit.fd.io/r/c/vpp/+/38304>`_ [VeC 56]: interface dpdk avf: introducing setting RSS hash key feature
  | `38876 <https:////gerrit.fd.io/r/c/vpp/+/38876>`_ [VeC 176]: dpdk: revert "flow dpdk: introduce IP in IP support for flow"

**Yahui Chen** <goodluckwillcomesoon@gmail.com>:

  | `37653 <https:////gerrit.fd.io/r/c/vpp/+/37653>`_ [Vec 77]: af_xdp: optimizing send performance

**dengfeng liu** <liudf0716@gmail.com>:

  | `39228 <https:////gerrit.fd.io/r/c/vpp/+/39228>`_ [VeC 124]: ipsec: should use praddr_ instead of pladdr_

**hui zhang** <zhanghui1715@gmail.com>:

  | `38451 <https:////gerrit.fd.io/r/c/vpp/+/38451>`_ [vec 65]: vrrp: dump vrrp vr peer

**shivansh S** <shivansh.nwk@gmail.com>:

  | `39363 <https:////gerrit.fd.io/r/c/vpp/+/39363>`_ [VeC 94]: dhcp: fix dhcp multiple client request

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
authors          59
maintainers      15
committers       0
abandoned        0
================ ===

